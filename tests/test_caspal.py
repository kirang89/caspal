# -*- coding: utf-8 -*-

import unittest

from caspal.lexer import Lexer
from caspal.parser import Parser
from caspal import ENVIRONMENT


def evaluate(text):
    lexer = Lexer(text)
    parser = Parser(lexer)
    ast = parser.parse()

    return ast.evaluate()


class CaspalTestCase(unittest.TestCase):

    def test_arith_expr_with_precedence(self):
        self.assertEqual(
            evaluate('PROGRAM example; Var a : integer; BEGIN a := 1+4-2 END.'), None
        )
        self.assertEqual(ENVIRONMENT['a'][0], 3)

        self.assertEqual(
            evaluate('PROGRAM example; Var b: integer; BEGIN b := 1+4*2 END.'), None
        )
        self.assertEqual(ENVIRONMENT['b'][0], 9)

        self.assertEqual(
            evaluate('PROGRAM example; Var foo:integer; BEGIN foo := 1+4/2 END.'), None
        )
        self.assertEqual(ENVIRONMENT['foo'][0], 3.0)

        self.assertEqual(
            evaluate('PROGRAM example; Var bar:integer; BEGIN bar := 1*4/2 END.'), None
        )
        self.assertEqual(ENVIRONMENT['bar'][0], 2)

    def test_arith_expr_with_user_precedence(self):
        self.assertEqual(
            evaluate('PROGRAM example; Var a:integer; BEGIN a := 2*(10/(2+3)) END.'), None
        )
        self.assertEqual(ENVIRONMENT['a'][0], 4.0)

        self.assertEqual(
            evaluate('PROGRAM example; Var b:integer; BEGIN b := 2*(2+3) END.'), None
        )
        self.assertEqual(ENVIRONMENT['b'][0], 10)

    def test_multiple_statements(self):
        self.assertEqual(
            evaluate('PROGRAM example; Var a:integer; BEGIN a := 2*(10/(2+3)); b := 4 END.'),
            None
        )
        self.assertEqual(ENVIRONMENT['a'][0], 4.0)
        self.assertEqual(ENVIRONMENT['b'][0], 4)

        self.assertEqual(
            evaluate('PROGRAM example; Var b, d:integer; BEGIN b := 2*(2+3); c := 1 + 3; d := 12 END.'),  # noqa
            None
        )
        self.assertEqual(ENVIRONMENT['b'][0], 10)
        self.assertEqual(ENVIRONMENT['c'][0], 4)
        self.assertEqual(ENVIRONMENT['d'][0], 12)

    def test_declarations(self):
        self.assertEqual(
            evaluate(
                'PROGRAM example; Var a,b,c:integer; BEGIN a := 2; b := 3; c := 4 END.'
            ), None)

        self.assertEqual(ENVIRONMENT['b'][0], 3)
        self.assertEqual(ENVIRONMENT['c'][0], 4)
        self.assertEqual(ENVIRONMENT['a'][0], 2)


if __name__ == '__main__':
    unittest.main()
