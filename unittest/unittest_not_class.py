import unittest
import calc_funcs


# class TddTest(unittest.TestCase):
#     def test_add(self):
#         self.assertEqual(calc_funcs.add(5, 3), 7)
#
#     def test_sub(self):
#         res = calc_funcs.sub(5, 3)
#         if res > 2:
#             bool_val = True
#         else:
#             bool_val = False
#
#         self.assertTrue(bool_val)
#
#     def test_div(self):
#         self.assertRaises(ZeroDivisionError, calc_funcs.div(4, 0))
#
#     def test_mul(self):
#         none_check = True
#         res = calc_funcs.mul(10, 9)
#
#         if res > 100:
#             none_check = None
#
#         self.assertIsNone(none_check)


def test_add():
    assert calc_funcs.add(10,20), 30


if __name__ == "__main__":
    testcase = unittest.FunctionTestCase(test_add(),
                                         setUp=setUp,
                                         tearDown=tearDown)
