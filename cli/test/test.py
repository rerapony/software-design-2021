import os
import sys

import pytest

from cli.src.command.cat import Cat
from cli.src.command.echo import Echo
from cli.src.command.grep import Grep
from cli.src.command.pwd import Pwd
from cli.src.command.wc import Wc
from cli.src.factory.command_factory import CommandFactory
from cli.src.parser import Parser
from cli.src.shell import Shell

TEST_FILE = os.path.join(sys.path[0], "cli/test/temp.txt")
INPUT_FILE = os.path.join(sys.path[0], "cli/test/input_file.txt")
OUTPUT_FILE = os.path.join(sys.path[0], "cli/test/output_file.txt")

PWD_PATH = "/home/valeria/software-design-2021/cli/test"


@pytest.mark.parametrize("args", [[TEST_FILE]])
def test_cat_command(args):
    with open(TEST_FILE, 'r') as test_file:
        data = test_file.read()

    command = Cat()
    result = command.execute("", 0, *args)

    assert data == result


@pytest.mark.parametrize("args", [[], ["one", "two", "three"]])
def test_echo_command(args):
    command = Echo()
    result = command.execute("", 0, *args)

    assert " ".join(args) == result


@pytest.mark.parametrize("args", [[], ["one", "two", "three"]])
def test_pwd_command(args):
    command = Pwd()
    result = command.execute("", 0, *args)

    assert PWD_PATH == result


@pytest.mark.parametrize("args", [([TEST_FILE], "2 2 68")])
def test_wc_command(args):
    command_ans = args[1]
    command_args = args[0]

    command = Wc()
    result = command.execute("", 0, *command_args)

    assert command_ans == result


@pytest.mark.parametrize("args", [(['b', TEST_FILE], "bbbbbbbbbb")])
def test_grep_command(args):
    command_ans = args[1]
    command_args = args[0]

    command = Grep()
    result = command.execute("", 0, *command_args)

    assert command_ans == result


@pytest.mark.parametrize("args", [("cat {} | wc".format(TEST_FILE), "2 2 68\n"),
                                  ("echo 1111111 222 | wc", "1 2 12\n"),
                                  ("echo aaaaaaaaaaaaaaaaaaaaaaaaaa | pwd", PWD_PATH + '\n')])
def test_pipe(args):
    command_ans = args[1]
    command_args = args[0]

    with open(INPUT_FILE, 'w') as pipe_file:
        pipe_file.write(command_args)

    open(OUTPUT_FILE, "w").close()

    with open(INPUT_FILE, "r") as input_file:
        with open(OUTPUT_FILE, "w") as output_file:
            shell = Shell(CommandFactory(), Parser(), input_file, output_file)
            shell.run_shell()

    with open(OUTPUT_FILE, 'r') as output_file:
        data = output_file.read()

    assert command_ans == data


@pytest.mark.parametrize("args", [("cat \"{}\" | wc\n".format(TEST_FILE), "2 2 68\n"),
                                  ("cat \'{}\' | wc\n".format(TEST_FILE), "2 2 68\n"),
                                  ("echo \"1111111\" 222 | wc\n", "1 2 12\n"),
                                  ("echo \'1111111\' 222 | wc\n", "1 2 12\n")])
def test_quotes(args):
    command_ans = args[1]
    command_args = args[0]

    with open(INPUT_FILE, 'w') as input_file:
        input_file.write(command_args)

    open(OUTPUT_FILE, "w").close()

    with open(INPUT_FILE, "r") as input_file:
        with open(OUTPUT_FILE, "w") as output_file:
            shell = Shell(CommandFactory(), Parser(), input_file, output_file)
            shell.run_shell()

    with open(OUTPUT_FILE, 'r') as output_file:
        data = output_file.read()

    assert command_ans == data


@pytest.mark.parametrize("args", [("var=1\n echo var\n", "var\n"),
                                  ("var=1\n echo $var\n", "1\n"),
                                  ("var=1\n echo \'$var\'\n", "$var\n"),
                                  ("var=1\n echo \"$var\"\n", "1\n")])
def test_variables(args):
    command_ans = args[1]
    command_args = args[0]

    with open(INPUT_FILE, 'w') as input_file:
        input_file.write(command_args)

    open(OUTPUT_FILE, "w").close()

    with open(INPUT_FILE, "r") as input_file:
        with open(OUTPUT_FILE, "w") as output_file:
            shell = Shell(CommandFactory(), Parser(), input_file, output_file)
            shell.run_shell()

    with open(OUTPUT_FILE, 'r') as output_file:
        data = output_file.read()

    assert command_ans == data
