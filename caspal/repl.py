# -*- coding: utf-8 -*-

from . import version
from .lexer import Lexer
from .parser import Parser
from cmd import Cmd


class CaspalREPL(Cmd):
    """The REPL for Caspal"""

    prompt = "caspal > "
    intro = "Welcome to Caspal {}\n".format(version)

    def run(self, text):
        lexer = Lexer(text)
        # print(lexer.get_all_tokens())

        parser = Parser(lexer)
        ast = parser.parse()

        print(ast.evaluate())
        self.show_env()

    def show_env(self):
        from . import ENVIRONMENT

        print("=======================================================")
        print("Environment:\n")
        print(ENVIRONMENT)
        print("=======================================================")

    def default(self, line):
        self.run(line)

    def postcmd(self, stop, line):
        print("")

    def do_exit(self, line):
        """Exit from the REPL"""
        import sys
        sys.exit(1)

    def do_EOF(self, line):
        return True
