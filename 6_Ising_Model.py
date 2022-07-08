import numpy as np
from matplotlib import pyplot as plt

#np.random.seed(4408)
N=100
T_mat=[1,10,20]
max_steps=1000
fig,ax=plt.subplots(3,1,figsize=(10,7))
plt.tight_layout(pad=2)
for t1,T in enumerate(T_mat):
    M=np.zeros(max_steps)
    beta=1/T

    spins=np.random.choice([1,-1],N)


    
    for step in range(max_steps):
        x=np.random.randint(1,N-1)
        initial_spin=spins[x]
        final_spin=-spins[x] #Flip spin
        
        
        
        initial_energy=-initial_spin*spins[x-1]-initial_spin*spins[x+1]
        final_energy=-final_spin*spins[x-1]-final_spin*spins[x+1]
        dE=final_energy - initial_energy
        p=np.exp(-beta*dE)
        
        # if dE<=0:
        #     spins[x]=final_spin
            
        # if dE>0:
        #     r=np.random.rand()
        #     if r<=p:
        #         spins[x]=final_spin
        r=np.random.rand()
        if r<=p:
            spins[x]=final_spin
        M[step]=np.sum(spins)

    
    
    time_steps=np.arange(1,max_steps+1,1)
    ax[t1].plot(time_steps,M/N)
    title1='<M> - time step figure for T = 1 '
    title2='<M> - time step figure for T = 10 '
    title3='<M> - time step figure for T = 20 '
    ax[0].set_title(title1)
    ax[1].set_title(title2)
    ax[2].set_title(title3)
    