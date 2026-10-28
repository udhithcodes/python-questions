# 1. Identify the output if the input is 3
#     ```
n=input()
# print(n*n) # TypeError: can't multiply sequence by non-int of type 'str'
print(n+n+n) # 333
print(4*n)   # 3333
# print(n/2) # TypeError: unsupported operand type(s) for /: 'str' and 'int'
# print(n-n) # TypeError: unsupported operand type(s) for -: 'str' and 'str'
#     ```