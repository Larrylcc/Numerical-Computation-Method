import numpy as np
import matplotlib.pyplot as plt

# 给定数据
x = np.array([1.0000, 1.4000, 1.8000, 2.2000, 2.6000, 3.0000, 3.4000, 3.8000, 4.2000, 4.6000, 5.0000])
y = np.array([4.7187, 9.4496, 13.3248, 16.0722, 17.4894, 17.5794, 16.6755, 15.6332, 16.0858, 20.8430, 34.4605])


# 定义复合函数
def func(x, a, b, c, d, e, f):
    return a + b * x + c * x ** 2 + d * x ** 3 + e * np.exp(x) + f * np.log(x)

def func2(x, a, b, c, d, e, f):
    return a + b * x + c * x ** 2 + d * x ** 3 + e * x ** 4 + f * x ** 5
# 定义最小二乘法拟合函数
def least_squares_fit(x, y):
    n = len(x)

    # 构建设计矩阵
    X = np.column_stack((np.ones_like(x), x, x ** 2, x ** 3, np.exp(x), np.log(x)))
    # 计算最小二乘解
    theta = np.linalg.inv(X.T @ X) @ X.T @ y

    return theta

def multinomial_only(x,y):
    n=len(x)
    X=np.column_stack((np.ones_like(x), x, x ** 2, x ** 3, x ** 4, x ** 5))
    theta=np.linalg.inv(X.T @ X) @ X.T @ y
    return theta

# 调用最小二乘拟合函数
theta = least_squares_fit(x, y)
theta2=multinomial_only(x,y)
print(f"拟合系数:")
print(f"a = {theta[0]:.2f}")
print(f"b = {theta[1]:.2f}")
print(f"c = {theta[2]:.2f}")
print(f"d = {theta[3]:.2f}")
print(f"e = {theta[4]:.2f}")
print(f"f = {theta[5]:.2f}")
print("拟合值与真实值差(最小二乘）：",np.linalg.norm(func(x, *theta)-y))
print(f"仅多项式拟合系数:")
print(f"a = {theta2[0]:.2f}")
print(f"b = {theta2[1]:.2f}")
print(f"c = {theta2[2]:.2f}")
print(f"d = {theta2[3]:.2f}")
print(f"e = {theta2[4]:.2f}")
print(f"f = {theta2[5]:.2f}")
print("拟合值与真实值差(最小二乘）：",np.linalg.norm(func2(x, *theta2)-y))
# 绘制拟合曲线
plt.figure(figsize=(10, 6))
plt.scatter(x, y, label="true value")
plt.plot(x, func(x, *theta), label="fitting value")
plt.plot(x, func2(x, *theta2), label="fitting value multi only")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Figure1")
plt.legend()
plt.show()