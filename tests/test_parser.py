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
        self.assertEqual(caspalify('1+4-2'), 3)
        self.assertEqual(caspalify('1+4*2'), 9)
        self.assertEqual(caspalify('1+4/2'), 3)
        self.assertEqual(caspalify('1*4/2'), 2)

    def test_parse_arith_expr_with_user_precedence(self):
        self.assertEqual(caspalify('2*(10/(2+3))'), 4)
        self.assertEqual(caspalify('2*(2+3)'), 10)


if __name__ == '__main__':
    unittest.main()
