import json

import pytest
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


def test_recursive_file_expansion_json(capsys, recursive_json_filename, tmpdir):
    """
    Test resolution on recursive refs

    Based on the JSONSchema spec, refs *can* be recursive:
      https://json-schema.org/understanding-json-schema/structuring.html#recursion
    """
    with pytest.raises(SystemExit) as excinfo:
        main([recursive_json_filename])
    expected_error_message = (
        "error processing {}: "
        "recursion detected with allow_recursive=False\n".format(
            recursive_json_filename
        )
    )
    assert excinfo.value.code == 1
    assert capsys.readouterr().err == expected_error_message
