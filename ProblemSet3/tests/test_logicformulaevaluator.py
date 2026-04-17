from problemset3.logicformulaevaluator import extract_variables


def test_extract_variables():
    formula = "A AND B OR NOT C IMPLIES D"
    expected = {"A", "B", "C", "D"}
    assert set(extract_variables(formula)) == expected
