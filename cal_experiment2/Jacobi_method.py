import numpy as np
A = np.array([[14, 2, 1, 5], [8, 17, 2, 10], [4, 18, 3, 6], [12, 26, 11, 20]])
b = np.array([[2], [4], [6], [8]])
D=np.diag(np.diagonal(A))
L=-np.tril(A,-1)
U=-np.triu(A,1)
B=np.linalg.inv(D).dot(L+U)
f=np.linalg.inv(D).dot(b)
x=np.transpose(np.array([[0,0,0,0]]))

for i in range(100):
    x=B.dot(x)+f
    if np.linalg.norm(A.dot(x)-b)<1e-6:
        break
print("雅可比迭代法:分析可得，雅可比法不收敛：解 x =",x)