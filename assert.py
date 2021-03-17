
"""

The assert keyword lets you test 
if a condition in your code returns True, 
if not, the program will raise an AssertionError.

"""
assert True #nothing happened

x = "hello"

#if condition returns False, AssertionError is raised:
assert x == "goodbye", "x should be 'hello'"




""" assert 어떻게 쓰는지 보여준다. """
#위에 지우면 아래가 돌아감을 보여줌

a = 2
b = 4
assert a + b == 5, "a+b should be 6"

