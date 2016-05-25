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

    def __init__(self, type, value):
        self.type, self.value = type, value

    def evaluate(self):
        return self.type(self.value)

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

        if isinstance(self.left, Number) and isinstance(self.right, Number):
            msg = 'Type Mismatch: {} and {}'.format(
                self.left.type, self.right.type
            )
            assert self.left.type == self.right.type, msg

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
        if self.var.name in ENVIRONMENT.keys():
            _, _type = ENVIRONMENT[self.var.name]
            val = self.value.evaluate()
            ENVIRONMENT[self.var.name] = (_type(val), _type)
        else:
            raise Exception('Variable {} not declared'.format(self.var.name))

    def __repr__(self):
        return 'Assignment(var={}, value={})'.format(
            self.var.name, self.value
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
        for var, var_type in self.vars:
            ENVIRONMENT[var] = (None, var_type)

    def __repr__(self):
        return 'Declaration({})'.format(self.vars)


class Variable(AST):
    """The AST node that takes care of variables"""

    def __init__(self, name):
        self.name = name

    def evaluate(self):
        value, _type = ENVIRONMENT[self.name]
        return _type(value)

    def __repr__(self):
        return 'Variable({})'.format(self.name)


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
