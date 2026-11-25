import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Calculate the multimodal function
        result = 0.0
        
        # Quadratic component with exponential scaling
        for i in range(self.dim):
            result += x[i]**2 * (1.0 + 0.1 * np.exp(-0.1 * x[i]**2))
        
        # Add sinusoidal perturbations with varying frequencies and amplitudes
        for i in range(self.dim):
            result += 0.2 * np.sin(3 * x[i]) * np.cos(7 * x[i]) * np.exp(-0.05 * abs(x[i]))
        
        # Add coupling terms between dimensions with chaotic interaction
        for i in range(self.dim - 1):
            result += 0.1 * np.sin(x[i] * x[i+1]) * np.exp(-0.02 * (x[i]**2 + x[i+1]**2))
        
        # Add a global scaling factor to increase complexity
        result *= (1.0 + 0.05 * np.sum(np.abs(x)))
        
        return result