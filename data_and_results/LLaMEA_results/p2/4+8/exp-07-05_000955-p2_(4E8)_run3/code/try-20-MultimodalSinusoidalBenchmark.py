import numpy as np

class MultimodalSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
    
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension must match the function dimension")
        
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Create a highly multimodal landscape with exponentially increasing frequencies
        result = 0.0
        for i in range(self.dim):
            # High-frequency sinusoidal components with exponential growth
            freq = 3 ** (i + 1)
            sinusoidal = np.cos(freq * np.pi * x_norm[i]) * np.sin(freq * np.pi * x_norm[i])
            
            # Add radial basin structure with modified exponential decay
            radial_term = (x_norm[i] ** 2) * np.exp(-0.3 * (x_norm[i] ** 2))
            
            # Combine with polynomial and higher-order terms for increased complexity
            result += (x_norm[i] ** 6 - 3 * x_norm[i] ** 4 + 3 * x_norm[i] ** 2 - 1) * (1 + 0.4 * sinusoidal) + 0.15 * radial_term
        
        # Add stronger coupling terms between dimensions for increased complexity
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += 0.1 * np.sin(7 * (x_norm[i] + x_norm[j])) * np.cos(4 * (x_norm[i] - x_norm[j])) * np.exp(-0.1 * (x_norm[i]**2 + x_norm[j]**2))
        
        # Add global scaling and offset with additional polynomial terms
        result = result * 3.0 + coupling + 0.1 * np.sum(x_norm ** 8)
        
        return result