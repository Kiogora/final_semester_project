# -*- coding: utf-8 -*-
"""
Author: Alois Mbutura
GBW vs input capacitance plot 
"""
import numpy as np
import matplotlib.pyplot as plt

#linear space(start(6pF),end(50pF),numpoints)
Cin=np.linspace(6e-9,50e-9,10000)

#Actual calculation
GBW=(Cin+0.1e-9)/(2*np.pi*7.75e3*np.square(0.1e-9))

#Now the plotting begins. Call Matplotlib
plt.plot(Cin,GBW)
plt.grid("on")
plt.show()