from resolvref import resolve_references


def test_recursive_expansion():
    """
    Test resolution on recursive refs without restriction
    """
    doc = resolve_references({"foo": {"bar": {"$ref": "#/foo"}}})
    assert doc["foo"]["bar"] == doc["foo"]
