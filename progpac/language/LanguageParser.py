# $ANTLR 3.4 Language.g 2012-09-06 00:17:54

import sys
from antlr3 import *
from antlr3.compat import set, frozenset

from antlr3.tree import *




# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EOF=-1
T__10=10
FUNC_NAME=4
NEWLINE=5
STEP_FORWARD=6
TURN_LEFT=7
TURN_RIGHT=8
WS=9

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "FUNC_NAME", "NEWLINE", "STEP_FORWARD", "TURN_LEFT", "TURN_RIGHT", "WS", 
    "':'"
]




class LanguageParser(Parser):
    grammarFileName = "Language.g"
    api_version = 1
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(LanguageParser, self).__init__(input, state, *args, **kwargs)



              
        self.functions = {}
        self.code = None
        self.errors = []


        self.delegates = []

	self._adaptor = None
	self.adaptor = CommonTreeAdaptor()



    def getTreeAdaptor(self):
        return self._adaptor

    def setTreeAdaptor(self, adaptor):
        self._adaptor = adaptor

    adaptor = property(getTreeAdaptor, setTreeAdaptor)

             
    def emitErrorMessage(self, message):
         self.errors.append(message)


    class func_def_return(ParserRuleReturnScope):
        def __init__(self):
            super(LanguageParser.func_def_return, self).__init__()

            self.tree = None





    # $ANTLR start "func_def"
    # Language.g:61:1: func_def : FUNC_NAME ':' body -> FUNC_NAME body ;
    def func_def(self, ):
        retval = self.func_def_return()
        retval.start = self.input.LT(1)


        root_0 = None

        FUNC_NAME1 = None
        char_literal2 = None
        body3 = None


        FUNC_NAME1_tree = None
        char_literal2_tree = None
        stream_10 = RewriteRuleTokenStream(self._adaptor, "token 10")
        stream_FUNC_NAME = RewriteRuleTokenStream(self._adaptor, "token FUNC_NAME")
        stream_body = RewriteRuleSubtreeStream(self._adaptor, "rule body")
        try:
            try:
                # Language.g:62:5: ( FUNC_NAME ':' body -> FUNC_NAME body )
                # Language.g:62:7: FUNC_NAME ':' body
                pass 
                FUNC_NAME1 = self.match(self.input, FUNC_NAME, self.FOLLOW_FUNC_NAME_in_func_def274) 
                stream_FUNC_NAME.add(FUNC_NAME1)


                char_literal2 = self.match(self.input, 10, self.FOLLOW_10_in_func_def276) 
                stream_10.add(char_literal2)


                self._state.following.append(self.FOLLOW_body_in_func_def278)
                body3 = self.body()

                self._state.following.pop()
                stream_body.add(body3.tree)


                #action start
                                         
                self.functions[FUNC_NAME1.text] = body3.tree;
                     
                #action end


                # AST Rewrite
                # elements: FUNC_NAME, body
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 64:8: -> FUNC_NAME body
                self._adaptor.addChild(root_0, 
                stream_FUNC_NAME.nextNode()
                )

                self._adaptor.addChild(root_0, stream_body.nextTree())




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "func_def"


    class func_call_return(ParserRuleReturnScope):
        def __init__(self):
            super(LanguageParser.func_call_return, self).__init__()

            self.tree = None





    # $ANTLR start "func_call"
    # Language.g:67:1: func_call : FUNC_NAME ;
    def func_call(self, ):
        retval = self.func_call_return()
        retval.start = self.input.LT(1)


        root_0 = None

        FUNC_NAME4 = None

        FUNC_NAME4_tree = None

        try:
            try:
                # Language.g:68:5: ( FUNC_NAME )
                # Language.g:68:7: FUNC_NAME
                pass 
                root_0 = self._adaptor.nil()


                FUNC_NAME4 = self.match(self.input, FUNC_NAME, self.FOLLOW_FUNC_NAME_in_func_call303)
                FUNC_NAME4_tree = self._adaptor.createWithPayload(FUNC_NAME4)
                self._adaptor.addChild(root_0, FUNC_NAME4_tree)





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "func_call"


    class move_return(ParserRuleReturnScope):
        def __init__(self):
            super(LanguageParser.move_return, self).__init__()

            self.tree = None





    # $ANTLR start "move"
    # Language.g:71:1: move : ( STEP_FORWARD | TURN_LEFT | TURN_RIGHT | func_call | WS ->);
    def move(self, ):
        retval = self.move_return()
        retval.start = self.input.LT(1)


        root_0 = None

        STEP_FORWARD5 = None
        TURN_LEFT6 = None
        TURN_RIGHT7 = None
        WS9 = None
        func_call8 = None


        STEP_FORWARD5_tree = None
        TURN_LEFT6_tree = None
        TURN_RIGHT7_tree = None
        WS9_tree = None
        stream_WS = RewriteRuleTokenStream(self._adaptor, "token WS")

        try:
            try:
                # Language.g:72:5: ( STEP_FORWARD | TURN_LEFT | TURN_RIGHT | func_call | WS ->)
                alt1 = 5
                LA1 = self.input.LA(1)
                if LA1 == STEP_FORWARD:
                    alt1 = 1
                elif LA1 == TURN_LEFT:
                    alt1 = 2
                elif LA1 == TURN_RIGHT:
                    alt1 = 3
                elif LA1 == FUNC_NAME:
                    alt1 = 4
                elif LA1 == WS:
                    alt1 = 5
                else:
                    nvae = NoViableAltException("", 1, 0, self.input)

                    raise nvae


                if alt1 == 1:
                    # Language.g:72:7: STEP_FORWARD
                    pass 
                    root_0 = self._adaptor.nil()


                    STEP_FORWARD5 = self.match(self.input, STEP_FORWARD, self.FOLLOW_STEP_FORWARD_in_move320)
                    STEP_FORWARD5_tree = self._adaptor.createWithPayload(STEP_FORWARD5)
                    self._adaptor.addChild(root_0, STEP_FORWARD5_tree)




                elif alt1 == 2:
                    # Language.g:73:7: TURN_LEFT
                    pass 
                    root_0 = self._adaptor.nil()


                    TURN_LEFT6 = self.match(self.input, TURN_LEFT, self.FOLLOW_TURN_LEFT_in_move328)
                    TURN_LEFT6_tree = self._adaptor.createWithPayload(TURN_LEFT6)
                    self._adaptor.addChild(root_0, TURN_LEFT6_tree)




                elif alt1 == 3:
                    # Language.g:74:7: TURN_RIGHT
                    pass 
                    root_0 = self._adaptor.nil()


                    TURN_RIGHT7 = self.match(self.input, TURN_RIGHT, self.FOLLOW_TURN_RIGHT_in_move336)
                    TURN_RIGHT7_tree = self._adaptor.createWithPayload(TURN_RIGHT7)
                    self._adaptor.addChild(root_0, TURN_RIGHT7_tree)




                elif alt1 == 4:
                    # Language.g:75:7: func_call
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_func_call_in_move344)
                    func_call8 = self.func_call()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, func_call8.tree)



                elif alt1 == 5:
                    # Language.g:76:7: WS
                    pass 
                    WS9 = self.match(self.input, WS, self.FOLLOW_WS_in_move352) 
                    stream_WS.add(WS9)


                    # AST Rewrite
                    # elements: 
                    # token labels: 
                    # rule labels: retval
                    # token list labels: 
                    # rule list labels: 
                    # wildcard labels: 
                    retval.tree = root_0
                    if retval is not None:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                    else:
                        stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                    root_0 = self._adaptor.nil()
                    # 76:10: ->
                    root_0 = None



                    retval.tree = root_0




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "move"


    class body_return(ParserRuleReturnScope):
        def __init__(self):
            super(LanguageParser.body_return, self).__init__()

            self.tree = None





    # $ANTLR start "body"
    # Language.g:79:1: body : ( move )+ ;
    def body(self, ):
        retval = self.body_return()
        retval.start = self.input.LT(1)


        root_0 = None

        move10 = None



        try:
            try:
                # Language.g:80:5: ( ( move )+ )
                # Language.g:80:7: ( move )+
                pass 
                root_0 = self._adaptor.nil()


                # Language.g:80:7: ( move )+
                cnt2 = 0
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == FUNC_NAME or (STEP_FORWARD <= LA2_0 <= WS)) :
                        alt2 = 1


                    if alt2 == 1:
                        # Language.g:80:7: move
                        pass 
                        self._state.following.append(self.FOLLOW_move_in_body371)
                        move10 = self.move()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, move10.tree)



                    else:
                        if cnt2 >= 1:
                            break #loop2

                        eee = EarlyExitException(2, self.input)
                        raise eee

                    cnt2 += 1




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "body"


    class line_return(ParserRuleReturnScope):
        def __init__(self):
            super(LanguageParser.line_return, self).__init__()

            self.tree = None





    # $ANTLR start "line"
    # Language.g:84:1: line : ( body NEWLINE | ( WS )? func_def NEWLINE | NEWLINE );
    def line(self, ):
        retval = self.line_return()
        retval.start = self.input.LT(1)


        root_0 = None

        NEWLINE12 = None
        WS13 = None
        NEWLINE15 = None
        NEWLINE16 = None
        body11 = None

        func_def14 = None


        NEWLINE12_tree = None
        WS13_tree = None
        NEWLINE15_tree = None
        NEWLINE16_tree = None

        try:
            try:
                # Language.g:84:5: ( body NEWLINE | ( WS )? func_def NEWLINE | NEWLINE )
                alt4 = 3
                LA4 = self.input.LA(1)
                if LA4 == STEP_FORWARD or LA4 == TURN_LEFT or LA4 == TURN_RIGHT:
                    alt4 = 1
                elif LA4 == FUNC_NAME:
                    LA4_2 = self.input.LA(2)

                    if (LA4_2 == 10) :
                        alt4 = 2
                    elif ((FUNC_NAME <= LA4_2 <= WS)) :
                        alt4 = 1
                    else:
                        nvae = NoViableAltException("", 4, 2, self.input)

                        raise nvae


                elif LA4 == WS:
                    LA4_3 = self.input.LA(2)

                    if ((NEWLINE <= LA4_3 <= WS)) :
                        alt4 = 1
                    elif (LA4_3 == FUNC_NAME) :
                        LA4_2 = self.input.LA(3)

                        if (LA4_2 == 10) :
                            alt4 = 2
                        elif ((FUNC_NAME <= LA4_2 <= WS)) :
                            alt4 = 1
                        else:
                            nvae = NoViableAltException("", 4, 2, self.input)

                            raise nvae


                    else:
                        nvae = NoViableAltException("", 4, 3, self.input)

                        raise nvae


                elif LA4 == NEWLINE:
                    alt4 = 3
                else:
                    nvae = NoViableAltException("", 4, 0, self.input)

                    raise nvae


                if alt4 == 1:
                    # Language.g:84:7: body NEWLINE
                    pass 
                    root_0 = self._adaptor.nil()


                    self._state.following.append(self.FOLLOW_body_in_line385)
                    body11 = self.body()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, body11.tree)


                    NEWLINE12 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_line387)
                    NEWLINE12_tree = self._adaptor.createWithPayload(NEWLINE12)
                    self._adaptor.addChild(root_0, NEWLINE12_tree)



                    #action start
                    self.code = body11.tree
                    #action end



                elif alt4 == 2:
                    # Language.g:85:7: ( WS )? func_def NEWLINE
                    pass 
                    root_0 = self._adaptor.nil()


                    # Language.g:85:7: ( WS )?
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == WS) :
                        alt3 = 1
                    if alt3 == 1:
                        # Language.g:85:7: WS
                        pass 
                        WS13 = self.match(self.input, WS, self.FOLLOW_WS_in_line397)
                        WS13_tree = self._adaptor.createWithPayload(WS13)
                        self._adaptor.addChild(root_0, WS13_tree)






                    self._state.following.append(self.FOLLOW_func_def_in_line400)
                    func_def14 = self.func_def()

                    self._state.following.pop()
                    self._adaptor.addChild(root_0, func_def14.tree)


                    NEWLINE15 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_line402)
                    NEWLINE15_tree = self._adaptor.createWithPayload(NEWLINE15)
                    self._adaptor.addChild(root_0, NEWLINE15_tree)




                elif alt4 == 3:
                    # Language.g:86:7: NEWLINE
                    pass 
                    root_0 = self._adaptor.nil()


                    NEWLINE16 = self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_line410)
                    NEWLINE16_tree = self._adaptor.createWithPayload(NEWLINE16)
                    self._adaptor.addChild(root_0, NEWLINE16_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "line"


    class prog_return(ParserRuleReturnScope):
        def __init__(self):
            super(LanguageParser.prog_return, self).__init__()

            self.tree = None





    # $ANTLR start "prog"
    # Language.g:89:1: prog : ( line )+ EOF -> ( line )+ ;
    def prog(self, ):
        retval = self.prog_return()
        retval.start = self.input.LT(1)


        root_0 = None

        EOF18 = None
        line17 = None


        EOF18_tree = None
        stream_EOF = RewriteRuleTokenStream(self._adaptor, "token EOF")
        stream_line = RewriteRuleSubtreeStream(self._adaptor, "rule line")
        try:
            try:
                # Language.g:90:5: ( ( line )+ EOF -> ( line )+ )
                # Language.g:90:7: ( line )+ EOF
                pass 
                # Language.g:90:7: ( line )+
                cnt5 = 0
                while True: #loop5
                    alt5 = 2
                    LA5_0 = self.input.LA(1)

                    if ((FUNC_NAME <= LA5_0 <= WS)) :
                        alt5 = 1


                    if alt5 == 1:
                        # Language.g:90:7: line
                        pass 
                        self._state.following.append(self.FOLLOW_line_in_prog427)
                        line17 = self.line()

                        self._state.following.pop()
                        stream_line.add(line17.tree)



                    else:
                        if cnt5 >= 1:
                            break #loop5

                        eee = EarlyExitException(5, self.input)
                        raise eee

                    cnt5 += 1


                EOF18 = self.match(self.input, EOF, self.FOLLOW_EOF_in_prog430) 
                stream_EOF.add(EOF18)


                # AST Rewrite
                # elements: line
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 
                retval.tree = root_0
                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 90:17: -> ( line )+
                # Language.g:90:20: ( line )+
                if not (stream_line.hasNext()):
                    raise RewriteEarlyExitException()

                while stream_line.hasNext():
                    self._adaptor.addChild(root_0, stream_line.nextTree())


                stream_line.reset()




                retval.tree = root_0





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)

        finally:
            pass
        return retval

    # $ANTLR end "prog"



 

    FOLLOW_FUNC_NAME_in_func_def274 = frozenset([10])
    FOLLOW_10_in_func_def276 = frozenset([4, 6, 7, 8, 9])
    FOLLOW_body_in_func_def278 = frozenset([1])
    FOLLOW_FUNC_NAME_in_func_call303 = frozenset([1])
    FOLLOW_STEP_FORWARD_in_move320 = frozenset([1])
    FOLLOW_TURN_LEFT_in_move328 = frozenset([1])
    FOLLOW_TURN_RIGHT_in_move336 = frozenset([1])
    FOLLOW_func_call_in_move344 = frozenset([1])
    FOLLOW_WS_in_move352 = frozenset([1])
    FOLLOW_move_in_body371 = frozenset([1, 4, 6, 7, 8, 9])
    FOLLOW_body_in_line385 = frozenset([5])
    FOLLOW_NEWLINE_in_line387 = frozenset([1])
    FOLLOW_WS_in_line397 = frozenset([4])
    FOLLOW_func_def_in_line400 = frozenset([5])
    FOLLOW_NEWLINE_in_line402 = frozenset([1])
    FOLLOW_NEWLINE_in_line410 = frozenset([1])
    FOLLOW_line_in_prog427 = frozenset([4, 5, 6, 7, 8, 9])
    FOLLOW_EOF_in_prog430 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("LanguageLexer", LanguageParser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
