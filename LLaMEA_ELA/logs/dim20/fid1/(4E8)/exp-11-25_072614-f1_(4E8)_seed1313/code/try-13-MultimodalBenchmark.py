import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # High-dimensional chaotic multimodal function
        result = np.sum(x**2)
        
        # Add chaotic sinusoidal perturbations with varying frequencies
        for i in range(self.dim):
            result += 0.5 * np.sin(10 * x[i]) * np.cos(7 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Add cross-dimensional interactions with exponential scaling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.1 * np.sin(x[i] * x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
        
        # Add polynomial and exponential terms for increased complexity
        result += 0.05 * np.sum(np.exp(0.5 * x**2)) + 0.02 * np.sum(x**6)
        
        return result