# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# set up the parameters for the SIR model
N = 10000          # Total population
beta = 0.3         # Infection rate
gamma = 0.05       # Recovery rate
time_steps = 1000  # Number of simulation time steps

# Initial state
S = N - 1  # Susceptible: Total population - 1 initial infected person
I = 1      # Infected: Initial 1 person
R = 0      # Recovered: Initial 0 people

# Lists to store the number of susceptible, infected, and recovered individuals over time
S_list = [S]
I_list = [I]
R_list = [R]
#I neeed to calculate the number of new infections and recoveries at each time step
#update the counts of S, I, and R accordingly. 
#Time loop
for t in range(time_steps):
    # Calculate new infections
    infection_prob = beta * (I / N)  # Probability of infection based on current infected proportion
    infection_results=np.random.choice([0,1], size=S, p=[1-infection_prob, infection_prob]) # Simulate infections for all susceptible individuals
    new_infected = np.sum(infection_results) # Count how many new infections occurred
    
    # Calculate new recoveries
    recovery_prob = gamma  # Probability of recovery
    recovery_results=np.random.choice([0,1], size=I, p=[1-recovery_prob, recovery_prob]) # Simulate recoveries for all infected individuals
    new_recovered = np.sum(recovery_results) # Count how many new recoveries occurred

#Another better way to calculate new infections and recoveries is to use the binomial distribution, which is more efficient and appropriate for this type of problem.
   #The number of new infections can be modeled as a binomial random variable based on the number of susceptible individuals and the probability of infection, 
   #while the number of new recoveries can be modeled as a binomial random variable based on the number of infected individuals and the probability of recovery.
   #new_infected = np.random.binomial(S, beta * (I / N)) 
   #new_recovered = np.random.binomial(I, gamma)
   
   
    # Update the counts of each group
    S = S - new_infected
    I = I + new_infected - new_recovered
    R = R + new_recovered
    
    # record the counts for plotting
    S_list.append(S)
    I_list.append(I)
    R_list.append(R)

# Plotting the results
plt.figure(figsize=(6,4), dpi=150)
plt.plot(S_list, label='Susceptible')
plt.plot(I_list, label='Infected')
plt.plot(R_list, label='Recovered')
plt.xlabel('Time steps')
plt.ylabel('Number of people')
plt.title('Stochastic SIR Model')
plt.legend()
plt.savefig('SIR.png', dpi=150)
plt.show()