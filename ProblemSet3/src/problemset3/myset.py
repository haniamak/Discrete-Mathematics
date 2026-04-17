from __future__ import annotations
from typing import Any
from itertools import combinations


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

    def absolute_complement(self, universal: MySet) -> MySet:
        return MySet([x for x in universal.myset if x not in self.myset])

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

    def characteristic_function(self, element: Any) -> int:
        return 1 if element in self.myset else 0

    @staticmethod
    def inclusion_exclusion_principle(sets: list[MySet]) -> int:
        if not all(isinstance(s, MySet) for s in sets):
            raise TypeError(
                "Inclusion-Exclusion Principle expects a list of MySet instances"
            )

        def intersection_many(sets: list[MySet]) -> MySet:
            if not sets:
                return MySet([])
            result = sets[0]
            for s in sets[1:]:
                result = result.intersection(s)
            return MySet(result.myset)

        cardinality = 0
        for k in range(1, len(sets) + 1):
            for subset in combinations(sets, k):
                size = len(intersection_many(list(subset)).myset)
                if k % 2 == 1:
                    cardinality += size
                else:
                    cardinality -= size
        return cardinality
