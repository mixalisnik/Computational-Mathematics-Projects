#Monty Hall Problem
import numpy as np
#Strategy 1: Initial unchanged choice
wins=0
for n in range(10000):
    
    choices=[0,1,2]
    gift,choice=np.random.choice(choices,2)
    
    if gift==choice:
        
        wins=wins+1
        
probability1=wins/10000
#Strategy 2: Always change initial choice
wins=0
for n in range(10000):
    choices=[0,1,2]

    gift,choice=np.random.choice(choices,2)


    #strategy implementation
    #1 always change
    if gift!=choice:
        wins=wins+1
probability2=wins/10000

#Strategy 3: Change 50% of the time
wins=0
for n in range(10000):
    choices=[0,1,2]
    choice=0
    gift=np.random.choice(choices)
    r=np.random.rand()
    if r>0.5: #change
        if gift!=choice:
            wins=wins+1
    else:
        if gift==choice:
            wins=wins+1
            
probability3=wins/10000


print("Strategy 1: Never changing leads to ",np.round(probability1*100,4),"% chance of winning.")
print("Strategy 2: Always changing leads to ",np.round(probability2*100,4),"% chance of winning.")
print("Strategy 3: Change 50% of the time leads to ",np.round(probability3*100,4),"% chance of winning.")
