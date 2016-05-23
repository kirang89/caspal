import unittest
from caspal import *


class CaspalParserTestCase(unittest.TestCase):

    def test_parse_arith_expr_with_precedence1(self):
        l = Lexer('1+4-2')
        self.assertEqual(Parser(l).parse(), 3)

        l = Lexer('1+4*2')
        self.assertEqual(Parser(l).parse(), 9)

        l = Lexer('1+4/2')
        self.assertEqual(Parser(l).parse(), 3)

        l = Lexer('1*4/2')
        self.assertEqual(Parser(l).parse(), 2)


if __name__ == '__main__':
    unittest.main()
