import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Create exponentially increasing complexity with chaotic oscillations
        for i in range(self.dim):
            # Exponential scaling of coefficients
            scale = 2.0 ** (i / self.dim)
            
            # Quadratic term with sinusoidal modulation
            quad_term = scale * (x[i]**2 - 2 * x[i] * np.sin(x[i]))
            
            # Chaotic oscillatory component
            chaotic_term = scale * np.sin(5 * x[i] + i) * np.cos(3 * x[i] * np.exp(-i/10))
            
            # Add to result
            result += quad_term + chaotic_term
            
        # Add multiple global minima with varying distances from origin
        # Using a sum of inverse distance terms to create flat regions
        for i in range(self.dim):
            if x[i] != 0:
                result += 0.1 * np.sin(10 * x[i]) / (abs(x[i]) + 0.1)
        
        # Add a highly complex sinusoidal modulation that depends on all dimensions
        # This creates an extremely rugged landscape with many local minima
        sum_x = np.sum(x)
        result += 2.0 * np.sin(10 * sum_x) * np.cos(5 * sum_x) * np.exp(-0.1 * sum_x**2)
        
        # Add a penalty term that increases sharply near boundaries
        boundary_penalty = 0.01 * np.sum((np.abs(x) - 5.0)**4)
        result += boundary_penalty
        
        # Add a small random component to make the landscape non-reproducible
        np.random.seed(int(sum_x * 1000) % 1000000)
        result += 0.001 * np.random.rand()
        
        return result