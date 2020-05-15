import numpy as np
from scipy.optimize import curve_fit

def theory_curve( n, d, freq_in, angle_in, incpol):
    const = np.sqrt((8.85e-12)/(4.*np.pi*1e-7))
    c=299792458
    angle_in2=angle_in*np.pi/180.
    n=[1., n, 1.]
    angle=[angle_in2, np.arcsin(np.sin(angle_in2)/n[1]), angle_in2]

    Y=np.zeros(3, 'complex')

    for i in range(3):
        if (incpol==1):
            Y[i] = const*n[i]*np.cos(angle[i])
        if (incpol== -1):
            Y[i] = const*n[i]/np.cos(angle[i])

    k = 2*np.pi*freq_in/c
    h = n[1]*d*np.cos(angle[1])

    me = np.zeros((2,2),'complex')
    me[0,0] = complex(np.cos(k*h), 0.)
    me[1,0] = complex(0., np.sin(k*h)*Y[1])
    me[0,1] = complex(0., np.sin(k*h)/Y[1])
    me[1,1] = complex(np.cos(k*h), 0.)

    t=2*Y[0]/(Y[0]*me[0,0]+Y[0]*Y[2]*me[0,1]+me[1,0]+Y[2]*me[1,1])
    a=abs(t)**2
    return a

def fit_2(freq_in, n):
    global d
    global angle_in
    global incpol

    const = np.sqrt((8.85e-12)/(4.*np.pi*1e-7))
    c=299792458
    angle_in2=angle_in*np.pi/180.
    n=[1., n, 1.]
    angle=[angle_in2, np.arcsin(np.sin(angle_in2)/n[1]), angle_in2]

    Y=np.zeros(3, 'complex')

    for i in range(3):
        if (incpol == 1):
            Y[i] = const*n[i]*np.cos(angle[i])
        if (incpol == -1):
            Y[i] = const*n[i]/np.cos(angle[i])

    k = 2*np.pi*freq_in/c
    h = n[1]*d*np.cos(angle[1])
    me = [[0] * 2 for i in range(2)]
    #me = np.zeros((2,2),'complex')
    me[0][0] = np.cos(k*h)
    me[1][0] = np.sin(k*h)*Y[1]*1j
    me[0][1] = np.sin(k*h)/Y[1]*1j
    me[1][1] = np.cos(k*h)

    t = 2*Y[0]/(Y[0]*me[0][0]+Y[0]*Y[2]*me[0][1]+me[1][0]+Y[2]*me[1][1])
    T = abs(t)**2
    return T

def fit_nd(freq_in, n, d):
    global angle_in
    global incpol

    const = np.sqrt((8.85e-12)/(4.*np.pi*1e-7))
    c=299792458
    angle_in2=angle_in*np.pi/180.
    n=[1., n, 1.]
    angle=[angle_in2, np.arcsin(np.sin(angle_in2)/n[1]), angle_in2]

    Y=np.zeros(3, 'complex')

    for i in range(3):
        if (incpol == 1):
            Y[i] = const*n[i]*np.cos(angle[i])
        if (incpol == -1):
            Y[i] = const*n[i]/np.cos(angle[i])

    k = 2*np.pi*freq_in/c
    h = n[1]*d*np.cos(angle[1])
    me = [[0] * 2 for i in range(2)]
    #me = np.zeros((2,2),'complex')
    me[0][0] = np.cos(k*h)
    me[1][0] = np.sin(k*h)*Y[1]*1j
    me[0][1] = np.sin(k*h)/Y[1]*1j
    me[1][1] = np.cos(k*h)

    t = 2*Y[0]/(Y[0]*me[0][0]+Y[0]*Y[2]*me[0][1]+me[1][0]+Y[2]*me[1][1])
    T = abs(t)**2
    return T


def fit_d(freq_in, d):
    global n
    n = 3.
    angle_in = 5.
    global incpol
    incpol =-1

    const = np.sqrt((8.85e-12)/(4.*np.pi*1e-7))
    c=299792458
    angle_in2=angle_in*np.pi/180.
    n=[1., n, 1.]
    angle=[angle_in2, np.arcsin(np.sin(angle_in2)/n[1]), angle_in2]

    Y=np.zeros(3, 'complex')

    for i in range(3):
        if (incpol == 1):
            Y[i] = const*n[i]*np.cos(angle[i])
        if (incpol == -1):
            Y[i] = const*n[i]/np.cos(angle[i])

    k = 2*np.pi*freq_in/c
    h = n[1]*d*np.cos(angle[1])
    me = [[0] * 2 for i in range(2)]
    me[0][0] = np.cos(k*h)
    me[1][0] = np.sin(k*h)*Y[1]*1j
    me[0][1] = np.sin(k*h)/Y[1]*1j
    me[1][1] = np.cos(k*h)

    t = 2*Y[0]/(Y[0]*me[0][0]+Y[0]*Y[2]*me[0][1]+me[1][0]+Y[2]*me[1][1])
    T = abs(t)**2
    return T
