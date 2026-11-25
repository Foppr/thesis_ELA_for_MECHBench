import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize parameters for exponential decay and trigonometric coupling
        self.exp_rates = [0.5 + 0.3 * np.sin(0.4 * i + 1.0) for i in range(dim)]
        self.coupling_coeffs = [0.8 + 0.2 * np.cos(0.6 * i + 0.5) for i in range(dim)]
        self.noise_levels = [0.05 + 0.02 * np.sin(0.3 * i + 0.2) for i in range(dim)]
        self.depth_factors = [1.0 + 0.5 * np.cos(0.7 * i + 0.3) for i in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Add exponential decay components with dimension-specific rates
        for i in range(self.dim):
            xi = x[i]
            rate = self.exp_rates[i]
            # Exponential decay modulated by trigonometric functions
            result += np.exp(-rate * np.abs(xi)) * np.sin(xi)
            
        # Add trigonometric coupling between dimensions
        for i in range(self.dim):
            xi = x[i]
            coeff = self.coupling_coeffs[i]
            # Coupled terms with sinusoidal modulation
            for j in range(i+1, self.dim):
                xj = x[j]
                result += coeff * np.sin(xi + xj) * np.cos(xi - xj)
                
        # Add adaptive noise to create local variations
        for i in range(self.dim):
            xi = x[i]
            noise_level = self.noise_levels[i]
            # Random noise scaled by dimension-specific factor
            result += noise_level * np.random.normal(0, 1) * np.exp(-0.1 * xi**2)
            
        # Add depth variation for local minima
        for i in range(self.dim):
            xi = x[i]
            depth_factor = self.depth_factors[i]
            # Depth modulation with polynomial terms
            result += depth_factor * (xi**4 - 2*xi**2)
            
        # Add global scaling to control landscape complexity
        global_scale = 1.0 + 0.2 * np.sin(0.5 * self.dim + 0.2)
        result = result * global_scale
        
        return result