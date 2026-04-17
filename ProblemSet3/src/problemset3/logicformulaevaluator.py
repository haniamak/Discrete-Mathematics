from __future__ import annotations

from itertools import product


def AND(a: bool, b: bool) -> bool:
    return a and b


def OR(a: bool, b: bool) -> bool:
    return a or b


def NOT(a: bool) -> bool:
    return not a


def IMPLIES(a: bool, b: bool) -> bool:
    return (not a) or b


def extract_variables(formula: str):
    tokens = formula.replace("(", " ").replace(")", " ").replace(",", " ").split()
    return sorted({t for t in tokens if t not in {"AND", "OR", "NOT", "IMPLIES"}})


def enter_formula():
    formula = input("Enter a logical formula (use AND, OR, NOT, IMPLIES): ")
    return formula


def truth_table(formula: str):
    vars = extract_variables(formula)

    width = max(len(v) for v in vars)
    header = " | ".join(v.center(width) for v in vars) + " | RES"
    print(header)
    print("-" * len(header))

    for combination in product([False, True], repeat=len(vars)):
        values = dict(zip(vars, combination))

        context = {
            **values,
            "AND": AND,
            "OR": OR,
            "NOT": NOT,
            "IMPLIES": IMPLIES,
        }

        result = eval(formula, {}, context)

        row = " | ".join(("T" if v else "F").center(width) for v in values.values())
        row += " | " + ("T" if result else "F").center(3)

        print(row)


if __name__ == "__main__":
    formula = enter_formula()
    truth_table(formula)
