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
            # Multiple sine waves with different frequencies and phases
            freq = (i + 1) * 2.0
            phase = np.pi * i / self.dim
            result += np.sin(freq * xi + phase) * np.cos(freq * xi * 0.5 + phase * 2) * 0.5
            
        # Add interaction terms between variables to increase complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi, xj = x[i], x[j]
                # Non-linear interaction term
                result += (xi * xj) / (1.0 + np.abs(xi - xj)) * 0.05
                
        # Add a global scaling factor to ensure proper function range
        result *= 1.0 + 0.1 * np.sum(np.abs(x))
        
        return result