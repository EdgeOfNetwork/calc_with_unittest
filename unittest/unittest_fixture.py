import unittest
import calc_funcs


class TddTest(unittest.TestCase):
    aa = 0
    bb = 0
    res = 0

    def setUp(self):
        self.aa = 10
        self.bb = 20

    def test_add(self):
        self.res = calc_funcs.add(self.aa, self.bb)
        self.assertEqual(calc_funcs.add(self.res), 31)

    def test_sub(self):
        self.res = calc_funcs.sub(self.aa, self.bb)

        if self.res > 10:
            bool_val = True
        else:
            bool_val = False

        self.assertTrue(bool_val)

    def tearDown(self):
        print(' 결과 값 :' + str(self.res))


if __name__ == "__main__":
    unittest.main
