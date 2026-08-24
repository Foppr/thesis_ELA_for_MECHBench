import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic terms with multiple local minima
        result = 0.0
        for i in range(self.dim):
            result += (x[i] - 1.0)**2 + (x[i] + 1.0)**2 + 0.1 * x[i]**4
        
        # Add trigonometric perturbations for increased multimodality
        for i in range(self.dim):
            result += 0.5 * np.sin(3.0 * x[i]) * np.cos(2.0 * x[i])
        
        # Add interaction terms with varying correlation strengths
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = 0.05 * (x[i] - x[j])**2 * (1.0 + 0.1 * np.sin(5.0 * (x[i] + x[j])))
                result += interaction
        
        # Add global minimum at origin with additional penalty
        result += 0.001 * np.sum(x**2)
        
        # Add a conditioning factor to increase problem difficulty
        conditioning = 1.0 + 0.1 * np.sum(np.abs(x))
        result *= conditioning
        
        return result