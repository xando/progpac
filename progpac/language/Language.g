grammar Language;

options {
	language=Python;
	output=AST;
}

@init {
    self.functions = {}
    self.code = None
    self.errors = []
}

@lexer::init {
    self.errors = []
}

@lexer::members {
    def emitErrorMessage(self, message):
         self.errors.append(message)

    def getErrorHeader(self, e):
        return "line "+ str(e.line) +":"+ str(e.charPositionInLine + 1)+" "

    def getErrorMessage(self, e, tokenNames):
         return " there is a problem with '"+ e.c +"'"
}


@members {
    def emitErrorMessage(self, message):
         self.errors.append(message)
}

WS
    : ('\t' | ' ' | '\u000C')+ ;

NEWLINE
    : WS* '\n'
    ;

STEP_FORWARD
    : 's'
    ;

TURN_LEFT
    : 'l'
    ;

TURN_RIGHT
    : 'r'
    ;

FUNC_NAME
    : 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g'
    | 'h' | 'i' | 'j' | 'k' | 'm' | 'n' | 'o'
    | 'p' | 'q' | 't' | 'u' | 'v' | 'w' | 'x'
    | 'y' | 'z'
    ;

func_def
    : FUNC_NAME ':' body {
            self.functions[$FUNC_NAME.text] = $body.tree;
     } -> FUNC_NAME body
    ;

func_call
    : FUNC_NAME
    ;

move
    : STEP_FORWARD
    | TURN_LEFT
    | TURN_RIGHT
    | func_call
    | WS ->
    ;

body
    : move+
    ;


line: body NEWLINE {self.code = $body.tree}
    | WS? func_def NEWLINE
    | NEWLINE
    ;

prog
    : line+ EOF -> line+
    ;
