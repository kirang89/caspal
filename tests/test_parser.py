# -*- coding: utf-8 -*-

import unittest

from caspal.lexer import Lexer
from caspal.parser import Parser
from caspal import ENVIRONMENT


def caspalify(text):
    lexer = Lexer(text)
    parser = Parser(lexer)
    ast = parser.parse()

    return ast.evaluate()


class CaspalParserTestCase(unittest.TestCase):

    def test_parse_arith_expr_with_precedence(self):
        self.assertEqual(
            caspalify('PROGRAM example; BEGIN a := 1+4-2 END.'), None
        )
        self.assertEqual(ENVIRONMENT['a'], 3)

        self.assertEqual(
            caspalify('PROGRAM example; BEGIN b := 1+4*2 END.'), None
        )
        self.assertEqual(ENVIRONMENT['b'], 9)

        self.assertEqual(
            caspalify('PROGRAM example; BEGIN foo := 1+4/2 END.'), None
        )
        self.assertEqual(ENVIRONMENT['foo'], 3.0)

        self.assertEqual(
            caspalify('PROGRAM example; BEGIN bar := 1*4/2 END.'), None
        )
        self.assertEqual(ENVIRONMENT['bar'], 2)

    def test_parse_arith_expr_with_user_precedence(self):
        self.assertEqual(
            caspalify('PROGRAM example; BEGIN a := 2*(10/(2+3)) END.'), None
        )
        self.assertEqual(ENVIRONMENT['a'], 4.0)

        self.assertEqual(
            caspalify('PROGRAM example; BEGIN b := 2*(2+3) END.'), None
        )
        self.assertEqual(ENVIRONMENT['b'], 10)


if __name__ == '__main__':
    unittest.main()
