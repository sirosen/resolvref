import json

import yaml

import pytest


@pytest.fixture
def make_json_file(tmpdir):
    def _make_json_file(doc, filename="doc.json"):
        filename = str(tmpdir.join(filename))
        with open(filename, "w") as fp:
            json.dump(doc, fp)
        return filename

    return _make_json_file


@pytest.fixture
def make_yaml_file(tmpdir):
    def _make_yaml_file(doc, filename="doc.yaml"):
        filename = str(tmpdir.join(filename))
        with open(filename, "w") as fp:
            yaml.dump(doc, fp)
        return filename

    return _make_yaml_file
