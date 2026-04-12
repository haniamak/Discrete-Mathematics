from problemset3.myset import MySet


def test_union():
    set1 = MySet([1, 2, 3, 4])
    set2 = MySet([3, 4, 5, 6])
    result = set1.union(set2)

    assert result == MySet([1, 2, 3, 4, 5, 6])


def test_intersection():
    set1 = MySet([1, 2, 3, 4])
    set2 = MySet([3, 4, 5, 6])
    result = set1.intersection(set2)

    assert result == MySet([3, 4])


def test_relative_complement():
    set1 = MySet([1, 2, 3, 4])
    set2 = MySet([3, 4, 5, 6])

    a, b = set1.relative_complement(set2)

    assert a == MySet([1, 2])
    assert b == MySet([5, 6])


def test_cartesian_product():
    set1 = MySet([1, 2])
    set2 = MySet([3, 4])

    result = set1.cartesian_product(set2)

    assert result == MySet([(1, 3), (1, 4), (2, 3), (2, 4)])


def test_power_set():
    set1 = MySet([1, 2])

    result = set1.power_set()

    assert result == MySet(
        [
            (),
            (1,),
            (2,),
            (1, 2),
        ]
    )
