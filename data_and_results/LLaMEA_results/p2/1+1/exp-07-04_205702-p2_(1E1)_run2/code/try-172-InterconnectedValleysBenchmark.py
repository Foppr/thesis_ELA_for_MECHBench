import numpy as np

class InterconnectedValleysBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with dynamic conditioning
        f1 = 0.1 * np.sum(x**2)
        
        # Add interconnected valleys using sinusoidal modulation
        f2 = 0.0
        for i in range(self.dim):
            f2 -= 2.0 * np.cos(0.5 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Add ridges with polynomial interactions
        f3 = 0.0
        for i in range(self.dim):
            f3 += 0.5 * x[i]**4 - 2.0 * x[i]**2
        
        # Introduce periodic oscillations with varying frequencies
        f4 = 0.0
        for i in range(self.dim):
            f4 += np.sin(2.0 * np.pi * x[i]) * np.cos(0.3 * x[i])
        
        # Add cross-dimensional interactions with dynamic weights
        f5 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.1 + 0.2 * np.sin(0.5 * (i + j))
                f5 += weight * (x[i]**2 + x[j]**2) * np.sin(0.2 * x[i] * x[j])
        
        # Include asymmetric basin structures with exponential decay
        f6 = 0.0
        for i in range(self.dim):
            f6 += 1.5 * np.exp(-0.2 * (x[i] - 2.0)**2) * np.sin(0.8 * x[i])
        
        # Add a dynamic conditioning component
        f7 = 0.0
        for i in range(self.dim):
            f7 += (i + 1) * np.abs(x[i])**1.5 * np.cos(1.2 * x[i])
        
        # Add noise term for robustness
        noise = 0.01 * np.random.rand()
        
        # Combine all components
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + noise