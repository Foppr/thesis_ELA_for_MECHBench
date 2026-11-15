import numpy as np

class AdaptiveHybridBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial base with adaptive conditioning
        f1 = np.sum((x**4) / (1.0 + np.abs(x)**2))
        
        # Exponential decay with sinusoidal modulation
        f2 = 0.0
        for i in range(self.dim):
            f2 -= np.exp(-0.1 * x[i]**2) * np.sin(3.0 * x[i]) * np.cos(2.0 * x[i])
        
        # Adaptive Gaussian peaks with dynamic positions and widths
        f3 = 0.0
        for i in range(self.dim):
            sigma = 1.0 + 0.5 * np.sin(0.5 * i)
            mu = 3.0 * np.cos(0.3 * i)
            f3 -= np.exp(-0.5 * ((x[i] - mu) / sigma)**2) * (1.0 + 0.2 * np.sin(7.0 * x[i]))
        
        # Multi-scale sinusoidal interaction terms
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited range interaction
                f4 += np.sin(x[i]) * np.cos(x[j]) * np.exp(-0.1 * (x[i] - x[j])**2)
        
        # Asymmetric long-range coupling
        f5 = 0.0
        for i in range(self.dim):
            f5 += np.sin(0.5 * x[i]) * np.exp(-0.05 * np.sum(x**2)) * (1.0 + 0.1 * np.cos(3.0 * x[i]))
        
        # Adaptive conditioning with dynamic weights
        weights = np.array([1.0 + 0.3 * np.sin(0.2 * i) for i in range(self.dim)])
        f6 = np.sum(weights * np.abs(x)**3)
        
        # Combined chaotic component
        f7 = 0.1 * np.sum(np.sin(np.exp(x)) * np.cos(np.log(np.abs(x) + 1e-8)) * np.exp(-0.1 * np.abs(x)))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7