import numpy as np 
import matplotlib.pyplot as plt 
from scipy.interpolate import InterpolatedUnivariateSpline

pos = np.genfromtxt('posities_1_Team_B7.txt', delimiter = '   ')
t, x = pos[:,0], pos[:,1]
plt.plot(t,x)

f2 = InterpolatedUnivariateSpline(t, x)
#Get dervative
der = []
for i in range(len(x)):

    h = 1e-4
    der.append( ( f2(t[i]+h)-f2(t[i]-h) )/(2*h) )
der = np.array(der)   

plt.plot(t, der)
plt.show()

f2 = InterpolatedUnivariateSpline(t, der)
#Get second dervative
der2 = []
for i in range(len(der)):

    h = 1e-4
    der2.append( ( f2(t[i]+h)-f2(t[i]-h) )/(2*h) )
der2 = np.array(der2)   

plt.plot(t, der2)
plt.show()