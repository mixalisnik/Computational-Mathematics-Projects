import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats


def getRandomExpNum(lamda):
    r = np.random.uniform(0,1)
    
    y = - np.log(1 - r) / lamda #Inverse cdf function of exponential pdf.
    return y


runs = 10000
lamda=1
hist_dat = [] 
for i in range(runs):
    exp_rn = getRandomExpNum(lamda)
    hist_dat.append(exp_rn)

# Histogram

plt.figure()
plt.hist(hist_dat, bins=20,density=True)
plt.title("Histogram of probability")
plt.xlabel('Number')
plt.ylabel('Probability')
plt.show()

# QQ plot
plt.figure()
qqplot=stats.probplot(hist_dat, dist="expon",plot=plt)
plt.show()