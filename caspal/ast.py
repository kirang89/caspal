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
        ENVIRONMENT[self.var] = self.value.evaluate()

    def __repr__(self):
        return 'Assignment(var={}, value={})'.format(
            self.var, self.value
        )
