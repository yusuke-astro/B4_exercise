import numpy as np  # numpy の読み込み
import matplotlib.pyplot as plt  # Matplotlib の読み込み

def Brack_rad(x,n):
    h=6.6/1e34
    c=3*1e8
    k=1.4/(1e23)
    A=2*h*(10**36)/c**2
    B=h*10**12/k

    return (A*x**3)/ (np.exp(B*x/n) - 1.)
