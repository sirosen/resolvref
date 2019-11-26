import os

import pytest

HERE = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture(scope="session")
def simple_yaml_filename():
    return os.path.join(os.path.dirname(HERE), "files", "simple.yaml")


@pytest.fixture(scope="session")
def simple_json_filename():
    return os.path.join(os.path.dirname(HERE), "files", "simple.json")
