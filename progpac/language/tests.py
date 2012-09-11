import unittest

import LanguageLexer
import LanguageParser
import antlr3

from language import Language


class TestLanguageParser(unittest.TestCase):

    def test_parse(self):
        code = """

        ssrsrs

        """

        char_stream = antlr3.ANTLRStringStream(code + "\n")
        lexer = LanguageLexer.LanguageLexer(char_stream)
        tokens = antlr3.CommonTokenStream(lexer)
        parser = LanguageParser.LanguageParser(tokens)

        parser.prog()

        self.assertEqual(lexer.errors,[])
        self.assertEqual(parser.errors,[])


class TestLanguage(unittest.TestCase):

    def test_simple(self):
        code = """



        ssrsrs
        """

        parser = Language(code)

        self.assertEqual(parser.code, ['s','s','r','s','r','s'])
        self.assertEqual(parser.errors, [])

    def test_func(self):
        code = """x:sss
        x
        """

        parser = Language(code)

        self.assertEqual(parser.code, ['s','s','s'])
        self.assertEqual(parser.errors, [])

    def test_func_with_code(self):
        code = """x:sss
        xrr
        """

        parser = Language(code)

        self.assertEqual(parser.code, ['s','s','s','r','r'])

    def test_code_with_new_lines(self):
        code = """
        x:sss

        xrr
        """

        parser = Language(code)

        self.assertEqual(parser.code, ['s','s','s','r','r'])


if __name__ == '__main__':
    unittest.main()