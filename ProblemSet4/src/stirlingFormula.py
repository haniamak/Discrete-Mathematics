from math import factorial, sqrt, pi, e


def stirling_formula(n):
    if n == 0:
        return 1
    else:
        return round((n / e) ** n * sqrt((2 * pi * n)), 3)


def compare_stirling(n):
    for i in range(n + 1):
        actual = factorial(i)
        approximation = stirling_formula(i)
        print(
            f"n: {i}, Actual value: {actual}, Stirling's Approximation: {approximation}"
        )


if __name__ == "__main__":
    n = 10
    compare_stirling(n)
