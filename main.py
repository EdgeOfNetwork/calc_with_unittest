
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
        # try:
        #     self.syn_error = False
        #     self.__is_parentheses(line) #parenth check first
        #     #if self.syn_error == True:
        #         #execption raise
        #
        # except: #오류가 발생한다면.
        #     pass


    def __is_paranthesis(self, line):
        stack_for_parenth = Stack()
        for ch in line:
            if ch == "(":
                stack_for_parenth.push("(")
            elif ch == ")":
                if stack_for_parenth.is_empty() == False:
                    stack_for_parenth.pop()
                else:
                    self.syn_error = True
        if stack_for_parenth.is_empty() == False:
            self.syn_error = True


    def get_post_calc(self):
        stack_for_post_op = Stack()
        tokens = self.line
        post_fix = ""

        for ch in tokens:
            if ch == "(":
                stack_for_post_op.push(ch)
            elif ch == ")":
                while(True):
                    temp = stack_for_post_op.pop()
                    if temp != "(":
                        post_fix += temp + " "
                    else:
                        break
            elif ch == "+" or ch == "-":
                while(True):
                    if self.operator_yn(stack_for_post_op.peek()) == True:
                        post_fix += stack_for_post_op.pop() + " "
                    else:
                        break
                stack_for_post_op.push(ch)
            elif ch == "*" or ch == "/":
                while (True):
                    if stack_for_post_op.peek() == "*" or stack_for_post_op.peek() == "/":
                        post_fix += stack_for_post_op.pop() + " "
                    else:
                        break
                stack_for_post_op.push(ch)
            else:
                post_fix += ch + " "

        while(stack_for_post_op.is_empty() != True):
            post_fix += stack_for_post_op.pop() + " "

        print(post_fix)

        tokens = post_fix.split()
        stack_for_post_op.clear()
        for ch in tokens:
            if self.operator_yn(ch) == False:
                stack_for_post_op.push(ch)
            else:
                sec = float(stack_for_post_op.pop())
                fst = float(stack_for_post_op.pop())
                if ch == "*":
                    stack_for_post_op.push(fst * sec)
                elif ch == "/":
                    stack_for_post_op.push(fst / sec)
                elif ch == "+":
                    stack_for_post_op.push(fst + sec)
                else:
                    stack_for_post_op.push(fst - sec)


        result = ""
        while(stack_for_post_op.is_empty()!= True):
            result += str(stack_for_post_op.pop())

        print(result)
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

    def __is_parentheses(self):
        pass


    def __pattern_matching(self, line):
        pass



if __name__ == "__main__":
    x = input()  # 1+3 / 1 + 3 / 1      +     3 등 처리
    x = list(x)
    c = Calc(x)
    print(c.get_post_calc())
