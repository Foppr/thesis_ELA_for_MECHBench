import numpy as np

class SinusoidalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
    
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension mismatch")
        
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Create highly chaotic sinusoidal grid pattern
        result = 0.0
        for i in range(self.dim):
            # Add chaotic sinusoidal components with varying frequencies
            result += np.sin(5 * np.pi * x_norm[i]) * np.cos(7 * np.pi * x_norm[i]) * np.sin(3 * np.pi * x_norm[i])
            # Add polynomial conditioning with high order terms
            result += 0.2 * x_norm[i]**4 + 0.15 * x_norm[i]**6
            # Add complex interaction terms between dimensions
            for j in range(i+1, min(i+4, self.dim)):  # Limited interaction for complexity
                # Add chaotic interaction pattern
                result += 0.1 * np.sin(4 * np.pi * (x_norm[i]**2 + x_norm[j]**2)) * \
                         np.cos(6 * np.pi * (x_norm[i] * x_norm[j])) * \
                         np.sin(2 * np.pi * (x_norm[i] - x_norm[j])**3)
            # Add nested global minima structure
            result += 0.05 * np.sin(10 * np.pi * x_norm[i]) * np.cos(8 * np.pi * x_norm[i])
        
        # Add strong conditioning and global minimum at origin
        result += 0.3 * np.sum(x_norm**2) + 0.05 * np.sum(x_norm**8)
        
        # Add a complex landscape with multiple local minima
        for i in range(self.dim):
            result += 0.1 * np.sin(15 * np.pi * x_norm[i]) * np.cos(12 * np.pi * x_norm[i])
        
        return result