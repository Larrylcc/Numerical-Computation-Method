#龙贝格算法 P145 5.42
#先计算k=0,1,2，从k=3开始循环，四个值只需记录T3_
import numpy as np

def f(x):
    return 4/(1+x**2)
def T0_0(f,a,b):
    return (b-a)/2*(f(a)+f(b))
def T0_l(f,a,b,T0_l_m1,l):
    return 0.5*T0_l_m1+(b-a)/2**l*sum([f(a+(2*i-1)*(b-a)/2**l) for i in range(1,2**(l-1)+1)])
def Tm_k(T_m_m1_k_p1,T_m_m1_k,m,k):
    return (4**m*T_m_m1_k_p1-T_m_m1_k)/(4**m-1)
def romberg(f,a,b,tol=1e-5):
    T0_0_val=T0_0(f,a,b)
    T0_1=T0_l(f,a,b,T0_0_val,1)
    T1_0=Tm_k(T0_1,T0_0_val,1,0)
    m=1
    while abs(T1_1 - T0_1) >= tol:
        T0_1=T0_l(f,a,b,T0_1,m+1)
        T1_1=T0_1
        for k in range(1,m+1):
            T1_1=Tm_k(T0_1,T1_1,m,k)
        m+=1

print(romberg(f,0,1,1e-5))