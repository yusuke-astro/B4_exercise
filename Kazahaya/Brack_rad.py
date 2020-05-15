import numpy as np
import matplotlib.pyplot as plt
import doi_func as doi

x=np.arange(0, 1, 0.001)

"""
y1=x**3/(np.exp(x/2.5)-1)
y2=x**3/(np.exp(x/2.725)-1)
y3=x**3/(np.exp(x/2.9)-1)
"""

plt.plot(x, doi.Brack_rad(x,2.5))
plt.plot(x, doi.Brack_rad(x,2.725))
plt.plot(x, doi.Brack_rad(x,2.9))
plt.show()
