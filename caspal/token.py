# -*- coding: utf-8 -*-

from enum import Enum


class TokenType(Enum):
    NUMBER = 1
    PLUS = 2
    MINUS = 3
    MULT = 4
    DIV = 5
    EOF = 6
    LPAREN = 7
    RPAREN = 8
    BEGIN = 9
    END = 10
    DOT = 11
    PROGRAM = 12
    SEMICOLON = 13
    VAR = 14
    NAME = 15
    COLON = 16
    ASSIGN = 17
    COMMA = 18
    TYPE_INTEGER = 19


class Token(object):
    """Represents a lexer token"""

    def __init__(self, type, value):
        if not isinstance(type, TokenType):
            raise TypeError('Invalid token type')

        self.type, self.value = type, value

    def __eq__(self, other):
        return self.type == other.type and \
            self.value == other.value

    def __repr__(self):
        return 'Token({}, {})'.format(self.value, self.type)


RESERVED_KEYWORDS = {
    'begin': Token(TokenType.BEGIN, 'BEGIN'),
    'end': Token(TokenType.END, 'END'),
    'var': Token(TokenType.VAR, 'Var'),
    'program': Token(TokenType.PROGRAM, 'PROGRAM'),
}

DATATYPES = {
    'integer': Token(TokenType.TYPE_INTEGER, 'integer')
}
