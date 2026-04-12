from __future__ import annotations
from typing import Any


class MySet:
    def __init__(self, myset: list[Any]):
        self.myset = myset

    def __eq__(self, other: MySet) -> bool:
        if not isinstance(other, MySet):
            return False
        return self.myset == other.myset

    def union(self, other: MySet) -> MySet:
        if not isinstance(other, MySet):
            raise TypeError("Union expects argument of type MySet")
        result = list(self.myset)
        for element in other.myset:
            if element not in result:
                result.append(element)
        return MySet(result)

    def intersection(self, other: MySet) -> MySet:
        if not isinstance(other, MySet):
            raise TypeError("Intersection expects argument of type MySet")
        result = []
        for element in self.myset:
            if element in other.myset:
                result.append(element)
        return MySet(result)

    def relative_complement(self, other: MySet) -> tuple[MySet, MySet]:
        if not isinstance(other, MySet):
            raise TypeError("Relative Complement expects argument of type MySet")
        result_a = []
        result_b = []
        for element in self.myset:
            if element not in other.myset:
                result_a.append(element)
        for element in other.myset:
            if element not in self.myset:
                result_b.append(element)
        return MySet(result_a), MySet(result_b)

    def cartesian_product(self, other: MySet) -> MySet:
        if not isinstance(other, MySet):
            raise TypeError("Cartesian Product expects argument of type MySet")
        result = []
        for element_a in self.myset:
            for element_b in other.myset:
                result.append((element_a, element_b))
        return MySet(result)

    def power_set(self) -> MySet:
        result: list[tuple[Any, ...]] = [()]
        for element in self.myset:
            subset = []
            for curr in result:
                tmp = list(curr)
                tmp.append(element)
                subset.append(tuple(tmp))
            for curr in subset:
                result.append(curr)
        return MySet(result)
