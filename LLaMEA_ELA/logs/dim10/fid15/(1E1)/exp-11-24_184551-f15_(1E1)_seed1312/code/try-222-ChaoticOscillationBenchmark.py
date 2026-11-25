import numpy as np

class ChaoticOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Initialize function value
        result = 0.0
        
        # Add polynomial terms with varying degrees
        for i in range(self.dim):
            xi = x[i]
            # Higher degree polynomial terms to create complex landscape
            result += (xi**4 - 2*xi**2 + 1) * (i + 1) * 0.1
            
        # Add chaotic sinusoidal components
        for i in range(self.dim):
            xi = x[i]
            # Multiple sine waves with different frequencies and amplitudes
            result += np.sin(xi * (i + 1)) * np.cos(xi * (i + 1) * 0.5) * 0.3
            
        # Add cross-terms to create coupling between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += np.sin(x[i] * x[j]) * 0.2
                
        # Add a global scaling factor and noise
        result *= 1.0 + np.random.normal(0, 0.01)
        
        return result