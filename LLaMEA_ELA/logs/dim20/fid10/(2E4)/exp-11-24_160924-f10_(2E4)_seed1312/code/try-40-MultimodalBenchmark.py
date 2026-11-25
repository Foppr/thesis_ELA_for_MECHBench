import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Add chaotic polynomial and sinusoidal components with varying frequencies
        for i in range(self.dim):
            xi = x[i]
            # Chaotic behavior using sine and cosine with non-integer powers
            result += (xi**5 - 10 * xi**3 + 25 * xi) * np.sin(0.5 * xi**2) + 0.5 * xi**3 * np.cos(0.4 * xi**1.5)
            
        # Add time-delayed feedback terms between dimensions
        for i in range(self.dim):
            for j in range(max(0, i-3), i):  # Delayed coupling with up to 3 steps back
                # Introduce chaotic feedback based on previous dimension values
                result += 0.3 * np.sin(2.0 * (x[i] - x[j])) * np.exp(-0.1 * (x[i] - x[j])**2)
                
        # Add fractional Brownian motion inspired interaction terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractional noise-like interaction with distance-dependent scaling
                dist = np.abs(x[i] - x[j])
                result += 0.4 * np.exp(-dist**2) * np.sin(3.0 * dist) * (1.0 + 0.1 * np.sin(5.0 * x[i]))
                
        # Add global conditioning and multi-scale modulation
        result += 0.05 * np.sum(np.sin(0.2 * x)**4) + 0.03 * np.sum(np.cos(0.3 * x)**3)
        
        # Add a complex interaction term that creates multiple local minima with chaotic behavior
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.25 * np.sin(4.0 * (x[i]**2 + x[j]**2)) * np.exp(-0.08 * (x[i] - x[j])**2) * np.cos(0.5 * x[i])
                
        return result