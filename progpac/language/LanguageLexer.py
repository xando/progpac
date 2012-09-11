# $ANTLR 3.4 Language.g 2012-09-06 00:17:55

import sys
from antlr3 import *
from antlr3.compat import set, frozenset



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


class LanguageLexer(Lexer):

    grammarFileName = "Language.g"
    api_version = 1

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super(LanguageLexer, self).__init__(input, state)

        self.delegates = []

        self.dfa3 = self.DFA3(
            self, 3,
            eot = self.DFA3_eot,
            eof = self.DFA3_eof,
            min = self.DFA3_min,
            max = self.DFA3_max,
            accept = self.DFA3_accept,
            special = self.DFA3_special,
            transition = self.DFA3_transition
            )


                           
        self.errors = []



                             
    def emitErrorMessage(self, message):
         self.errors.append(message)

    def getErrorHeader(self, e):
        return "line "+ str(e.line) +":"+ str(e.charPositionInLine + 1)+" "

    def getErrorMessage(self, e, tokenNames):
         return " there is a problem with '"+ e.c +"'"



    # $ANTLR start "T__10"
    def mT__10(self, ):
        try:
            _type = T__10
            _channel = DEFAULT_CHANNEL

            # Language.g:21:7: ( ':' )
            # Language.g:21:9: ':'
            pass 
            self.match(58)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__10"



    # $ANTLR start "WS"
    def mWS(self, ):
        try:
            _type = WS
            _channel = DEFAULT_CHANNEL

            # Language.g:36:5: ( ( '\\t' | ' ' | '\\u000C' )+ )
            # Language.g:36:7: ( '\\t' | ' ' | '\\u000C' )+
            pass 
            # Language.g:36:7: ( '\\t' | ' ' | '\\u000C' )+
            cnt1 = 0
            while True: #loop1
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if (LA1_0 == 9 or LA1_0 == 12 or LA1_0 == 32) :
                    alt1 = 1


                if alt1 == 1:
                    # Language.g:
                    pass 
                    if self.input.LA(1) == 9 or self.input.LA(1) == 12 or self.input.LA(1) == 32:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    if cnt1 >= 1:
                        break #loop1

                    eee = EarlyExitException(1, self.input)
                    raise eee

                cnt1 += 1




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "WS"



    # $ANTLR start "NEWLINE"
    def mNEWLINE(self, ):
        try:
            _type = NEWLINE
            _channel = DEFAULT_CHANNEL

            # Language.g:39:5: ( ( WS )* '\\n' )
            # Language.g:39:7: ( WS )* '\\n'
            pass 
            # Language.g:39:7: ( WS )*
            while True: #loop2
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if (LA2_0 == 9 or LA2_0 == 12 or LA2_0 == 32) :
                    alt2 = 1


                if alt2 == 1:
                    # Language.g:39:7: WS
                    pass 
                    self.mWS()



                else:
                    break #loop2


            self.match(10)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "NEWLINE"



    # $ANTLR start "STEP_FORWARD"
    def mSTEP_FORWARD(self, ):
        try:
            _type = STEP_FORWARD
            _channel = DEFAULT_CHANNEL

            # Language.g:43:5: ( 's' )
            # Language.g:43:7: 's'
            pass 
            self.match(115)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "STEP_FORWARD"



    # $ANTLR start "TURN_LEFT"
    def mTURN_LEFT(self, ):
        try:
            _type = TURN_LEFT
            _channel = DEFAULT_CHANNEL

            # Language.g:47:5: ( 'l' )
            # Language.g:47:7: 'l'
            pass 
            self.match(108)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TURN_LEFT"



    # $ANTLR start "TURN_RIGHT"
    def mTURN_RIGHT(self, ):
        try:
            _type = TURN_RIGHT
            _channel = DEFAULT_CHANNEL

            # Language.g:51:5: ( 'r' )
            # Language.g:51:7: 'r'
            pass 
            self.match(114)



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "TURN_RIGHT"



    # $ANTLR start "FUNC_NAME"
    def mFUNC_NAME(self, ):
        try:
            _type = FUNC_NAME
            _channel = DEFAULT_CHANNEL

            # Language.g:55:5: ( 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h' | 'i' | 'j' | 'k' | 'm' | 'n' | 'o' | 'p' | 'q' | 't' | 'u' | 'v' | 'w' | 'x' | 'y' | 'z' )
            # Language.g:
            pass 
            if (97 <= self.input.LA(1) <= 107) or (109 <= self.input.LA(1) <= 113) or (116 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "FUNC_NAME"



    def mTokens(self):
        # Language.g:1:8: ( T__10 | WS | NEWLINE | STEP_FORWARD | TURN_LEFT | TURN_RIGHT | FUNC_NAME )
        alt3 = 7
        alt3 = self.dfa3.predict(self.input)
        if alt3 == 1:
            # Language.g:1:10: T__10
            pass 
            self.mT__10()



        elif alt3 == 2:
            # Language.g:1:16: WS
            pass 
            self.mWS()



        elif alt3 == 3:
            # Language.g:1:19: NEWLINE
            pass 
            self.mNEWLINE()



        elif alt3 == 4:
            # Language.g:1:27: STEP_FORWARD
            pass 
            self.mSTEP_FORWARD()



        elif alt3 == 5:
            # Language.g:1:40: TURN_LEFT
            pass 
            self.mTURN_LEFT()



        elif alt3 == 6:
            # Language.g:1:50: TURN_RIGHT
            pass 
            self.mTURN_RIGHT()



        elif alt3 == 7:
            # Language.g:1:61: FUNC_NAME
            pass 
            self.mFUNC_NAME()








    # lookup tables for DFA #3

    DFA3_eot = DFA.unpack(
        u"\2\uffff\1\10\6\uffff"
        )

    DFA3_eof = DFA.unpack(
        u"\11\uffff"
        )

    DFA3_min = DFA.unpack(
        u"\1\11\1\uffff\1\11\6\uffff"
        )

    DFA3_max = DFA.unpack(
        u"\1\172\1\uffff\1\40\6\uffff"
        )

    DFA3_accept = DFA.unpack(
        u"\1\uffff\1\1\1\uffff\1\3\1\4\1\5\1\6\1\7\1\2"
        )

    DFA3_special = DFA.unpack(
        u"\11\uffff"
        )


    DFA3_transition = [
        DFA.unpack(u"\1\2\1\3\1\uffff\1\2\23\uffff\1\2\31\uffff\1\1\46\uffff"
        u"\13\7\1\5\5\7\1\6\1\4\7\7"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\2\1\3\1\uffff\1\2\23\uffff\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #3

    class DFA3(DFA):
        pass


 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(LanguageLexer)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
