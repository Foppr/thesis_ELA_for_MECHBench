import numpy as np

class MultimodalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basin terms with varying depths and widths
        radial_sum = 0.0
        for i in range(self.dim):
            # Create radial basins with different characteristics
            radial_term = (x[i] ** 2) * np.exp(-0.1 * (x[i] ** 2))
            radial_sum += radial_term
        
        # Sinusoidal oscillations in multiple dimensions
        sin_sum = 0.0
        for i in range(self.dim):
            sin_sum += np.sin(3 * x[i]) * np.cos(2 * x[i])
        
        # Cross-dimensional interaction terms
        cross_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_sum += 0.5 * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
        
        # Add a global minimum at the origin with additional noise
        result = radial_sum + 0.3 * sin_sum + 0.2 * cross_sum + 0.1 * np.sum(x**4)
        
        # Add small random noise to increase ruggedness
        noise = 0.01 * np.random.rand()
        
        return result + noise