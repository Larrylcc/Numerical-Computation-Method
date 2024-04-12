import math
def f(x):
    if x <= 0:
        return float('inf')  # 或者任何其他指示不可接受输入的值
    else:
        return math.e ** x + 3 * (x ** 3) - 2 * (x ** 2) + math.log(x) - 1

def dichotomy(f, a, b, tol=1e-4, max_iter=100):
    x_values = []  # 用于存储迭代过程中的 x_new 值
    error_values = []  # 用于存储迭代过程中的误差值

    for i in range(max_iter):
        x = (a + b) / 2
        x_values.append(x)
        error_values.append(abs(b - a))
        print("epoch=",i,"x_new=",x,"error=",abs(b-a))
        if abs(b - a) < tol:
            print('root=',x)
            return x, x_values, error_values

        if f(b) * f(x) < 0:
            a = x
        else:
            b = x

    return x, x_values, error_values

#dichotomy(f, 0, 1, tol=1e-4, max_iter=100)