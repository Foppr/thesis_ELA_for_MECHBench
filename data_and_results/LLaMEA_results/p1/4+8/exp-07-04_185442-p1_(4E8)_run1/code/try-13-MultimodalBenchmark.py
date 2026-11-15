import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f = np.sum(x**2)
        
        # Add coupled multimodal components with varying frequencies
        for i in range(self.dim):
            f += 0.2 * np.sin(7 * x[i]) * np.cos(4 * x[i]) + 0.1 * np.sin(3 * x[i])**2
            
        # Add cross-term interactions for increased complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f += 0.05 * np.sin(x[i] + x[j]) * np.cos(2 * x[i] - x[j])
                
        # Enhance global minimum with a more complex penalty
        f += 0.02 * np.sum(np.sin(15 * x) + np.cos(10 * x))
        
        return f