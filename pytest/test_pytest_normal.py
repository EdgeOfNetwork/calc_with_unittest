import calc_funcs

def test_add():
    res = calc_funcs.add(5,3)
    if res is 8 :
        print("add_passed")

def test_sub():
    res = calc_funcs.sub(5,3)
    if res > 0:
        bool_val = True
    else:
        bool_val = False

    if bool_val is True:
        print('Sub passed')

def test_div():
    try:
        calc_funcs.div(4,0)
    except Exception as e: #억지로 0으로 나눠보자
        print(e)

def test_mul():
    res = calc_funcs.mul(5,3)
    if res < 100:
        print("test_mul error")

