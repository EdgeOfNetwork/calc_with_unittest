"""
목표 :
1. 사칙연산 + () 순서까지 연산이 가능한 계산기가 만들어져야 한다.
    1-1 input으로? 4+6 = 10 과 (15-3)/4 를 주입
    str로 들어오면 담겨진 요소들을 분리해야한다.
    1-2 output으로?

    1-3 stack!
    Stack을 이용해야

2. unittest로 유닛테스팅 확인
2-1. 무엇을 유닛테스트 할 지
    given / when / assert ?? 형식으로 유닛테스트 준비

3. pytest로 유닛테스트 확인
"""
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
        if n!=0:
            temp = self.stack[n-1]
            del self.stack[n-1]
        return temp

    def clear(self):
        self.stack=[]

    def peek(self):
        n = len(self.stack)
        if n > 0:
            return self.stack[n-1]

    def stack_print(self):
        n = len(self.stack)
        if n > 0:
            for i in range(0, n):
                print(self.stack[n-1-i])


class Calc:
    def __init__(self, line):
        self.line = line
        calc_stack = Stack()

        #아래 괄호검사로 함수화
        self.syn_error = False # 왜 쓰는건지 이해하고 쓰자
        for ch in line: #괄호검사
            if ch == "(":
                calc_stack.push("(")
            elif ch == ")":
                if calc_stack.is_empty() == False:
                    pop_ch = calc_stack.pop()
                else:
                    self.syn_error = True
        if calc_stack.is_empty() == False:
            self.syn_error = True

    def get_post_calc(self): #후위연산으로 변경
        calc_stack2 = Stack()
        tokens = self.line
        post_fix = ""

        for ch in tokens:
            if ch == "(":
                calc_stack2.push(ch)
            elif ch == ")":
                while(True):
                    temp = calc_stack2.pop()
                    if temp != "(":
                        post_fix += temp + " "
                    else:
                        break
            elif ch == "+" or ch == "-":
                while(True):
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

        while(calc_stack2.is_empty() != True):
            post_fix += calc_stack2.pop() + " "

        print(post_fix)

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
        while(calc_stack2.is_empty()!= True):
            result += str(calc_stack2.pop())

        print(result)
        return result

    # def __init__(self, line): #str로 input이 온다.
    #     self.buffer = [] #버퍼를 만들어서 연산과정을 기록한다.
    #     self.line = list(line) #list로 감싸서 하나하나 담는다.
    #     self.__is_paranthesis() #괄호검사 -> 괄호 검사 후
    #     result = self.__pattern_matching(self.line)

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

    def __pattern_matching(self, line):
        pass


    # def __is_paranthesis(self, line):
    #     if "(" in line or ")":
    #         try:
    #         except:
    #
    #     else:

if __name__ == "__main__":
    x = input()  # 1+3 / 1 + 3 / 1      +     3 등 처리
    x = list(x)
    c = Calc(x)
    print(c.get_post_calc())
