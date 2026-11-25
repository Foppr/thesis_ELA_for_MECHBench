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
        
        # Exponentially modulated chaotic sinusoidal components
        for i in range(self.dim):
            freq = 2**(i % 3 + 1)
            result += 0.8 * np.sin(freq * np.pi * x[i]) * np.exp(-0.1 * np.abs(x[i]))
            result += 0.5 * np.cos(freq * np.pi * x[i])**3 * np.exp(-0.05 * x[i]**2)
            result += 0.3 * np.sin(3 * freq * np.pi * x[i]) * np.cos(2 * freq * np.pi * x[i])
        
        # Higher-order polynomial penalty terms to create ruggedness
        for i in range(self.dim):
            result += 0.02 * x[i]**4 + 0.01 * x[i]**6 + 0.005 * x[i]**8
        
        # Complex cross-dimensional coupling with exponential interactions
        for i in range(self.dim - 1):
            result += 0.05 * np.exp(-0.5 * (x[i] - x[i+1])**2) * np.sin(3 * np.pi * (x[i] + x[i+1]))
            result += 0.04 * np.sinh(0.3 * x[i]) * np.cos(2 * np.pi * x[i+1])
            result += 0.03 * (x[i]**2 + x[i+1]**2) * np.exp(-0.1 * np.abs(x[i] - x[i+1]))
        
        # Add a global scaling factor with chaotic modulation
        chaos_factor = 1.0 + 0.2 * np.sin(5 * np.pi * np.sum(np.abs(x)))
        result *= chaos_factor
        
        # Add a small noise term to increase problem difficulty
        result += 0.001 * np.sum(np.random.randn(self.dim) * x)
        
        return result