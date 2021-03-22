import pytest
import calc_funcs


@pytest.fixture
def default_numb():
    aa = 10
    bb = 20
    cc = 30
    return [aa, bb, cc]


@pytest.mark.add
def test_add(default_numb):
    res = calc_funcs.add(default_numb[0], default_numb[1])
    assert res is 30

@pytest.mark.add
def test_add2(default_numb):
    res = calc_funcs.add(default_numb[1], default_numb[2])
    assert res is 50


def test_sub(default_numb):
    res = calc_funcs.sub(default_numb[0], default_numb[1])

    if res > 10:
        bool_val = True
    else:
        bool_val = False

    assert bool_val is True
