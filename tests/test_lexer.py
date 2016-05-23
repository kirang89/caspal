# -*- coding: utf-8 -*-

import unittest
from caspal.token import Token, TokenType
from caspal.lexer import Lexer


class CaspalLexerTestCase(unittest.TestCase):

    def test_add_expression(self):
        l = Lexer('21 + 12')
        tokens = l.get_all_tokens()
        expected = [Token(TokenType.NUMBER, '2'),
                    Token(TokenType.NUMBER, '1'),
                    Token(TokenType.PLUS, '+'),
                    Token(TokenType.NUMBER, '1'),
                    Token(TokenType.NUMBER, '2')]
        self.assertEquals(tokens, expected)

    def test_subtract_expression(self):
        l = Lexer('1234 - 24')
        tokens = l.get_all_tokens()
        expected = [Token(TokenType.NUMBER, '1'),
                    Token(TokenType.NUMBER, '2'),
                    Token(TokenType.NUMBER, '3'),
                    Token(TokenType.NUMBER, '4'),
                    Token(TokenType.MINUS, '-'),
                    Token(TokenType.NUMBER, '2'),
                    Token(TokenType.NUMBER, '4')]
        self.assertEquals(tokens, expected)

    def test_multiplication_expression(self):
        l = Lexer('2 * 24')
        tokens = l.get_all_tokens()
        expected = [Token(TokenType.NUMBER, '2'),
                    Token(TokenType.MULT, '*'),
                    Token(TokenType.NUMBER, '2'),
                    Token(TokenType.NUMBER, '4')]
        self.assertEquals(tokens, expected)

    def test_division_expression(self):
        l = Lexer('66 / 2')
        tokens = l.get_all_tokens()
        expected = [Token(TokenType.NUMBER, '6'),
                    Token(TokenType.NUMBER, '6'),
                    Token(TokenType.DIV, '/'),
                    Token(TokenType.NUMBER, '2')]
        self.assertEquals(tokens, expected)


if __name__ == '__main__':
    unittest.main()
