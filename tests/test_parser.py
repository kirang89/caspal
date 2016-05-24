# -*- coding: utf-8 -*-

import unittest
from caspal.lexer import Lexer
from caspal.parser import Parser


def caspalify(text):
    lexer = Lexer(text)
    parser = Parser(lexer)
    ast = parser.parse()

    return ast.evaluate()


class CaspalParserTestCase(unittest.TestCase):

    def test_parse_arith_expr_with_precedence(self):
        self.assertEqual(caspalify('PROGRAM example; BEGIN 1+4-2 END.'), 3)
        self.assertEqual(caspalify('PROGRAM example; BEGIN 1+4*2 END.'), 9)
        self.assertEqual(caspalify('PROGRAM example; BEGIN 1+4/2 END.'), 3)
        self.assertEqual(caspalify('PROGRAM example; BEGIN 1*4/2 END.'), 2)

    def test_parse_arith_expr_with_user_precedence(self):
        self.assertEqual(
            caspalify('PROGRAM example; BEGIN 2*(10/(2+3)) END.'), 4)
        self.assertEqual(caspalify('PROGRAM example; BEGIN 2*(2+3) END.'), 10)


if __name__ == '__main__':
    unittest.main()
