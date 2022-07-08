import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simpson

runs = 1000000
success = 0
for i in range(runs):
    romeo_eta = np.random.rand() * 60
    juliet_eta = np.random.rand() * 60

    if (romeo_eta < juliet_eta and juliet_eta< romeo_eta + 15) or (juliet_eta<romeo_eta and romeo_eta < juliet_eta + 15):
        success += 1

print("Romeo and Juliet will meet ", 100*success/runs,"% of the time.")

x=np.linspace(0,60,61) #Romeo ETA
y=np.linspace(0,60,61) #Juliet ETA

#Theoretical
plt.figure(0)
plt.plot(x,y,label="They arrive at the same time") #They arrive at the same time
plt.plot(x,y-15,label="Romeo/Juliet arrives 15mins earlier") # Romeo arrives 15mins later
plt.plot(x,y+15,label="Juliet/Romeo arrives 15mins later") #Juliet arrives 15mins later
plt.legend()
plt.grid
plt.xlabel("Romeo/Juliet ETA")
plt.ylabel("Juliet/Romeo ETA")
plt.fill_between(x, y-15, y+15, color='grey', alpha=0.5) #Grey_Area/Max_Area corresponds to the probability of the meeting to happen
plt.show()
plt.axhline(0.0, linestyle = '--', color = 'k')
I1=simpson(y+15,x)
I2=simpson(y[:15]-15,x[:15])
I3=simpson(y[15:]-15,x[15:])

p_theoretical=(I1+I2-I3)/3600
print("Theoretically, Romeo and Juliet will meet ", 100*p_theoretical,"% of the time.")