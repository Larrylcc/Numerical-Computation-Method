import math


def f(x):
    if x <= 0:
        return float('inf')  # 或者任何其他指示不可接受输入的值
    else:
        return math.e ** x + 3 * (x ** 3) - 2 * (x ** 2) + math.log(x) - 1


def g(x0, x1):
    return (f(x1) - f(x0)) / (x1 - x0)


def chord(f, g, x0, x1, tol=1e-4, max_iter=100):
    x_values = []  # 用于存储迭代过程中的 x_new 值
    error_values = []  # 用于存储迭代过程中的误差值

    for i in range(max_iter):
        x2 = x1 - f(x1) / g(x0, x1)
        x_values.append(x2)
        error_values.append(abs(x2 - x1))
        print("epoch=",i,"x_new=",x2,"error=",abs(x2-x1))
        if abs(x2 - x1) < tol:
            print('root=',x2)
            return x2, x_values, error_values

        x0 = x1
        x1 = x2

    return x1, x_values, error_values


if __name__ == "__main__":
    root, x_values, error_values = chord(f, g, 0.1, 0.9, tol=1e-4, max_iter=100)
    print("Root found:", root)
