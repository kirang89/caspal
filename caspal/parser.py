# -*- coding: utf-8 -*-

from .token import TokenType
from .ast import *              # noqa


class Parser(object):
    """Parser for Caspal.

    Parses a token generated by the Lexer and converts it into
    an AST(Abstract Syntax Tree).

    """

    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def advance(self):
        self.current_token = self.lexer.get_next_token()

    def number(self):
        """Parses a number

        Note: Can only parse an integer for now.
        """
        res = ''
        token = self.current_token

        while token is not None and token.type == TokenType.NUMBER:
            res = res + token.value
            self.advance()
            token = self.current_token

        return Number(int(res))

    def term(self):
        token = self.current_token

        if token.type == TokenType.LPAREN:
            self.advance()
            res = self.expression()
            if self.current_token.type == TokenType.RPAREN:
                self.advance()
                return res
        else:
            return self.number()

    def factor(self):
        res = self.term()
        op = self.current_token

        while op.type in (TokenType.MULT, TokenType.DIV):
            self.advance()
            res1 = self.term()

            if op.type in (TokenType.MULT, TokenType.DIV):
                res = BinOp(op=op.value, left=res, right=res1)

            op = self.current_token

        return res

    def expression(self):
        """Parses an arithmetic expression"""
        res = self.factor()
        op = self.current_token

        while op.type in (TokenType.PLUS, TokenType.MINUS):
            self.advance()
            res1 = self.factor()

            if op.type in (TokenType.PLUS, TokenType.MINUS):
                res = BinOp(op=op.value, left=res, right=res1)

            op = self.current_token

        return res

    def assignment(self):
        """Parse an assignment statement in a Caspal program"""
        var = None
        if self.current_token.type == TokenType.NAME:
            var = self.current_token.value
            self.advance()
            if self.current_token.type == TokenType.ASSIGN:
                self.advance()
                return Assignment(var, self.expression())

    def statement(self):
        return self.assignment()

    def statement_list(self):
        stmts = [self.statement()]

        while all([self.current_token is not None,
                   self.current_token.type == TokenType.SEMICOLON]):
            self.advance()
            stmts.append(self.statement())

        return CompoundStatement(stmts)

    def program_header(self):
        """Parse the header of a Caspal program"""
        token_seq = [TokenType.PROGRAM, TokenType.NAME, TokenType.SEMICOLON]
        for token_type in token_seq:
            if self.current_token.type == token_type:
                self.advance()
            else:
                raise Exception('Expected token of type {} but got {}'.format(
                    token_type, self.current_token.type
                ))

    def program(self):
        self.program_header()
        if self.current_token.type == TokenType.BEGIN:
            self.advance()
        else:
            raise Exception('Expected BEGIN, but got ' +
                            self.current_token.value)

        res = self.statement_list()

        if self.current_token.type == TokenType.END:
            self.advance()
        else:
            raise Exception('Expected END, but got ' +
                            self.current_token.value)

        if self.current_token.type == TokenType.DOT:
            return res

    def parse(self):
        return self.program()
