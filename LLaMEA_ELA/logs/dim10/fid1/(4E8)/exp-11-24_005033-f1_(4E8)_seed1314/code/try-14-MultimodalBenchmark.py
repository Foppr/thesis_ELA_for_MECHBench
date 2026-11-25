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
        
        # Chaotic sinusoidal components with varying frequencies and amplitudes
        for i in range(self.dim):
            result += 0.5 * np.sin(2 * np.pi * x[i]) * np.cos(3 * np.pi * x[i])
            result += 0.3 * np.sin(4 * np.pi * x[i])**3
            result += 0.2 * np.cos(5 * np.pi * x[i])**2
        
        # Polynomial penalty terms to create ruggedness
        for i in range(self.dim):
            result += 0.01 * x[i]**4 + 0.005 * x[i]**6
        
        # Cross-dimensional coupling with chaotic interaction terms
        for i in range(self.dim - 1):
            result += 0.03 * np.sin(x[i] * x[i+1]) * np.cos(x[i] + x[i+1])
            result += 0.02 * (x[i]**2 + x[i+1]**2) * np.sin(0.5 * (x[i] - x[i+1])**2)
        
        # Add a global scaling factor to control the function's overall magnitude
        result *= (1.0 + 0.1 * np.sum(np.abs(x)))
        
        return result