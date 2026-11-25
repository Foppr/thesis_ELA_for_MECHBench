import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        for i in range(self.dim):
            # Base quadratic term with exponential modulation
            result += (x[i]**2) * np.exp(-0.1 * x[i]**2)
            
            # Add sinusoidal components with varying frequencies and amplitudes
            result += 2.0 * np.sin(2.5 * x[i]) * np.cos(1.3 * x[i])
            
            # Include higher-order polynomial and cross-term interactions
            if i > 0:
                result += 0.5 * x[i] * x[i-1] * np.sin(x[i] + x[i-1])
                
        # Add a global shaping term with multiple peaks
        result += 3.0 * np.exp(-0.5 * np.sum((x - 1.0)**2)) + \
                  2.0 * np.exp(-0.3 * np.sum((x + 1.5)**2)) + \
                  1.5 * np.exp(-0.2 * np.sum((x - 2.0)**2))
        
        # Add noise-like perturbations to increase complexity
        result += 0.1 * np.sum(np.sin(5 * x) * np.cos(3 * x))
        
        return result