from collections import defaultdict

EQ = '='
PIPE = '|'
DOL = '$'


class Parser:
    """
    Command parser. Execution steps are:

    1. Substitute variables.
    2. Remove single quotes.
    3. Check if line is an assignment, if it is, then update storage (globals) with a new variable.
    4. Pipe split into separate tokens and return to shell for further execution.
    """

    def __init__(self):
        self.globals = defaultdict()

    def parse(self, line):
        """Parses single line into separated command (by pipe)
        and splits each of them into tokens."""

        line = self.substitute(line)
        line = line.strip('\n')

        single_quotes_count = line.count('\'')
        double_quotes_count = line.count('\"')
        if single_quotes_count % 2 != 0 or double_quotes_count % 2 != 0:
            raise Exception("Incorrect command: odd number of single quotes")

        line = line.replace('\'', '').replace('\"', '')

        is_assignment = self.check_assignment(line)

        if is_assignment:
            return None

        commands = line.split(PIPE)
        return [command.lstrip().split(' ') for command in commands]

    def substitute(self, line):
        """Executes $ substitution"""

        line = line.replace('\"', '')

        is_dollar = False
        is_quote_expected = False
        var_name = ''

        for char in line:
            if char == '\'':
                is_quote_expected = not is_quote_expected

            elif char == DOL and not is_quote_expected:
                if is_dollar:
                    raise Exception("Incorrect statement")

                is_dollar = True
            elif is_dollar:
                if not is_quote_expected and char in (' ', '\n'):
                    if var_name not in self.globals.keys():
                        raise ValueError("Incorrect variable name: {}".format(var_name))
                    var_value = self.globals[var_name]
                    line = line.replace(DOL + var_name, var_value)
                    var_name = ''
                else:
                    var_name += char

        return line

    def check_assignment(self, line):
        """Checks, if command is assignment, and implement this assignment."""

        if line.count(' ') == 0 and line.count('\t') == 0 and EQ in line:
            var, value = line.split(EQ)
            if not var or '$' in var:
                raise KeyError("Incorrect variable name: {}".format(var))

            self.globals[var] = value
            return True

        return False
