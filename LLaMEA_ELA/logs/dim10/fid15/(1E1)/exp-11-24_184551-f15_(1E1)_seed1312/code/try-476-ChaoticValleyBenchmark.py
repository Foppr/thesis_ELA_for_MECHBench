import numpy as np

class ChaoticValleyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Initialize function value
        result = 0.0
        
        # Add polynomial valley terms (creates deep, narrow valleys)
        for i in range(self.dim):
            result += 0.5 * x[i]**4 - 2.0 * x[i]**2
            
        # Add sinusoidal oscillations (creates chaotic terrain with many local minima)
        for i in range(self.dim):
            result += 2.0 * np.sin(3.0 * x[i]) + 1.5 * np.cos(2.0 * x[i])
            
        # Add cross-terms to create correlations between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.3 * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                
        # Add a global quadratic term to balance the landscape
        result += 0.1 * np.sum(x**2)
        
        # Add chaotic behavior with exponential terms
        for i in range(self.dim):
            result += 0.2 * np.exp(-0.5 * (x[i] - 1.0)**2) + 0.1 * np.exp(-0.3 * (x[i] + 2.0)**2)
            
        return result