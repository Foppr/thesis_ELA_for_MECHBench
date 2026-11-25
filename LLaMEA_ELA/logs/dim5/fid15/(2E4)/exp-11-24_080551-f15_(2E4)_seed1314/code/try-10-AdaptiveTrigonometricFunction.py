import numpy as np

class AdaptiveTrigonometricFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Base polynomial term with varying exponents
        result = 0.0
        for i in range(self.dim):
            result += (x[i] ** (2 + i % 3)) / (1.0 + i)
            
        # Trigonometric coupling terms with adaptive frequencies
        for i in range(self.dim):
            freq_i = 1.0 + 0.5 * np.sin(i)
            result += np.sin(freq_i * x[i]) * np.cos(freq_i * x[(i + 1) % self.dim])
            
        # Cross-dimensional interaction with distance-dependent scaling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                scale = 1.0 / (1.0 + dist)
                result += scale * np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
                
        # Adaptive exponential decay term based on dimension
        decay_factor = np.exp(-0.1 * self.dim)
        result += decay_factor * np.sum(np.abs(x))
        
        return result