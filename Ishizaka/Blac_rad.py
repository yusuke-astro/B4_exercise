import matplotlib.pyplot as plt
import  numpy as np

x = np.arange(0, 10, 0.01)


def f(x,n):

    return x**3/(np.exp(n*x)-1)

y1=f(x,1)
y2=f(x,0.9)
y3=f(x,0.8)

plt.xlabel('ν[Hz]')
plt.title("Black-Body-Rdiation")
plt.ylabel('I[W sr−1 m−2]')

plt.grid()
plt.plot(x,y1,label="T=1")
plt.plot(x,y2,label="T=0.9")
plt.plot(x,y3,label="T=0.8")
plt.legend()
