import unittest
import calc_funcs

""" 실행순서 ? """
""" assert 없이 TestCase 실행하는 법 """


class TddTest(unittest.TestCase):
    def test_add(self):
        res = calc_funcs.add(5, 3)
        if res is 9:
            print("add_passed")

    def test_sub(self):
        res = calc_funcs.sub(5, 3)
        if res > 0:
            bool_val = True
        else:
            bool_val = False

        if bool_val is True:
            print('Sub passed')

    def test_div(self):
        try:
            calc_funcs.div(4, 0)
        except Exception as e:  # 억지로 0으로 나눠보자
            print(e)

    def test_mul(self):
        res = calc_funcs.mul(5, 3)
        if res < 100:
            print("test_mul error")


if __name__ == "__main__":
    unittest.main()
