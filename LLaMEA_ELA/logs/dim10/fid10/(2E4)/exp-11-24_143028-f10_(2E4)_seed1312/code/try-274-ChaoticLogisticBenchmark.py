import numpy as np

class ChaoticLogisticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters for each dimension
        self.r_values = np.random.uniform(3.8, 4.0, dim)
        self.noise_levels = np.random.uniform(0.05, 0.2, dim)
        # Dynamic coupling coefficients that vary with dimension index
        self.coupling_matrix = np.zeros((dim, dim))
        for i in range(dim):
            for j in range(dim):
                if i != j:
                    self.coupling_matrix[i, j] = np.random.uniform(-0.8, 0.8) * (1.0 / (1.0 + abs(i - j)))
        # Initialize logistic map states
        self.states = np.random.uniform(0.1, 0.9, dim)
        # Time-delay parameters for each dimension
        self.delay_params = np.random.uniform(0.1, 0.5, dim)
        # Energy landscape modulation parameters
        self.energy_coeffs = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Normalize inputs to [0, 1] for logistic map
        normalized_x = (x + 5.0) / 10.0
        
        # Update chaotic states using delayed logistic maps with dynamic coupling
        new_states = np.zeros(self.dim)
        for i in range(self.dim):
            # Base delayed logistic map contribution
            base_contribution = self.r_values[i] * normalized_x[i] * (1.0 - normalized_x[i])
            
            # Delayed coupling from other dimensions
            delayed_coupling = 0.0
            for j in range(self.dim):
                if i != j:
                    delayed_coupling += self.coupling_matrix[i, j] * np.sin(2.0 * np.pi * normalized_x[j]) * np.exp(-self.delay_params[i])
            
            # Add noise and compute new state
            new_states[i] = base_contribution + delayed_coupling + \
                           self.noise_levels[i] * np.random.uniform(-1, 1)
        
        # Compute fitness with energy landscape modulation
        fitness = 0.0
        for i in range(self.dim):
            # Energy landscape modulation with multiple harmonic terms
            energy_mod = (self.energy_coeffs[i] * np.sin(2.0 * np.pi * new_states[i]) + 
                         0.5 * self.energy_coeffs[i] * np.cos(3.0 * np.pi * new_states[i]) +
                         0.3 * self.energy_coeffs[i] * np.sin(5.0 * np.pi * new_states[i]))
            fitness += (new_states[i] - energy_mod)**2
            
        # Add highly complex cross-dimensional interaction terms with exponential decay
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Exponentially decaying interaction with sinusoidal modulation
                distance_factor = np.exp(-0.2 * (i - j)**2)
                interaction = np.sin(3.0 * np.pi * (normalized_x[i] - normalized_x[j])) * distance_factor
                cross_term += interaction**2
        
        # Add global fitness modulation based on dimensionality
        dim_modulation = 1.0 + 0.5 * np.sin(np.pi * self.dim / 10.0)
        
        return (fitness + 0.2 * cross_term) * dim_modulation