import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        for i in range(self.dim):
            # Base quadratic term with exponential modulation and oscillation
            result += (x[i]**2) * np.exp(-0.1 * x[i]**2) * (1.0 + 0.3 * np.sin(3.0 * x[i]))
            
            # Add sinusoidal components with varying frequencies and amplitudes
            result += 3.0 * np.sin(3.0 * x[i]) * np.cos(2.0 * x[i]) + \
                      1.5 * np.sin(5.0 * x[i]) * np.cos(1.0 * x[i])
            
            # Include higher-order polynomial and cross-term interactions
            if i > 0:
                result += 0.8 * x[i] * x[i-1] * np.sin(x[i] + x[i-1]) + \
                          0.3 * (x[i]**2) * (x[i-1]**2) * np.cos(x[i] - x[i-1])
                
        # Add a global shaping term with multiple peaks and valleys
        result += 4.0 * np.exp(-0.5 * np.sum((x - 1.0)**2)) + \
                  3.0 * np.exp(-0.3 * np.sum((x + 1.5)**2)) + \
                  2.5 * np.exp(-0.2 * np.sum((x - 2.0)**2)) + \
                  1.8 * np.exp(-0.4 * np.sum((x + 2.5)**2))
        
        # Add noise-like perturbations to increase complexity
        result += 0.2 * np.sum(np.sin(7 * x) * np.cos(4 * x)) + \
                  0.1 * np.sum(np.sin(9 * x) * np.cos(2 * x))
        
        # Add a non-separable component with mixed interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.5 * np.sin(x[i] * x[j]) * np.exp(-0.1 * (x[i] - x[j])**2)
        
        return result