import numpy as np

class ExponentialSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.exp_base = 2.71828
        self.fractal_dim = 0.3
        self.saddle_density = 0.4
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential potential component with dimension-dependent base
        exp_sum = 0
        for i in range(self.dim):
            exp_val = self.exp_base ** (0.1 * x[i]**2) + 0.5 * np.sin(0.5 * x[i])
            exp_sum += exp_val
            
        # Sinusoidal cross-term interactions with fractal scaling
        cross_sum = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractal-like interaction with dimension-dependent scaling
                scale_factor = (i + j) ** self.fractal_dim
                cross_val = np.sin(scale_factor * x[i] * x[j]) * np.cos(0.3 * (x[i]**2 + x[j]**2))
                cross_sum += cross_val ** 2
                
        # Saddle-point distribution with adaptive density
        saddle_sum = 0
        for i in range(self.dim):
            if np.random.random() < self.saddle_density:
                saddle_sum += (x[i] ** 4 - 6 * x[i]**2 + 9) * (1 + 0.1 * np.cos(3 * x[i]))
                
        # Fractal-like self-similar structure with multiple scales
        fractal_sum = 0
        for i in range(self.dim):
            # Multi-scale sinusoidal modulation
            scale1 = 1.0 + 0.5 * np.sin(i)
            scale2 = 1.0 + 0.3 * np.cos(i * 0.7)
            fractal_sum += (np.sin(scale1 * x[i]) * np.cos(scale2 * x[i])) ** 2
            
        # Adaptive scaling based on dimensionality
        dim_factor = 1.0 + 0.3 * np.log(self.dim + 1)
        
        # Add a small constant to avoid flat regions
        return dim_factor * (exp_sum + cross_sum + saddle_sum + fractal_sum) + 0.05 * self.dim