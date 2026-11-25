import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Add multiple periodic components with different frequencies and amplitudes
        for i in range(1, 6):
            result += (1.0 / i) * np.sum(np.sin(i * x) * np.cos(i * x))
        
        # Add exponential decay terms that create complex valleys
        for i in range(self.dim):
            result += 0.5 * np.exp(-0.1 * np.abs(x[i])) * np.sin(2 * np.pi * x[i])
        
        # Cross-dimensional interaction terms
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += 0.3 * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
        
        result += cross_term
        
        # Add a global scaling factor to increase multimodality
        result *= (1.0 + 0.5 * np.sum(np.sin(0.5 * x)**2))
        
        return result