import pytest

SIMPLE_DOCUMENT = {
    "part1": {"$ref": "#/part2/otherdoc"},
    "part2": {
        "otherdoc": {
            "k1": "a string",
            "k2": 1,
            "k3": ["a list", "of strings"],
            "k4": {"k5": {"k6": {"k7": "a deeply nested object"}}},
        }
    },
}

RECURSIVE_DOCUMENT = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "definitions": {
        "person": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "children": {
                    "type": "array",
                    "items": {"$ref": "#/definitions/person"},
                    "default": [],
                },
            },
        }
    },
    "type": "object",
    "properties": {"person": {"$ref": "#/definitions/person"}},
}


@pytest.fixture
def simple_yaml_filename(make_yaml_file):
    return make_yaml_file(SIMPLE_DOCUMENT)


@pytest.fixture
def simple_json_filename(make_json_file):
    return make_json_file(SIMPLE_DOCUMENT)


@pytest.fixture
def recursive_json_filename(make_json_file):
    return make_json_file(RECURSIVE_DOCUMENT)
