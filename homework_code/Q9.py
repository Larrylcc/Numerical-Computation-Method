#逐次分半梯形递推算式 P141 5.37
#只需改f函数与截断误差
import numpy as np
def f(x):
    return 4/(1+x**2)
def trapezoidal(f, a, b, tol=1e-3):
    T2_k=(b-a)/2*(f(a)+f(b))
    k=1
    while(1):
        T2_k_1=0.5*T2_k+(b-a)/(2**k)*sum([f(a+(2*i-1)*(b-a)/(2**k)) for i in range(1,2**(k-1)+1)])
        if(abs(T2_k_1-T2_k)<tol):
            return T2_k_1,k
        T2_k=T2_k_1
        k+=1
print(trapezoidal(f,0,1,1e-3))