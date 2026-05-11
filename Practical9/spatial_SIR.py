import numpy as np
import matplotlib.pyplot as plt

# paremeters
size = 100
beta = 0.3
gamma = 0.05
time_steps = 100

# initialize population: 0 for susceptible, 1 for infected, 2 for recovered
pop = np.zeros((size, size), dtype=int)

# choose a random point to start the outbreak
outbreak = np.random.choice(size, 2)
x0, y0 = outbreak[0], outbreak[1]
pop[x0, y0] = 1

# initial plot
plt.figure(figsize=(6,4), dpi=150)
plt.imshow(pop, cmap='viridis', interpolation='nearest')
plt.title('Time 0')
plt.show()

# time circulation
for step in range(time_steps):
    # copy the current state to avoid simultaneous updates
    current = pop.copy()
    # find all infected points
    infected = np.argwhere(current == 1)
    
    for (i,j) in infected:
        # recovery process
        if np.random.rand() < gamma:
            pop[i,j] = 2
        
        # infection of 8 neighbors
        for di in [-1,0,1]:
            for dj in [-1,0,1]:
                if di ==0 and dj ==0:
                    continue
                ni = i + di
                nj = j + dj
                if 0<=ni<size and 0<=nj<size:
                    if current[ni, nj] == 0 and np.random.rand() < beta:
                        pop[ni, nj] = 1
    
    # plot every 10 steps
    if step %10 ==0:
        plt.imshow(pop, cmap='viridis', interpolation='nearest')
        plt.title(f'Time {step}')
        plt.show()