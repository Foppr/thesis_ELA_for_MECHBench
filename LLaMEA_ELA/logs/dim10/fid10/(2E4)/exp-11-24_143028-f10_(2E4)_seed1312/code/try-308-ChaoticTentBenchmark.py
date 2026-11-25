import numpy as np

class ChaoticTentBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters with higher variability and sensitivity
        self.a_values = np.random.uniform(1.5, 1.99, dim)
        self.noise_levels = np.random.uniform(0.05, 0.2, dim)
        # Dynamic coupling matrix with spatially varying strengths
        self.coupling_matrix = np.random.uniform(-2.0, 2.0, (dim, dim))
        np.fill_diagonal(self.coupling_matrix, 0.0)
        # Fractal-like modulation parameters
        self.modulation_freqs = np.random.uniform(2.0, 8.0, dim)
        self.modulation_ampls = np.random.uniform(0.5, 1.5, dim)
        # Initialize tent map states
        self.states = np.random.uniform(0.1, 0.9, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Normalize inputs to [0, 1] for tent map
        normalized_x = (x + 5.0) / 10.0
        
        # Update chaotic states using tent maps with dynamic coupling
        new_states = np.zeros(self.dim)
        for i in range(self.dim):
            # Base tent map contribution with parameter sensitivity
            if normalized_x[i] < 0.5:
                base_contribution = self.a_values[i] * normalized_x[i]
            else:
                base_contribution = self.a_values[i] * (1.0 - normalized_x[i])
            
            # Dynamic coupling from other dimensions with varying strengths
            coupling_contribution = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling_contribution += self.coupling_matrix[i, j] * normalized_x[j]
            
            # Add noise and compute new state with enhanced chaotic behavior
            new_states[i] = base_contribution + coupling_contribution + \
                           self.noise_levels[i] * np.random.uniform(-1, 1)
        
        # Compute fitness with fractal-like periodic modulation and sharp transitions
        fitness = 0.0
        for i in range(self.dim):
            # Enhanced fractal-like modulation using multiple frequencies
            mod_term = (self.modulation_ampls[i] * 
                       (np.sin(self.modulation_freqs[i] * np.pi * new_states[i]) + 
                        0.5 * np.cos(2 * self.modulation_freqs[i] * np.pi * new_states[i]) +
                        0.3 * np.sin(3 * self.modulation_freqs[i] * np.pi * new_states[i])))
            
            # Add sharp transition components to increase difficulty
            sharp_term = 0.1 * np.abs(np.sin(10 * np.pi * new_states[i]))
            
            # Introduce additional non-linearity for better fitness landscape
            nonlinear_term = 0.05 * np.sin(5 * np.pi * new_states[i])**2
            
            fitness += (new_states[i] - mod_term + sharp_term + nonlinear_term)**2
            
        # Add cross-dimensional interaction with fractal-like weighting
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractal-like distance weighting
                dist_weight = np.exp(-0.5 * (i - j)**2 / (0.5 * self.dim))
                cross_term += (normalized_x[i] - normalized_x[j])**2 * dist_weight
        
        # Add global scaling factor to increase landscape complexity
        return fitness + 0.3 * cross_term + 0.05 * np.sum(np.abs(x)) + 0.1 * np.sum(np.sin(x))