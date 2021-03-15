"""

목표 :
1. 사칙연산 + () 순서까지 연산이 가능한 계산기가 만들어져야 한다.
    1-1 input으로? 4+6 = 10 과 (15-3)/4 를 주입

    str로 들어오면 담겨진 요소들을 분리해야한다.



    1-2 output으로?


2. unittest로 유닛테스팅 확인
2-1. 무엇을 유닛테스트 할 지
    given / when / assert ?? 형식으로 유닛테스트 준비

3. pytest로 유닛테스트 확인


"""


class Calc:

    def __init__(self, line):
        self.line = line
        self.__pattern_matching(line)
        self.list = []
        for i in self.line:
            self.list.append(i) # 문장 들어온거 리스트로 몽땅 집어넣고
                                #리스트에 들어온거 에서 ( ) 이거 판별합시다.

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

