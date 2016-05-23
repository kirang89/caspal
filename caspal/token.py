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
