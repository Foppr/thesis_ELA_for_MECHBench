import numpy as np

class ExponentialSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.scale_factor = 1.0
        self.modulation_freq = 2.0 * np.pi
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = np.clip(x / 5.0, -1, 1)
        
        # Initialize fitness value
        fitness = 0.0
        
        # Add exponential decay components with sinusoidal modulation
        for i in range(self.dim):
            # Exponential decay term with dimension-specific scaling
            exp_term = np.exp(-self.scale_factor * (x_norm[i]**2))
            
            # Sinusoidal modulation based on multiple frequencies
            sin_mod = np.sin(self.modulation_freq * x_norm[i]) + \
                     0.5 * np.sin(3 * self.modulation_freq * x_norm[i]) + \
                     0.3 * np.sin(7 * self.modulation_freq * x_norm[i])
            
            # Combine exponential decay with sinusoidal modulation
            fitness += exp_term * (1 + 0.5 * sin_mod)
        
        # Add gradient-based attraction fields between dimensions
        for i in range(self.dim - 1):
            # Quadratic attraction potential between adjacent dimensions
            attr_term = (x_norm[i] - x_norm[i+1])**2
            
            # Add coupling strength that increases with dimension index
            coupling_strength = 0.1 * (i + 1) / self.dim
            
            fitness += coupling_strength * attr_term
        
        # Add multi-modal structure through higher-order polynomial terms
        poly_term = np.sum(x_norm**4) + 0.5 * np.sum(x_norm**6)
        
        # Add small random noise for ruggedness
        noise = 0.001 * np.random.rand()
        
        return fitness + poly_term + noise