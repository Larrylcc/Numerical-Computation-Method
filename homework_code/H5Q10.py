#龙贝格算法 P145 5.42
def f(x):
    return 4/(1+x**2)

def T(f,a,b,T_p,k):
    return 0.5*T_p+(b-a)/(2**k)*sum([f(a+(2*i-1)*(b-a)/(2**k)) for i in range(1,2**(k-1)+1)])

def romberg(f,a,b,tol=1e-5):
    Tn=[]
    Sn=[]
    Cn=[]
    Rn=[]
    Tn.append((b-a)/2*(f(a)+f(b)))
    for i in range(1,10):
        Tn.append(T(f,a,b,Tn[i-1],i))
    for i in range(0,8):
        Sn.append(4/3*Tn[i+1]-1/3*Tn[i])
    for i in range(0,7):
        Cn.append(16/15*Sn[i+1]-1/15*Sn[i])
    for i in range(0,6):
        Rn.append(64/63*Cn[i+1]-1/63*Cn[i])
        print("R",i+1,"=",Rn[i])

    for i in range(0,5):
        if(abs(Rn[i]-Rn[i+1])<=tol):
            print("R",i+2,"满足条件")
            return "%.6f" % Rn[i+1]


print("最终结果为：",romberg(f,0,1,1e-5))