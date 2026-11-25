import numpy as np

class ChaoticLogisticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters
        self.r_values = np.random.uniform(3.5, 4.0, dim)
        self.delay = 2
        self.feedback_strength = 0.1
        
    def f(self, x):
        # Normalize input to [0, 1] range
        x_norm = (x + 5.0) / 10.0
        
        # Initialize chaotic system
        state = x_norm.copy()
        fitness = 0.0
        
        # Iterate through logistic maps with time-delayed feedback
        for t in range(100):  # Burn-in period
            next_state = np.zeros(self.dim)
            for i in range(self.dim):
                # Logistic map with delayed feedback
                delayed_idx = (i - self.delay) % self.dim
                feedback = self.feedback_strength * state[delayed_idx]
                next_state[i] = self.r_values[i] * state[i] * (1 - state[i]) + feedback
                
                # Add parameter modulation based on position
                modulation = np.sin(0.5 * np.pi * x_norm[i])
                next_state[i] *= (1 + 0.1 * modulation)
                
            state = next_state
            
        # Compute fitness from final chaotic states
        for i in range(self.dim):
            # Add quadratic basin terms with chaotic modulation
            basin_term = (state[i] - 0.5)**2
            chaotic_mod = np.sin(10 * state[i]) + np.cos(7 * state[i])
            fitness += basin_term * (1 + 0.3 * chaotic_mod)
            
        # Add cross-dimensional coupling terms
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += np.sin(2 * np.pi * (state[i] - state[j])) * \
                           np.exp(-0.1 * (i - j)**2)
                
        # Add dimensionality scaling and noise
        dim_scaling = 0.01 * self.dim
        noise = 0.001 * np.random.rand()
        
        return fitness + coupling * 0.1 + dim_scaling + noise