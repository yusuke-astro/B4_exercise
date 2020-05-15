import numpy as np  # numpy の読み込み
import matplotlib.pyplot as plt  # Matplotlib の読み込み

h=6.6/1e34
h
c=3*1e8
c
k=1.4/(1e23)


A=2*h*(10**36)/c**2
B=h*10**12/k

x = np.arange(1,1500, 10)

def f(x,n,):
    return (A*x**3)/ (np.exp(B*x/n) - 1.)

y1=f(x,5000)
y2=f(x,6000)
y3=f(x,7000)
y4=f(x,8000)


plt.xlabel('ν(Thz)')
plt.title("Black-Body-Rdiation")
plt.ylabel('I(W sr−1 m−2)', rotation=90)
plt.grid()
plt.plot(x,y1,label="T=5000")
plt.plot(x,y2,label="T=6000")
plt.plot(x,y3,label="T=7000")
plt.plot(x,y4,label="T=8000")
plt.legend()
plt.show()
