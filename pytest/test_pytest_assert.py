import calc_funcs

def test_add():
    assert calc_funcs.add(5,3), 8

def test_sub():
    res = calc_funcs.sub(5,3)
    if res > 0:
        bool_val = True
    else:
        bool_val = False

    assert bool_val is True

def test_div():
    assert calc_funcs.div(4, 0)

def test_mul():
    none_check = True
    res = calc_funcs.mul(10, 9)

    if res > 100:
        none_check = None

    assert none_check is None

