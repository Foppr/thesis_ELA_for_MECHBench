import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic system parameters
        self.omega = np.random.uniform(0.5, 2.0, dim)
        self.alpha = np.random.uniform(0.1, 0.5, dim)
        self.beta = np.random.uniform(0.1, 0.3, dim)
        # Fractal modulation parameters
        self.fractal_dims = np.random.uniform(1.1, 2.9, dim)
        self.modulation_freq = np.random.uniform(0.5, 3.0, dim)
        # Basin boundary adaptation
        self.basin_shifts = np.random.uniform(-1.0, 1.0, dim)
        self.basin_scales = np.random.uniform(0.5, 2.0, dim)
        # Multi-scale interaction matrix
        self.interaction_matrix = np.zeros((dim, dim))
        for i in range(dim):
            for j in range(dim):
                if i != j:
                    self.interaction_matrix[i, j] = np.random.uniform(-0.3, 0.3) * np.exp(-abs(i-j)/max(1, dim/3))

    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Normalize to [-1, 1]
        normalized_x = x / 5.0
        
        # Compute chaotic gradient components
        chaotic_sum = np.zeros(self.dim)
        for i in range(self.dim):
            # Hyperchaotic dynamics with fractal modulation
            omega_i = self.omega[i]
            alpha_i = self.alpha[i]
            beta_i = self.beta[i]
            
            # Fractal modulation based on dimension
            fractal_mod = np.sin(self.modulation_freq[i] * normalized_x[i]) ** 2 + \
                          np.cos(self.modulation_freq[i] * normalized_x[i]) ** 2
            
            # Chaotic attractor component with adaptive parameters
            chaotic_term = (
                omega_i * np.sin(alpha_i * normalized_x[i]) * 
                np.exp(-beta_i * np.abs(normalized_x[i])) * fractal_mod
            )
            
            # Add interaction effects
            interaction_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    interaction_sum += self.interaction_matrix[i, j] * np.tan(normalized_x[j])
            
            chaotic_sum[i] = chaotic_term + interaction_sum
        
        # Multi-scale fractal energy landscape
        fractal_energy = 0.0
        for i in range(self.dim):
            # Adaptive basin boundaries with scaling and shifting
            shifted_x = normalized_x[i] - self.basin_shifts[i]
            scaled_x = shifted_x / self.basin_scales[i]
            
            # Fractal energy with multi-scale structure
            fractal_component = 0.0
            for d in range(1, int(self.fractal_dims[i]) + 1):
                fractal_component += np.sin(d * scaled_x) / (d ** 1.5)
            
            fractal_energy += fractal_component ** 2
        
        # Combine chaotic and fractal components with nonlinearity
        fitness = np.sum(chaotic_sum ** 2) + 0.5 * fractal_energy
        
        # Add multi-scale conditioning effects
        condition_factor = np.sum(np.abs(normalized_x) ** (1.5 + np.random.rand() * 2)) / self.dim
        fitness += 0.3 * condition_factor
        
        # Add noise for complexity
        noise = np.random.uniform(-0.01, 0.01)
        return fitness + noise