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
        line = self.substitute(line)
        line = line.strip('\n')
        line = self.remove_quotes(line)
        is_assignment = self.check_assignment(line)

        if is_assignment:
            return None

        commands = line.split(PIPE)
        return [command.lstrip().split(' ') for command in commands]

    def substitute(self, line: str) -> str:
        """Executes $ substitution"""

        line = line.replace('\"', '')

        isDollar = False
        isQuoteExpected = False
        var_name = ''

        for ch in line:
            if ch == '\'':
                isQuoteExpected = not isQuoteExpected

            elif ch == DOL and not isQuoteExpected:
                if isDollar:
                    raise Exception("Incorrect statement")

                isDollar = True
            elif isDollar:
                if not isQuoteExpected and (ch == ' ' or ch == '\n'):
                    if var_name not in self.globals.keys():
                        raise ValueError("Incorrect variable name: {}".format(var_name))
                    var_value = self.globals[var_name]
                    line = line.replace(DOL + var_name, var_value)
                    var_name = ''
                else:
                    var_name += ch

        return line

    def remove_quotes(self, line: str) -> str:
        single_quotes_count = line.count('\'')
        double_quotes_count = line.count('\"')
        if single_quotes_count % 2 != 0 or double_quotes_count % 2 != 0:
            raise Exception("Incorrect command: odd number of single quotes")

        line = line.replace('\'', '').replace('\"', '')
        return line

    def check_assignment(self, line: str):
        if line.count(' ') == 0 and line.count('\t') == 0 and EQ in line:
            var, value = line.split(EQ)
            if len(var) == 0 or '$' in var:
                raise KeyError("Incorrect variable name: {}".format(var))

            self.globals[var] = value
            return True

        return False
