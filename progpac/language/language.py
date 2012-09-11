import antlr3
import os
import sys

import LanguageLexer
import LanguageParser


class Bug(object):

    def __init__(self, code, level):
        self.level = level
        self.dots = level.dots
        self.position = level.start
        self.direction = 0
        self.code=code

    def _real_direction(self):
        return self.direction % 4

    def move(self, move):
        if move == "s":
            return self.step_forward()
        elif move == "r":
            return self.turn_right()
        elif move == "l":
            return self.turn_left()
        elif move == "!":
            return move

    def step_forward(self):
        moves = (
            (1, 0), (0, -1), (-1, 0), (0, 1)
        )
        next_move = moves[self._real_direction()]
        next_step = self.level.get(
            self.position[0] + next_move[0],
            self.position[1] + next_move[1]
        )

        if next_step in (".", "o", "u"):

            self.position = (
                self.position[0] + next_move[0],
                self.position[1] + next_move[1]
            )
            if next_step == "o":
                self.level.lines[self.position[0]][self.position[1]] = "."
                self.dots.remove(self.position)
                return u"s"
            return u"s"

        else:
            return u"x"

    def turn_left(self):
        self.direction-=1
        return u"l"

    def turn_right(self):
        self.direction+=1
        return u"r"

    def walk(self):
        code = []
        for step in self.code:
            bug_step = self.move(step)
            code.append(bug_step)

            if not self.dots:
                return code + ['@']

        return code

class Language(object):

    STEPS = [
        LanguageLexer.STEP_FORWARD, LanguageLexer.TURN_LEFT,
        LanguageLexer.TURN_RIGHT
    ]

    CALL = LanguageLexer.FUNC_NAME


    def __init__(self, code):
        char_stream = antlr3.ANTLRStringStream("%s\n" % code)
        lexer = LanguageLexer.LanguageLexer(char_stream)
        tokens = antlr3.CommonTokenStream(lexer)
        parser = LanguageParser.LanguageParser(tokens)

        parser.prog()

        self.parser = parser

        self.code = self.generate_code(self.parser.code)
        self.errors = sorted(lexer.errors + parser.errors)
        if self.errors:
            self.code = []

        self.program_length = len(
            code.replace('\r\n','').replace('\n','').replace(':','')
        )

    def generate_code(self, node, call_counter=0):
        code = []

        node_children = node.getChildren() if node.getChildren() else [node]

        for element in node_children:
            if element.getType() in self.STEPS:
                code.append( element.text )
            elif element.getType() == self.CALL:
                try:
                    function = self.parser.functions[element.text]
                except KeyError:
                    self.emit_undefined_error(element)
                    return code

                if call_counter < 40:
                    code.extend(
                        self.generate_code(function, call_counter+1)
                    )
                else:
                    code.append('!')
                    return code

        return code

    def emit_undefined_error(self, element):
        self.parser.emitErrorMessage(
            "line %s:%s step '%s' undefined" % (
                element.line, element.charPositionInLine + 1, element.text
            )
        )


if __name__ == '__main__':
    sys.path.append(
        os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..')
        )
    )

    import settings
    from django.core.management import setup_environ
    setup_environ(settings)

    from progpac.core.models import Level

    level = Level.objects.all()[0]

    parser = Language("""f:lsrslsslsrsf
srsslsf""")
    print parser.code
    print parser.errors

    bug = Bug(parser.code, level)
    print bug.walk()
