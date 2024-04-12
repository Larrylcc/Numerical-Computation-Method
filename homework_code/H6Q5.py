#Ordinary differential equation(ODE)
#Euler method, improved euler method and classical RK method
import numpy as np
def ori(x):
    return 1-np.exp(x)**(-1)

def f(x,y):
    return 1-y

def euler(h,Xi,Yi,f):
    return Yi+h*f(Xi,Yi)

def improved_euler(h,Xi,Xi_1,Yi,f):
    return Yi+h/2*(f(Xi,Yi)+f(Xi_1,Yi+h*f(Xi,Yi)))

def RK(h,Xi,Yi,f):
    K1=f(Xi,Yi)
    K2=f(Xi+h/2,Yi+h/2*K1)
    K3=f(Xi+h/2,Yi+h/2*K2)
    K4=f(Xi+h,Yi+h*K3)
    return Yi+h/6*(K1+2*K2+2*K3+K4)

En=[]
En.append(0)
print("欧拉法：")
for i in range (1,13):
    Xi=0
    h1=0.025
    En.append(euler(h1,Xi,En[i-1],f))
    Xi+=h1;
    if(i%4==0):
        print("En[",i,"]=",En[i])

In=[]
In.append(0)
Xi_1 = 0
print("改进欧拉法：")
for i in range(1,7):
    h2=0.05
    Xi=0.05
    In.append(improved_euler(h2,Xi,Xi_1,In[i-1],f))
    Xi+=h2
    Xi_1+=h2
    if(i%2==0):
        print("In[",i,"]=",In[i])

Rn=[]
Rn.append(0)
Xi=0
print("经典R-K法：")
for i in range(1,4):
    h3=0.1
    Rn.append(RK(h3,Xi,Rn[i-1],f))
    Xi+=h3;
    print("R[",i,"]=",Rn[i])

x=0.1
print("准确解：")
for i in range(1,4):
    print("y(0.",i,")=",ori(x))
    x+=0.1