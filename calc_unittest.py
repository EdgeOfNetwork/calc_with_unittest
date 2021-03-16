import unittest


class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return self.stack == []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        n = len(self.stack)
        temp = ""
        if n != 0:
            temp = self.stack[n - 1]
            del self.stack[n - 1]
        return temp

    def clear(self):
        self.stack = []

    def peek(self):
        n = len(self.stack)
        if n > 0:
            return self.stack[n - 1]

    def stack_print(self):
        n = len(self.stack)
        if n > 0:
            for i in range(0, n):
                print(self.stack[n - 1 - i])


class Calc:
    def __init__(self, line):
        self.line = line
        calc_stack = Stack()

        self.syn_error = False  # 왜 쓰는건지 이해하고 쓰자
        for ch in line:  # 괄호검사
            if ch == "(":
                calc_stack.push("(")
            elif ch == ")":
                if calc_stack.is_empty() == False:
                    pop_ch = calc_stack.pop()
                else:
                    self.syn_error = True
        if calc_stack.is_empty() == False:
            self.syn_error = True

    def get_post_calc(self):  # 후위연산으로 변경
        calc_stack2 = Stack()
        tokens = self.line
        post_fix = ""

        for ch in tokens:
            if ch == "(":
                calc_stack2.push(ch)
            elif ch == ")":
                while (True):
                    temp = calc_stack2.pop()
                    if temp != "(":
                        post_fix += temp + " "
                    else:
                        break
            elif ch == "+" or ch == "-":
                while (True):
                    if self.operator_yn(calc_stack2.peek()) == True:
                        post_fix += calc_stack2.pop() + " "
                    else:
                        break
                calc_stack2.push(ch)
            elif ch == "*" or ch == "/":
                while (True):
                    if calc_stack2.peek() == "*" or calc_stack2.peek() == "/":
                        post_fix += calc_stack2.pop() + " "
                    else:
                        break
                calc_stack2.push(ch)
            else:
                post_fix += ch + " "

        while (calc_stack2.is_empty() != True):
            post_fix += calc_stack2.pop() + " "

        #print(post_fix)

        tokens = post_fix.split()
        calc_stack2.clear()
        for ch in tokens:
            if self.operator_yn(ch) == False:
                calc_stack2.push(ch)
            else:
                sec = float(calc_stack2.pop())
                fst = float(calc_stack2.pop())
                if ch == "*":
                    calc_stack2.push(fst * sec)
                elif ch == "/":
                    calc_stack2.push(fst / sec)
                elif ch == "+":
                    calc_stack2.push(fst + sec)
                else:
                    calc_stack2.push(fst - sec)

        result = ""
        while (calc_stack2.is_empty() != True):
            result += str(calc_stack2.pop())

        #print(result)
        return result

    def operator_yn(self, item):
        if item == "*":
            return True
        elif item == "/":
            return True
        elif item == "+":
            return True
        elif item == "-":
            return True
        else:
            return False


class TestCalc(unittest.TestCase):
    def test_덧셈(self):
        # given
        x = "1+3"
        c = Calc(x)

        # when
        x = c.get_post_calc()

        # then
        self.assertEqual(x, "4.0")

    def test_뺄셈(self):
        # given
        x = "1-4"
        c = Calc(x)
        # when
        x = c.get_post_calc()

        # then
        self.assertEqual(x, "-3.0")

    def test_나눗셈(self):
        # given
        x = "2/4"
        c = Calc(x)
        # when
        x = c.get_post_calc()

        # then
        self.assertEqual(x, "0.5")

    def test_곱셈(self):
        # given
        x = "2*4"
        c = Calc(x)
        # when
        x = c.get_post_calc()

        # then
        self.assertEqual(x, "8.0")

    def test_두개이상연산(self):
        # given
        x = "2+2*4"
        c = Calc(x)
        # when
        x = c.get_post_calc()

        # then
        self.assertEqual(x, "10.0")
        #16을 띄우면 00raiseError 출력하게 합시다.


    def test_괄호검사(self):
        # given
        x = "(2+4)/4"
        c = Calc(x)
        # when
        x = c.get_post_calc()

        # then
        self.assertEqual(x, "1.5")


    def _괄호_에러테스트(self):
        # given
        x = ")2+4)/4"
        y = "(2+4/4"
        c = Calc(x)
        d = Calc(y)
        # when
        x = c.get_post_calc()
        y = d.get_post_calc()

        # then
        #try catch가 잘 되는지
        #self.assertEqual(x, "1.5")

    def test_순서_에러테스트(self):
        pass


if __name__ == "__main__":
    unittest.main()
