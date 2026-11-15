import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Calculate the multimodal function
        # Combines quadratic, sinusoidal, and exponential terms with enhanced complexity
        result = 0.0
        
        # Quadratic term (global minimum at origin)
        result += np.sum(x**2)
        
        # Sinusoidal terms to create multiple local minima with varying frequencies
        for i in range(self.dim):
            result += 15 * np.sin(0.7 * x[i]) * np.cos(0.4 * x[i]) * np.sin(0.2 * x[i])
        
        # Exponential terms with adaptive scaling
        for i in range(self.dim):
            result += 3 * np.exp(-0.05 * x[i]**2) * np.sin(0.6 * x[i])
        
        # Cross-terms with varying interaction strengths
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction_strength = 0.3 * (1 + np.sin(0.5 * (x[i] + x[j])))
                result += interaction_strength * np.sin(x[i] * x[j]) * np.cos(0.3 * (x[i] - x[j]))
        
        # Additional high-frequency oscillations to increase complexity
        for i in range(self.dim):
            result += 2 * np.sin(3.0 * x[i]) * np.cos(2.0 * x[i]) * np.sin(0.1 * x[i]**2)
        
        return result