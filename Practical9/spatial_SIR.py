import numpy as np
import matplotlib.pyplot as plt

# Model Parameters 
GRID_SIZE = 100        # 100 × 100 grid
INFECT_PROB = 0.3      # β: infection probability to neighbors
RECOVER_PROB = 0.05    # γ: recovery probability per step
TOTAL_STEPS = 100      # Simulate 100 time steps

# Initialize Grid 
# All start as Susceptible (0)
population = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)

# Random initial infected point (single outbreak)
init_x, init_y = np.random.choice(GRID_SIZE, 2)
population[init_x, init_y] = 1

# Simulation & Plotting 
# Plot settings
plt.figure(figsize=(6, 4), dpi=150)

# Time loop
for step in range(TOTAL_STEPS + 1):
    # Make a copy to avoid simultaneous update errors
    current = population.copy()
    infected_pos = np.argwhere(current == 1)

    # Process each infected cell
    for (i, j) in infected_pos:
        # 1. Recovery process
        if np.random.rand() < RECOVER_PROB:
            population[i, j] = 2

        # 2. Spread to 8 neighboring cells (Moore neighborhood)
        for di in (-1, 0, 1):
            for dj in (-1, 0, 1):
                if di == 0 and dj == 0:
                    continue  # skip self
                ni = i + di
                nj = j + dj
                # Check grid boundary
                if 0 <= ni < GRID_SIZE and 0 <= nj < GRID_SIZE:
                    # Only infect susceptible cells
                    if current[ni, nj] == 0 and np.random.rand() < INFECT_PROB:
                        population[ni, nj] = 1

    # Plot ONLY at steps: 0,10,20,...,100
    if step % 10 == 0:
        plt.clf()
        img = plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.title(f'Spatial SIR Model - Time {step}')
        cbar = plt.colorbar(img)
        cbar.set_label('State: 0=Susceptible, 1=Infected, 2=Recovered')
        plt.pause(0.4)  # Show plot briefly

# Keep final plot open
plt.show()