import numpy as np

class InterconnectedValleysBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = 0.1 * np.sum(x**2)
        
        # Periodic oscillation component
        f2 = 0.0
        for i in range(self.dim):
            f2 += np.sin(3.0 * x[i]) * np.cos(2.0 * x[i])
        
        # Asymmetric plateaus with exponential decay
        f3 = 0.0
        for i in range(self.dim):
            if x[i] >= 0:
                f3 += 2.0 * np.exp(-0.5 * (x[i] - 2.0)**2)
            else:
                f3 += 1.5 * np.exp(-0.3 * (x[i] + 2.0)**2)
        
        # Dynamic conditioning with sine modulation
        f4 = 0.0
        for i in range(self.dim):
            f4 += (1.0 + 0.5 * np.sin(0.5 * i)) * x[i]**4
        
        # Interconnected ridges and valleys
        f5 = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                f5 += np.sin(2.0 * (x[i] + x[j])) * np.cos(1.5 * (x[i] - x[j]))
        
        # Cross-terms with varying weights
        f6 = 0.0
        for i in range(self.dim):
            f6 += (i + 1) * np.sin(0.7 * x[i]) * np.cos(0.3 * x[i])
        
        # Add noise to increase complexity
        noise = 0.01 * np.sum(np.random.randn(self.dim))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + noise