# -*- coding: utf-8 -*-

import operator
from . import ENVIRONMENT


class AST(object):
    """Represents the AST(Abstract Syntax Tree) of a Caspal program"""

    def evaluate(self):
        """Method that describes how an AST node should be evaluated"""
        pass

    def __repr__(self):
        pass


class Number(AST):
    """The AST node for a number(integer)"""

    def __init__(self, value):
        self.value = value

    def evaluate(self):
        return self.value

    def __repr__(self):
        return 'Number({})'.format(self.value)


class BinOp(AST):
    """The AST node for a binary operation"""

    def __init__(self, op, left, right):
        self.op = op
        self.left, self.right = left, right

    def evaluate(self):
        op_map = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }

        operation = op_map[self.op]

        return operation(self.left.evaluate(), self.right.evaluate())

    def __repr__(self):
        return 'BinOp(op={}, left={}, right={})'.format(
            self.op, self.left, self.right
        )


class Assignment(AST):
    """The AST node of an assignment statement"""

    def __init__(self, var, value):
        self.var, self.value = var, value

    def evaluate(self):
        if self.var in ENVIRONMENT.keys():
            ENVIRONMENT[self.var] = self.value.evaluate()
        else:
            raise Exception('Variable {} not declared'.format(self.var))

    def __repr__(self):
        return 'Assignment(var={}, value={})'.format(
            self.var, self.value
        )


class CompoundStatement(AST):
    """The AST node of a compound statement

    a.k.a node that represents multiple statements seperated by ;
    """

    def __init__(self, statements):
        self.statements = statements

    def evaluate(self):
        for statement in self.statements:
            statement.evaluate()

    def __repr__(self):
        return 'CompoundStatement({})'.format(self.statements)


class Declaration(AST):
    """The AST node that takes care of variable declarations"""

    def __init__(self, vars):
        self.vars = vars

    def evaluate(self):
        for var in self.vars:
            ENVIRONMENT[var] = None

    def __repr__(self):
        return 'Declaration({})'.format(self.vars)


class Program(AST):
    """The AST node that represents the PROGRAM block

    The PROGRAM block in Caspal consists of:
    - variable declarations
    - the main block
    """

    def __init__(self, declarations=None, main=None):
        self.declarations = declarations or []
        self.main = main

    def evaluate(self):
        self.declarations.evaluate()
        self.main.evaluate()

    def __repr__(self):
        return 'Program(decl={}, main={})'.format(self.declarations, self.main)
