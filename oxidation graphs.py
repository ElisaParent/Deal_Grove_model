# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:03:46 2024

@author: 14086
"""
def temp_constant(constant,E_A,T):
    return constant*np.exp((-1*E_A)/(K*T))
def deal_grove_model(A,B,t):
    return (-1*A+np.power(A**2+4*B*t,.5))/2
import numpy as np
import matplotlib.pyplot as plt
K=8.617*10**-5
B_A_0=[1.63*10**8,6.23*10**6]
B_0=[386,772]
E_A=[2,.78,1.23]

i=0 
temp=np.linspace(800,1200,9)
B_dry=[]
B_wet=[]
B_A_dry=[]
B_A_wet=[]
for t in temp:
    B_dry.append(temp_constant(B_0[1],E_A[2],t))
    B_wet.append(temp_constant(B_0[0],E_A[1],t))
    B_A_dry.append(temp_constant(B_A_0[1], E_A[0], t))
    B_A_wet.append(temp_constant(B_A_0[0], E_A[0], t))
A_dry=[]
A_wet=[]
i=0
for x in B_dry:
    A_dry.append(B_dry[i]/B_A_dry[i])
    A_wet.append(B_wet[i]/B_A_wet[i])
    i+=1
Ox_dry_0=[]
Ox_dry_1=[]
Ox_dry_2=[]
Ox_dry_3=[]
Ox_dry_4=[]
Ox_dry_5=[]
Ox_dry_6=[]
Ox_dry_7=[]
Ox_dry_8=[]
Ox_wet_0=[]
Ox_wet_1=[]
Ox_wet_2=[]
Ox_wet_3=[]
Ox_wet_4=[]
Ox_wet_5=[]
Ox_wet_6=[]
Ox_wet_7=[]
Ox_wet_8=[]
time=np.linspace(0,150,1000)
for t in time:
    Ox_dry_0.append(deal_grove_model(A_dry[0], B_dry[0], t))
    Ox_dry_1.append(deal_grove_model(A_dry[1], B_dry[1], t))
    Ox_dry_2.append(deal_grove_model(A_dry[2], B_dry[2], t))
    Ox_dry_3.append(deal_grove_model(A_dry[3], B_dry[3], t))
    Ox_dry_4.append(deal_grove_model(A_dry[4], B_dry[4], t))
    Ox_dry_5.append(deal_grove_model(A_dry[5], B_dry[5], t))
    Ox_dry_6.append(deal_grove_model(A_dry[6], B_dry[6], t))
    Ox_dry_7.append(deal_grove_model(A_dry[7], B_dry[7], t))
    Ox_dry_8.append(deal_grove_model(A_dry[8], B_dry[8], t))
    Ox_wet_0.append(deal_grove_model(A_wet[0], B_wet[0], t))
    Ox_wet_1.append(deal_grove_model(A_wet[1], B_wet[1], t))
    Ox_wet_2.append(deal_grove_model(A_wet[2], B_wet[2], t))
    Ox_wet_3.append(deal_grove_model(A_wet[3], B_wet[3], t))
    Ox_wet_4.append(deal_grove_model(A_wet[4], B_wet[4], t))
    Ox_wet_5.append(deal_grove_model(A_wet[5], B_wet[5], t))
    Ox_wet_6.append(deal_grove_model(A_wet[6], B_wet[6], t))
    Ox_wet_7.append(deal_grove_model(A_wet[7], B_wet[7], t))
    Ox_wet_8.append(deal_grove_model(A_wet[8], B_wet[8], t))

fig, axs = plt.subplots(2, 2, layout='constrained')

ax = axs[0][0]
ax.plot(time,Ox_dry_0)
ax.plot(time,Ox_dry_1)
ax.plot(time,Ox_dry_2)
ax.plot(time,Ox_dry_3)
ax.plot(time,Ox_dry_4)
ax.plot(time,Ox_dry_5)
ax.plot(time,Ox_dry_6)
ax.plot(time,Ox_dry_7)
ax.plot(time,Ox_dry_8)
ax.set_title('Dry Oxidation vs Time')
ax.set(xlabel="Time (hr)",ylabel="Thickness (mircons)")


ax = axs[0][1]
ax.plot(time,Ox_wet_0)
ax.plot(time,Ox_wet_1)
ax.plot(time,Ox_wet_2)
ax.plot(time,Ox_wet_3)
ax.plot(time,Ox_wet_4)
ax.plot(time,Ox_wet_5)
ax.plot(time,Ox_wet_6)
ax.plot(time,Ox_wet_7)
ax.plot(time,Ox_wet_8)
ax.set_title('Wet Oxidation vs Time')
ax.set(xlabel="Time (hr)",ylabel="Thickness (mircons)")
Ox_dry_0=[]
Ox_dry_1=[]
Ox_dry_2=[]
Ox_dry_3=[]
Ox_dry_4=[]
Ox_dry_5=[]
Ox_dry_6=[]
Ox_dry_7=[]
Ox_dry_8=[]
Ox_wet_0=[]
Ox_wet_1=[]
Ox_wet_2=[]
Ox_wet_3=[]
Ox_wet_4=[]
Ox_wet_5=[]
Ox_wet_6=[]
Ox_wet_7=[]
Ox_wet_8=[]
time=np.linspace(0,.5,1000)
for t in time:
    Ox_dry_0.append(deal_grove_model(A_dry[0], B_dry[0], t))
    Ox_dry_1.append(deal_grove_model(A_dry[1], B_dry[1], t))
    Ox_dry_2.append(deal_grove_model(A_dry[2], B_dry[2], t))
    Ox_dry_3.append(deal_grove_model(A_dry[3], B_dry[3], t))
    Ox_dry_4.append(deal_grove_model(A_dry[4], B_dry[4], t))
    Ox_dry_5.append(deal_grove_model(A_dry[5], B_dry[5], t))
    Ox_dry_6.append(deal_grove_model(A_dry[6], B_dry[6], t))
    Ox_dry_7.append(deal_grove_model(A_dry[7], B_dry[7], t))
    Ox_dry_8.append(deal_grove_model(A_dry[8], B_dry[8], t))
    Ox_wet_0.append(deal_grove_model(A_wet[0], B_wet[0], t))
    Ox_wet_1.append(deal_grove_model(A_wet[1], B_wet[1], t))
    Ox_wet_2.append(deal_grove_model(A_wet[2], B_wet[2], t))
    Ox_wet_3.append(deal_grove_model(A_wet[3], B_wet[3], t))
    Ox_wet_4.append(deal_grove_model(A_wet[4], B_wet[4], t))
    Ox_wet_5.append(deal_grove_model(A_wet[5], B_wet[5], t))
    Ox_wet_6.append(deal_grove_model(A_wet[6], B_wet[6], t))
    Ox_wet_7.append(deal_grove_model(A_wet[7], B_wet[7], t))
    Ox_wet_8.append(deal_grove_model(A_wet[8], B_wet[8], t))

ax = axs[1][0]
ax.plot(time,Ox_dry_0)
ax.plot(time,Ox_dry_1)
ax.plot(time,Ox_dry_2)
ax.plot(time,Ox_dry_3)
ax.plot(time,Ox_dry_4)
ax.plot(time,Ox_dry_5)
ax.plot(time,Ox_dry_6)
ax.plot(time,Ox_dry_7)
ax.plot(time,Ox_dry_8)
ax.set_title('Dry Oxidation vs Time')
ax.set(xlabel="Time (hr)",ylabel="Thickness (mircons)")


ax = axs[1][1]
ax.plot(time,Ox_wet_0)
ax.plot(time,Ox_wet_1)
ax.plot(time,Ox_wet_2)
ax.plot(time,Ox_wet_3)
ax.plot(time,Ox_wet_4)
ax.plot(time,Ox_wet_5)
ax.plot(time,Ox_wet_6)
ax.plot(time,Ox_wet_7)
ax.plot(time,Ox_wet_8)
ax.set_title('Wet Oxidation vs Time')
ax.set(xlabel="Time (hr)",ylabel="Thickness (mircons)")


plt.show()