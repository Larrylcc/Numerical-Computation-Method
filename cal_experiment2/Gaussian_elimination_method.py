import numpy as np

def gaussian_elimination(A, b):
    n = len(b)

    Ab = np.column_stack((A.astype(float), b.astype(float)))

    for i in range(n - 1):
        for j in range(i + 1, n):
            proportion = Ab[j, i] / Ab[i, i]
            Ab[j, i:] -= proportion * Ab[i, i:]

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (Ab[i, n] - np.dot(Ab[i, i:n], x[i:n])) / Ab[i, i]

    return x

A = np.array([[14, 2, 1, 5], [8, 17, 2, 10], [4, 18, 3, 6], [12, 26, 11, 20]])
b = np.array([[2], [4], [6], [8]])

x = gaussian_elimination(A, b)
print("高斯消元法：解 x =", x)