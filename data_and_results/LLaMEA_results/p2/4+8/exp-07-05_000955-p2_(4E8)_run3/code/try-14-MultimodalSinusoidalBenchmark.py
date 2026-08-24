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
            freq = 2 ** (i + 1)
            sinusoidal = np.cos(freq * np.pi * x_norm[i]) * np.sin(freq * np.pi * x_norm[i])
            
            # Add radial basin structure
            radial_term = (x_norm[i] ** 2) * np.exp(-0.5 * (x_norm[i] ** 2))
            
            # Combine with quadratic and higher-order terms
            result += (x_norm[i] ** 4 - 2 * x_norm[i] ** 2 + 1) * (1 + 0.3 * sinusoidal) + 0.1 * radial_term
        
        # Add coupling terms between dimensions for increased complexity
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += 0.05 * np.sin(5 * (x_norm[i] + x_norm[j])) * np.cos(3 * (x_norm[i] - x_norm[j]))
        
        # Add global scaling and offset
        result = result * 2.0 + coupling + 0.05 * np.sum(x_norm ** 6)
        
        return result