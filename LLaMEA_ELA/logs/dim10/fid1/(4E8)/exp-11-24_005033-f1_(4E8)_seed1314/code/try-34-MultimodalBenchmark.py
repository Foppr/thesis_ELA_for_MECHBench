import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponentially increasing oscillations with chaotic sine-cosine interactions
        result = np.sum(np.exp(0.5 * np.abs(x)) * np.sin(20.0 * np.pi * x) * np.cos(15.0 * np.pi * x))
        
        # Cross-dimensional cubic couplings
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.1 * (x[i]**3 + x[j]**3) * np.sin(5.0 * (x[i] - x[j]))
        
        # Adaptive polynomial penalties
        penalty = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 2.0:
                penalty += 10.0 * (np.abs(x[i]) - 2.0)**3
            else:
                penalty += 0.5 * x[i]**4
                
        result += penalty
        
        # Additional high-frequency trigonometric peaks
        result += 2.0 * np.sum(np.sin(50.0 * x) + np.cos(30.0 * x))
        
        return result