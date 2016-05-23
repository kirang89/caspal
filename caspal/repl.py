from caspal import *            # noqa
from cmd import Cmd


class CaspalREPL(Cmd):
    """The REPL for Caspal"""

    prompt = "caspal > "
    intro = "Welcome to Caspal 0.0.1\n"

    def run(self, text):
        lexer = Lexer(text)
        # print(lexer.get_all_tokens())

        parser = Parser(lexer)
        ast = parser.parse()

        print(ast.evaluate())

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
