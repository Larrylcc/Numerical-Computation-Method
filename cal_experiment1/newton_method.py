import math

def f(x):
    if x <= 0:
        return float('inf')  # 或者任何其他指示不可接受输入的值
    else:
        return math.e**x + 3*(x**3) - 2*(x**2) + math.log(x) - 1

def df(x):
    return math.e**x + 9*(x**2) - 4*x + 1/x

def newton(f, df, x0, tol=1e-4, max_iter=100):
    x_values = []  # 用于存储迭代过程中的 x_new 值
    error_values = []  # 用于存储迭代过程中的误差值

    x = x0
    for i in range(max_iter):
        x_new = x - f(x) / df(x)
        x_values.append(x_new)
        error_values.append(abs(x_new - x))

        print("epoch=", i, "x_new=", x_new, "error=", abs(x_new - x))
        if abs(x_new - x) < tol:
            print('root=', x_new)
            return x_new, x_values, error_values

        x = x_new

    return x, x_values, error_values
