import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        for i in range(self.dim):
            # Base quadratic term with stronger exponential decay and multi-frequency oscillation
            result += (x[i]**2) * np.exp(-0.15 * x[i]**2) * (1.0 + 0.4 * np.sin(3.0 * x[i]) + 0.2 * np.sin(7.0 * x[i]))
            
            # Add complex sinusoidal components with varying amplitudes and frequencies
            result += 4.0 * np.sin(2.5 * x[i]) * np.cos(1.5 * x[i]) + \
                      2.0 * np.sin(4.0 * x[i]) * np.cos(3.0 * x[i]) + \
                      1.0 * np.sin(6.0 * x[i])
            
            # Include stronger cross-term interactions and higher-order polynomial components
            if i > 0:
                result += 1.2 * x[i] * x[i-1] * np.sin(x[i] + x[i-1]) + \
                          0.5 * (x[i]**2) * (x[i-1]**2) * np.cos(x[i] - x[i-1]) + \
                          0.3 * x[i] * x[i-1] * np.exp(-0.5 * (x[i] - x[i-1])**2)
                
        # Add a more complex global structure with multiple interacting peaks
        result += 5.0 * np.exp(-0.4 * np.sum((x - 1.2)**2)) + \
                  4.0 * np.exp(-0.2 * np.sum((x + 1.8)**2)) + \
                  3.0 * np.exp(-0.3 * np.sum((x - 2.2)**2)) + \
                  2.0 * np.exp(-0.5 * np.sum((x + 2.0)**2))
        
        # Add noise-like perturbations with different frequency components
        result += 0.3 * np.sum(np.sin(8 * x) * np.cos(3 * x)) + \
                  0.2 * np.sum(np.sin(10 * x) * np.cos(5 * x)) + \
                  0.1 * np.sum(np.sin(6 * x) * np.cos(7 * x))
        
        # Add a strong non-separable component with enhanced interaction terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.8 * np.sin(x[i] * x[j]) * np.exp(-0.15 * (x[i] - x[j])**2) + \
                          0.2 * np.cos(x[i] * x[j]) * np.exp(-0.05 * (x[i] + x[j])**2)
        
        return result