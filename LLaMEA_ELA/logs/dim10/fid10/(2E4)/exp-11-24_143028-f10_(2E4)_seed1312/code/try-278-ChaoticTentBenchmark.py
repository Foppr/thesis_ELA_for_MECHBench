import numpy as np

class ChaoticTentBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters for each dimension
        self.a_values = np.random.uniform(1.1, 1.9, dim)
        self.noise_levels = np.random.uniform(0.01, 0.1, dim)
        # Coupling coefficients between dimensions
        self.coupling_matrix = np.random.uniform(-0.5, 0.5, (dim, dim))
        np.fill_diagonal(self.coupling_matrix, 0.0)
        # Initialize tent map states
        self.states = np.random.uniform(0.1, 0.9, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Normalize inputs to [0, 1] for tent map
        normalized_x = (x + 5.0) / 10.0
        
        # Update chaotic states using tent maps with coupling
        new_states = np.zeros(self.dim)
        for i in range(self.dim):
            # Base tent map contribution
            if normalized_x[i] < 0.5:
                base_contribution = self.a_values[i] * normalized_x[i]
            else:
                base_contribution = self.a_values[i] * (1.0 - normalized_x[i])
            
            # Coupling from other dimensions
            coupling_contribution = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling_contribution += self.coupling_matrix[i, j] * normalized_x[j]
            
            # Add noise and compute new state
            new_states[i] = base_contribution + coupling_contribution + \
                           self.noise_levels[i] * np.random.uniform(-1, 1)
        
        # Compute fitness as sum of squared chaotic states with periodic modulation
        fitness = 0.0
        for i in range(self.dim):
            # Add periodic modulation to increase multimodality
            mod_term = np.sin(2.0 * np.pi * new_states[i]) + \
                      0.5 * np.cos(3.0 * np.pi * new_states[i])
            fitness += (new_states[i] - mod_term)**2
            
        # Add cross-dimensional interaction terms
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += (normalized_x[i] - normalized_x[j])**2 * \
                             np.exp(-0.1 * (i - j)**2)
        
        return fitness + 0.1 * cross_term