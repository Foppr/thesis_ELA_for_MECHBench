import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Base quadratic term with conditioning
        for i in range(self.dim):
            result += 0.1 * x[i]**2
        
        # Exponentially increasing sinusoidal components
        for i in range(self.dim):
            freq = 2**(i % 3 + 1)  # Varying frequencies: 2, 4, 8
            result += 0.8 * np.sin(freq * np.pi * x[i]) * np.cos(freq * np.pi * x[i])
            result += 0.4 * np.sin(2 * freq * np.pi * x[i])**3
        
        # Polynomial penalty terms with higher order terms for ruggedness
        for i in range(self.dim):
            result += 0.02 * x[i]**4 + 0.01 * x[i]**5 + 0.005 * x[i]**7
        
        # Cross-dimensional coupling with chaotic interaction terms
        for i in range(self.dim - 1):
            result += 0.05 * np.sin(x[i] * x[i+1]) * np.cos(2 * x[i] + x[i+1])
            result += 0.03 * (x[i]**2 + x[i+1]**2) * np.sin(0.7 * (x[i] - x[i+1])**2)
            result += 0.02 * np.exp(-abs(x[i] - x[i+1])) * np.cos(x[i] * x[i+1])
        
        # Add exponential scaling factor to create extreme landscape variations
        result *= (1.0 + 0.2 * np.sum(np.exp(0.5 * np.abs(x))))
        
        # Add a global minimum at the origin and ensure it's attractive
        result += 0.001 * np.sum(x**2)
        
        return result