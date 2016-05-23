#递归算法优化 
#1.递归
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

#2.尾递归优化
def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
#
