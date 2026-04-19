### This project contains implementations of a framework for creating sets and multisets with listed below set operations:

- Union of two sets ( A ) and ( B )

- Intersection of two sets

- Relative complement ( A \setminus B ) and ( B \setminus A )

- Absolute complement (with respect to a universal set ( U ))

- Cartesian product ( A \times B )

- Power set ( all possible subsets )

- Inclusion–exclusion principle to compute the cardinality of sets

- Characteristic function to check if an element belongs to a set

### Second part of the project contains an implementation of a logic formula evaluator that can evaluate logical expressions for all possible combinations of truth values of the variables involved in the expression.

### To run unit tests, use the following command in the terminal:
```bash
uv run pytest
```

### To run logic formula evaluator, use the following command in the terminal:
```bash
uv run python src/problemset3/logicformulaevaluator.py
```