import numpy as np

def gauss_seidel_iteration(A, b, tol=1e-6, max_iter=100):
        n = len(b)
        x = np.zeros(n)
        x_new = np.zeros(n)

        for iter in range(max_iter):
            for i in range(n):
                sum = np.dot(A[i], x_new) - A[i][i] * x[i]
                x_new[i] = (b[i] - sum) / A[i][i]

            if np.linalg.norm(x_new - x) < tol:
                break

            x = np.copy(x_new)
        return x

A = np.array([[14, 2, 1, 5], [8, 17, 2, 10], [4, 18, 3, 6], [12, 26, 11, 20]])
b = np.array([[2], [4], [6], [8]])
x = gauss_seidel_iteration(A, b)
print("高斯-赛德尔迭代法：解：", x)