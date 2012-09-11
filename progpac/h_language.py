import re

from lepl import *
from lepl.matchers.error import syntax_error_kargs

from django.core.management import setup_environ

from progpac.core.models import Level, Bug


def init(self, stream):
    self.lineno = s_deepest(stream)[1]._delta[1]
    self.offset = s_deepest(stream)[1]._delta[0]
    self.msg = "The match failed"

FullFirstMatchException.__init__ = init


def with_line(node):
    def wrapper(results, stream_out, **kwargs):
        location_helper = syntax_error_kargs(
            kwargs['stream_in'], stream_out, results)
        return node(results,
                    in_lineno=location_helper['in_lineno'],
                    in_char=location_helper['in_char'])
    return wrapper


class List(List):
    def __init__(self, *args, **kwargs):
        self.in_lineno = kwargs.pop('in_lineno', 0)
        self.in_char = kwargs.pop('in_char', 0)
        super(List, self).__init__(*args, **kwargs)


class Func(List):
    @property
    def name(self):
        return self[0]

    @property
    def args(self):
        try:
            if isinstance(self[1], FuncArgs):
                return self[1]
        except IndexError:
            pass
        return []

    @property
    def body(self):
        return filter(lambda x: isinstance(x,Body), self)[0]

class FuncCall(Func):
    pass

class FuncDef(Func):
    pass

class Variable(List):
    @property
    def name(self):
        return self[0]

class FuncArgs(List): pass

class Move(List): pass

class Main(List): pass

class Body(List): pass


# Drop
comma = ~Token(',')
left_bracket = ~Token("\(")
right_bracket = ~Token("\)")

# Predefinition
call = Delayed()
func = Delayed()

move = Token("[lsr]") ** with_line(Move) # > (lambda x: "".join(x)))
variable = Token('[A-Z]') ** with_line(Variable)
body = (move[1:] | call | variable)[1:] ** with_line(Body)

func_name = Token("[abcdefghijkmnopqtuvwxyz]")

# Function Call
call_digits = Token('[A-Z]') & Token('\-') & Token("[0-9]")[1:] > (lambda x: "".join(x))
call_args = left_bracket & Or(move[1:], call_digits)[1:, comma] & right_bracket > FuncArgs
call+= (func_name & call_args[:1]) ** with_line(FuncCall)

# Function definition
func_sep = ~Token(":")
func_args = left_bracket & Token('[A-Z]')[1:, comma] & right_bracket > FuncArgs
func_loc = Token('[A-Z]')
func+= (func_name & func_args[:1] & func_sep & body) ** with_line(FuncDef)

line = LineStart() & Or(func, body)[:] & LineEnd()
parser = (line[:] > Main)
parser.config.lines()


class Parser(object):

    def __init__(self, program, level=None):

        self.bug = Bug(level)
        self.code = []
        self.code_debug = []
        self.body = None
        self.ast = None
        self.funcs = {}
        self.error = None
        self.program = program
        self.program_length = len(re.sub("[\s:]", "", self.program))

        try:
            self.ast = parser.parse(program)[0]
            try:
                self.body = filter(lambda x: x.__class__ == Body, self.ast)[0]
            except IndexError:
                self.body = ""
            self.funcs = dict(
                map(lambda x: (x[0], x),
                filter(lambda x: isinstance(x,FuncDef), self.ast)))

            self.go(self.body)
        except (Error, FullFirstMatchException) as e:
            self.error = "Line: %s, Character: %s. %s" % (
                e.lineno, e.offset, e.msg)

    def go(self, body, loc=None):
        if loc is None:
            loc = {}

        for element in body:
            if "@" in self.code:
                break

            if isinstance(element, Move):
                move = element[0]
                if self.bug:
                    move = self.bug.move(move)
                    self.code.append(move)
                    self.code_debug.append(
                        (element.in_lineno, element.in_char, move))
                else:
                    self.code.append(move)

            elif isinstance(element, Variable):
                pass

            elif isinstance(element, FuncCall):
                function_call = element

                try:
                    function_def = self.funcs[element.name]
                except KeyError:
                    raise Error("Function %s not defined." % element.name,
                                {"in_lineno": element.in_lineno,
                                 "in_offset": element.in_char})

                if len(function_def.args) != len(element.args):
                    raise Error("Wrong arguments in function %s call." % element.name,
                                {"in_lineno": element.in_lineno,
                                 "in_offset": element.in_char})
                args = dict(zip(function_def.args, function_call.args))
                try:
                    self.go(function_def.body, args)
                except RuntimeError:
                    self.code.append("!")


if __name__ == "__main__":
    import settings
    setup_environ(settings)

    program =  """x:lslsrssrsls
    f:xxx
    srsslsf
    """
    first_level = Level.objects.all()[0]
    parser = Parser(program, first_level)
    print "".join(parser.code)
