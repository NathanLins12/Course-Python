# def factor(n):
# total = 5
#     # total = 1
#     # while n > 0:
#     #     total *= n
#     #     n -= 1
# print(factor(7))

def factor_r(num):
    if num == 1:
        return 1
    
    return num * factor_r(num - 1)