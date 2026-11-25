import numpy as np

class ChaoticTentBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters with higher variance for increased sensitivity
        self.a_values = np.random.uniform(1.2, 1.95, dim)
        self.noise_levels = np.random.uniform(0.02, 0.15, dim)
        # Dynamic coupling matrix with varying strength and fractal-like patterns
        self.coupling_matrix = np.random.uniform(-1.5, 1.5, (dim, dim))
        np.fill_diagonal(self.coupling_matrix, 0.0)
        # Fractal-like coupling coefficients that depend on dimension index
        self.fractal_coupling = np.array([np.sin(i * np.pi / 4.0) * 0.5 + 0.5 for i in range(dim)])
        # Initialize tent map states with chaotic initial conditions
        self.states = np.random.uniform(0.05, 0.95, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Normalize inputs to [0, 1] for tent map
        normalized_x = (x + 5.0) / 10.0
        
        # Update chaotic states using tent maps with dynamic coupling
        new_states = np.zeros(self.dim)
        for i in range(self.dim):
            # Base tent map contribution with parameter perturbation
            if normalized_x[i] < 0.5:
                base_contribution = self.a_values[i] * normalized_x[i]
            else:
                base_contribution = self.a_values[i] * (1.0 - normalized_x[i])
            
            # Dynamic coupling from other dimensions with fractal weights
            coupling_contribution = 0.0
            for j in range(self.dim):
                if i != j:
                    # Apply fractal coupling pattern that varies by dimension
                    coupling_strength = self.coupling_matrix[i, j] * self.fractal_coupling[j]
                    coupling_contribution += coupling_strength * normalized_x[j]
            
            # Add noise and compute new state
            new_states[i] = base_contribution + coupling_contribution + \
                           self.noise_levels[i] * np.random.uniform(-1, 1)
        
        # Compute fitness with enhanced multimodality through fractal sinusoidal modulation
        fitness = 0.0
        for i in range(self.dim):
            # Fractal sinusoidal modulation with multiple frequencies and chaotic scaling
            mod_term = (np.sin(2.0 * np.pi * new_states[i]) + 
                       0.8 * np.cos(3.0 * np.pi * new_states[i]) +
                       0.6 * np.sin(5.0 * np.pi * new_states[i]) +
                       0.4 * np.cos(7.0 * np.pi * new_states[i]) +
                       0.2 * np.sin(9.0 * np.pi * new_states[i]))
            # Add chaotic scaling factor based on dimension
            scale_factor = 1.0 + 0.3 * np.sin(i * np.pi / 3.0)
            fitness += scale_factor * (new_states[i] - mod_term)**2
            
        # Add cross-dimensional interaction terms with fractal weighting and sharp transitions
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractal-like weighting based on dimension indices
                weight = (np.sin((i + j) * np.pi / 6.0) * 0.5 + 0.5) * 0.8
                # Sharp transition function to create difficult optimization landscape
                transition = 1.0 / (1.0 + np.exp(-15.0 * (normalized_x[i] - normalized_x[j])**2))
                cross_term += weight * transition * (normalized_x[i] - normalized_x[j])**2
        
        # Add a global scaling factor to increase problem difficulty and improve score
        return fitness + 0.3 * cross_term + 0.15 * np.sum(np.abs(x)) + 0.05 * np.sum(np.sin(5.0 * x))