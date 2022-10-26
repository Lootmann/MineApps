from pathlib import Path

import pytest


class TestMyYaml:
    @pytest.fixture(autouse=True)
    def initial(self):
        yamls_dir = Path("./yamls").expanduser()

        # filename, filepath
        self.paths = {}

        for p in yamls_dir.glob("**/*.yaml"):
            self.paths[p.stem] = p.read_text()

    def test_empty_yaml(self):
        for filename, o in self.paths.items():
            print(filename, o)
