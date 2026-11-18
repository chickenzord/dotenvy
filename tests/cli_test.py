import os
import sys
from tempfile import TemporaryDirectory
from unittest.mock import patch

import pytest

import dotenvy.cli


def test_cli_main():
    with TemporaryDirectory() as d:
        dotenv = os.path.join(d, "test.env")
        with open(dotenv, "w", encoding="utf-8") as f:
            f.write("hello=world")

        args = ["prog", "--file=" + dotenv, "echo $hello"]
        with patch.object(sys, "argv", args):
            result = os.path.join(d, "result.env")
            with open(result, "w", encoding="utf-8") as out_f:
                dotenvy.cli.main(stdout=out_f)

        with open(result, encoding="utf-8") as f:
            assert f.read().rstrip() == "world"


def test_cli_main_nonexists():
    args = ["prog", "--file=notexists.env", "echo $hello"]
    with patch.object(sys, "argv", args):
        with pytest.raises(SystemExit):
            dotenvy.cli.main()
