import numpy as np

class ChaoticOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Initialize function value
        result = 0.0
        
        # Add polynomial potential terms
        for i in range(self.dim):
            xi = x[i]
            # Higher order polynomial terms
            result += 0.1 * xi**4 + 0.5 * xi**3 - 2.0 * xi**2 + 1.5 * xi
            
        # Add chaotic sinusoidal components
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Coupled oscillatory terms
                term = np.sin(x[i] * x[j] * 0.5) * np.cos(x[i] + x[j] * 0.3)
                result += 0.3 * term
                
        # Add cross-terms creating complex interactions
        for i in range(self.dim):
            result += 0.2 * np.sin(x[i] * 2.0) * np.cos(x[i] * 1.5)
            
        # Add noise to increase complexity
        noise = np.sum(np.random.normal(0, 0.01, self.dim))
        
        return result + noise