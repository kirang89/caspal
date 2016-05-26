# -*- coding: utf-8 -*-

from .token import Token, TokenType, RESERVED_KEYWORDS, DATATYPES


class Lexer(object):
    """The lexer for Caspal.

    Gets a stream of characters and converts them into tokens that are then
    sent to the parser.

    """

    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def advance(self):
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def ignore_whitespace(self):
        """Ignores whitespace character from stream"""
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def keyword(self):
        """Fetches a keyword from character stream"""
        ch = self.current_char
        kw = ''

        while ch is not None and ch.isalpha():
            kw += ch
            self.advance()
            ch = self.current_char

        return kw

    def get_next_token(self):
        ch = self.current_char

        if ch is None:
            return Token(TokenType.EOF, None)

        if ch.isspace():
            self.ignore_whitespace()
            ch = self.current_char

        if ch.isdigit():
            self.advance()
            return Token(TokenType.NUMBER, ch)

        if ch == '+':
            self.advance()
            return Token(TokenType.PLUS, ch)

        if ch == '-':
            self.advance()
            return Token(TokenType.MINUS, ch)

        if ch == '*':
            self.advance()
            return Token(TokenType.MULT, ch)

        if ch == '/':
            self.advance()
            return Token(TokenType.DIV, ch)

        if ch == '(':
            self.advance()
            return Token(TokenType.LPAREN, ch)

        if ch == ')':
            self.advance()
            return Token(TokenType.RPAREN, ch)

        if ch == ':':
            self.advance()
            if self.current_char == '=':
                self.advance()
                return Token(TokenType.ASSIGN, ':=')
            else:
                return Token(TokenType.COLON, ':')

        if ch == ';':
            self.advance()
            return Token(TokenType.SEMICOLON, ch)

        if ch == ',':
            self.advance()
            return Token(TokenType.COMMA, ch)

        if ch.isalpha():
            kw = self.keyword()

            return RESERVED_KEYWORDS.get(kw.lower()) or \
                DATATYPES.get(kw) or \
                Token(TokenType.NAME, kw)

        if ch == '.':
            self.advance()
            return Token(TokenType.DOT, '.')

        raise Exception('Invalid char: {}'.format(ch))

    def get_all_tokens(self):
        """Fetches all tokens from a stream, at once."""
        tokens = []
        token = self.get_next_token()
        while token is not None and token.type != TokenType.EOF:
            tokens.append(token)
            token = self.get_next_token()

        return tokens
