import numpy as np
from matplotlib import pyplot as plt


def f(x):
    return 2/(np.pi*np.sqrt(1 - x**2))


def g(x):
    return 0.5/np.sqrt(1-x)


def inverse_func(x): # Calculate inverse CDF of g(x) 
    return 1-x**2

rng = np.random.default_rng()
k = 4/np.pi
runs = 100000

hist_dat_f=[]
x1 = np.linspace(0,1.,1000)

for i in range(runs):
    r = rng.random()
    y = inverse_func(r)
    u = rng.random()
    
    if u <= f(y)/(k*g(y)):
        
        hist_dat_f.append(y)


plt.figure()
plt.hist(hist_dat_f, bins=18,density=True, label="Histogram of f(x) values using Acceptance-Rejection method")
plt.plot(x1,f(x1), label="f(x)")
plt.legend()



