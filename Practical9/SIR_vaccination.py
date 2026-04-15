import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm #use colormap for better visualization

N = 10000
beta = 0.3
gamma = 0.05
time_steps = 1000

# vaccine rates from 0% to 100%
vaccine_rates = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
plt.figure(figsize=(6,4), dpi=150)

# apply different vaccine rates
for idx, v in enumerate(vaccine_rates):
    # initial state with vaccination
    V = int(N * v)
    
    # fix 1：ensure S >= 0，prevent the wrong for n < 0 
    S = max(0, N - V - 1) 
    I = 1
    R = 0
    I_list = [I]
    
    for t in range(time_steps):
        # fix 2：ensure S >= 0，prevent the wrong for n < 0
        S = max(0, S)
        if S <= 0 or I <= 0:#if there are no susceptible or infected individuals left, stop the simulation
            I_list.extend([0] * (time_steps - t))
            break
            
        new_infected = np.random.binomial(S, beta * (I / N))
        new_recovered = np.random.binomial(I, gamma)
#Here I just sue the more efficient way to calculate.        
        S = S - new_infected
        I = I + new_infected - new_recovered
        R = R + new_recovered
        I_list.append(I)
    
    # plot the results for each vaccine rate
    plt.plot(I_list, label=f'Vaccine {int(v*100)}%', color=cm.viridis(idx*25))

plt.xlabel('Time steps')
plt.ylabel('Infected people')
plt.title('SIR with Vaccination')
plt.legend(bbox_to_anchor=(1.05,1), loc='upper left')
plt.tight_layout()
plt.savefig('SIR_vaccine.png', dpi=150)
plt.show()