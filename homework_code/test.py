import numpy as np
def f(x):
    return 4 / (1 + x**2)

def romberg(a, b, eps, f):
    """
    利用龙贝格算法求解函数 f 在 [a, b] 上的积分

    参数：
        a: 积分下限
        b: 积分上限
        eps: 阶段误差精度
        f: 被积函数

    返回值：
        积分结果
    """

    # 初始化
    T = [[(b - a) * f((a + b) / 2)]]
    h = b - a

    # 迭代求解
    while True:
        # 计算下一阶的梯形公式
        t = 0
        for i in range(1, 2**len(T[-1])):
            t += f(a + i * h / (2**len(T[-1])))
        t *= h / (2**len(T[-1]))
        T.append([0.5 * T[-1][0] + t])

        # 计算阶段误差
        ep = abs(T[-1][0] - T[-2][0])

        # 判断是否达到精度要求
        if ep <= eps:
            break

        # 更新步长
        h /= 2

    return T[-1][0]

# 求解积分
result = romberg(0, 1, 1e-5, f)

# 输出结果
print(f"积分结果为：{result}")
