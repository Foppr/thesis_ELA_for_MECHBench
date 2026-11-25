import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic system parameters with modified ranges
        self.omega = np.random.uniform(0.8, 2.5, dim)
        self.alpha = np.random.uniform(0.2, 0.6, dim)
        self.beta = np.random.uniform(0.15, 0.4, dim)
        # Fractal modulation parameters with increased complexity
        self.fractal_dims = np.random.uniform(1.2, 3.0, dim)
        self.modulation_freq = np.random.uniform(1.0, 4.0, dim)
        # Basin boundary adaptation with larger shifts
        self.basin_shifts = np.random.uniform(-1.5, 1.5, dim)
        self.basin_scales = np.random.uniform(0.3, 2.5, dim)
        # Multi-scale interaction matrix with stronger coupling
        self.interaction_matrix = np.zeros((dim, dim))
        for i in range(dim):
            for j in range(dim):
                if i != j:
                    self.interaction_matrix[i, j] = np.random.uniform(-0.5, 0.5) * np.exp(-abs(i-j)/max(1, dim/4))

    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Normalize to [-1, 1]
        normalized_x = x / 5.0
        
        # Compute chaotic gradient components
        chaotic_sum = np.zeros(self.dim)
        for i in range(self.dim):
            # Hyperchaotic dynamics with enhanced fractal modulation
            omega_i = self.omega[i]
            alpha_i = self.alpha[i]
            beta_i = self.beta[i]
            
            # Enhanced fractal modulation with higher frequency components
            fractal_mod = np.sin(self.modulation_freq[i] * normalized_x[i]) ** 3 + \
                          np.cos(self.modulation_freq[i] * normalized_x[i]) ** 3 + \
                          0.5 * np.sin(2 * self.modulation_freq[i] * normalized_x[i]) ** 2
            
            # Chaotic attractor component with modified parameters
            chaotic_term = (
                omega_i * np.sin(alpha_i * normalized_x[i]) * 
                np.exp(-beta_i * np.abs(normalized_x[i])) * fractal_mod
            )
            
            # Add interaction effects with stronger coupling
            interaction_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    interaction_sum += self.interaction_matrix[i, j] * np.tan(1.5 * normalized_x[j])
            
            chaotic_sum[i] = chaotic_term + interaction_sum
        
        # Enhanced multi-scale fractal energy landscape
        fractal_energy = 0.0
        for i in range(self.dim):
            # Adaptive basin boundaries with scaling and shifting
            shifted_x = normalized_x[i] - self.basin_shifts[i]
            scaled_x = shifted_x / self.basin_scales[i]
            
            # Enhanced fractal energy with multi-scale structure
            fractal_component = 0.0
            for d in range(1, int(self.fractal_dims[i]) + 2):
                fractal_component += np.sin(d * scaled_x) / (d ** 1.3)
            
            fractal_energy += fractal_component ** 2
        
        # Combine chaotic and fractal components with nonlinearity
        fitness = np.sum(chaotic_sum ** 2) + 0.7 * fractal_energy
        
        # Add enhanced multi-scale conditioning effects
        condition_factor = np.sum(np.abs(normalized_x) ** (1.8 + np.random.rand() * 2.5)) / self.dim
        fitness += 0.4 * condition_factor
        
        # Add noise for complexity
        noise = np.random.uniform(-0.015, 0.015)
        return fitness + noise