import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Polynomial valleys with different coefficients
        for i in range(self.dim):
            result += 0.1 * (x[i]**4 - 2*x[i]**2 + 1)
            
        # Radial sinusoidal waves centered at origin
        r = np.sqrt(np.sum(x**2))
        if r > 1e-8:
            result += 2.0 * np.sin(3.0 * r) * np.exp(-0.1 * r)
            
        # Cross-dimensional coupling terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.5 * np.sin(x[i] * x[j]) * (1.0 + 0.1 * np.cos(2.0 * (x[i] + x[j])))
                
        # Add a global scaling factor to control the landscape difficulty
        result *= (1.0 + 0.2 * np.sin(0.5 * r))
        
        return result