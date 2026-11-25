import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        for i in range(self.dim):
            # Base quadratic term with enhanced exponential modulation and oscillation
            result += (x[i]**2) * np.exp(-0.15 * x[i]**2) * (1.0 + 0.4 * np.sin(3.5 * x[i]))
            
            # Add sinusoidal components with varying frequencies and amplitudes
            result += 3.5 * np.sin(3.5 * x[i]) * np.cos(2.5 * x[i]) + \
                      1.8 * np.sin(5.5 * x[i]) * np.cos(1.5 * x[i])
            
            # Include higher-order polynomial and cross-term interactions with increased complexity
            if i > 0:
                result += 1.0 * x[i] * x[i-1] * np.sin(x[i] + x[i-1]) + \
                          0.4 * (x[i]**2) * (x[i-1]**2) * np.cos(x[i] - x[i-1])
                
        # Add a global shaping term with multiple peaks and valleys with varied amplitudes
        result += 5.0 * np.exp(-0.4 * np.sum((x - 1.2)**2)) + \
                  4.0 * np.exp(-0.25 * np.sum((x + 1.8)**2)) + \
                  3.0 * np.exp(-0.35 * np.sum((x - 2.2)**2)) + \
                  2.0 * np.exp(-0.5 * np.sum((x + 2.8)**2))
        
        # Add noise-like perturbations with different frequencies to increase complexity
        result += 0.25 * np.sum(np.sin(8 * x) * np.cos(3 * x)) + \
                  0.15 * np.sum(np.sin(10 * x) * np.cos(1.5 * x))
        
        # Add a non-separable component with stronger mixed interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.7 * np.sin(x[i] * x[j]) * np.exp(-0.12 * (x[i] - x[j])**2)
        
        # Add a new component that introduces sharper valleys and steeper gradients
        result += 2.5 * np.sum(np.abs(x) ** 3.0) + \
                  1.5 * np.sum(np.sin(4.0 * x) * np.cos(3.0 * x))
        
        return result