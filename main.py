"""
다시,

    처음부터 너무 크게 생각했다.

    그런데 그거에 비해 설계가 없었다.

"""


class Calc:

    def __init__(self, line):
        self.line = line
        self.__pattern_matching(line)

    def __pattern_matching(self,line):
        for i in range(len(line)): # (3+5)/2
            if i is "(":             #try-catch로 괄호가 안닫꼈음을 경고

            else:
                pass

    def __add(self):
        pass

    def __minus(self):
        pass

    def __divide(self):
        pass

    def __multi(self):
        pass

    def __is_paranthesis(self, line):
        if line is "(":

        else:
            return


if __name__ == "__main__":
    x = map(input())  # 1+3 / 1 + 3 / 1      +     3 등 처리
    c = Calc(x)

    #c.whatis(1+3)
    """
    계산기 뭐가필요해?
    
    input이랑 output
    즉, 2 + 5 면 7
    """

