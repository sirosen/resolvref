import json

import yaml

from resolvref.main import main


def test_simple_file_expansion_yaml(simple_yaml_filename, tmpdir):
    outputfile = str(tmpdir.join("dest.yaml"))
    main([simple_yaml_filename, "-o", outputfile])
    with open(outputfile, "r") as fp:
        result = yaml.load(fp)
    assert result == {
        "part1": {
            "k1": "a string",
            "k2": 1,
            "k3": ["a list", "of strings"],
            "k4": {"k5": {"k6": {"k7": "a deeply nested object"}}},
        },
        "part2": {
            "otherdoc": {
                "k1": "a string",
                "k2": 1,
                "k3": ["a list", "of strings"],
                "k4": {"k5": {"k6": {"k7": "a deeply nested object"}}},
            }
        },
    }


def test_simple_file_expansion_json(simple_json_filename, tmpdir):
    outputfile = str(tmpdir.join("dest.json"))
    main([simple_json_filename, "-o", outputfile])
    with open(outputfile, "r") as fp:
        result = json.load(fp)
    assert result == {
        "part1": {
            "k1": "a string",
            "k2": 1,
            "k3": ["a list", "of strings"],
            "k4": {"k5": {"k6": {"k7": "a deeply nested object"}}},
        },
        "part2": {
            "otherdoc": {
                "k1": "a string",
                "k2": 1,
                "k3": ["a list", "of strings"],
                "k4": {"k5": {"k6": {"k7": "a deeply nested object"}}},
            }
        },
    }


def test_simple_file_expansion_json_loaded_as_yaml(simple_json_filename, tmpdir):
    outputfile = str(tmpdir.join("dest.yaml"))
    main([simple_json_filename, "-o", outputfile, "-f", "yaml"])
    with open(outputfile, "r") as fp:
        result = yaml.load(fp)
    assert result == {
        "part1": {
            "k1": "a string",
            "k2": 1,
            "k3": ["a list", "of strings"],
            "k4": {"k5": {"k6": {"k7": "a deeply nested object"}}},
        },
        "part2": {
            "otherdoc": {
                "k1": "a string",
                "k2": 1,
                "k3": ["a list", "of strings"],
                "k4": {"k5": {"k6": {"k7": "a deeply nested object"}}},
            }
        },
    }
