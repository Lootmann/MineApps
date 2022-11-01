from pathlib import Path
from typing import Tuple

import pytest

import myyaml
import yaml


class TestMyYaml:
    @pytest.fixture(autouse=True)
    def initial(self):
        """
        create tests

        yaml names are:
            array boolean dict empty
            int int_minus mixed string

        filename: { text: str, yaml: dict }
        """
        yamls_dir = Path("./yamls").expanduser()

        self.files = {}

        for p in yamls_dir.glob("**/*.yaml"):
            self.files[p.stem] = {
                "text": p.read_text(),
                "yaml": yaml.safe_load(p.read_text()),
            }

    def split_tests(self, filename: str) -> Tuple[str, dict]:
        return self.files[filename]["text"], self.files[filename]["yaml"]

    # def test_show(self):
    #     for k, v in self.files.items():
    #         print("============", k)
    #         print(v["text"])
    #         print(v["yaml"])
    #         print()
    #
    def test_empty_yaml(self):
        text, want = self.split_tests("empty")
        got = myyaml.load(text)

        assert want == got

    def test_int(self):
        text, want = self.split_tests("int")
        got = myyaml.load(text)

        assert want == got

    def test_string(self):
        text, want = self.split_tests("string")
        got = myyaml.load(text)

        assert want == got
