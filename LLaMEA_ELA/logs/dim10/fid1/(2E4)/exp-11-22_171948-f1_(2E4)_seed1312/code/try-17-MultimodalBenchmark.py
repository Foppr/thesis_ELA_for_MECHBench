import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Calculate the multimodal function
        result = 0.0
        
        # Quadratic component with modified exponential scaling
        for i in range(self.dim):
            result += x[i]**2 * (1.0 + 0.15 * np.exp(-0.15 * x[i]**2))
        
        # Add sinusoidal perturbations with altered frequencies and amplitudes
        for i in range(self.dim):
            result += 0.25 * np.sin(4 * x[i]) * np.cos(8 * x[i]) * np.exp(-0.07 * abs(x[i]))
        
        # Add coupling terms between dimensions with modified chaotic interaction
        for i in range(self.dim - 1):
            result += 0.15 * np.sin(1.5 * x[i] * x[i+1]) * np.exp(-0.03 * (x[i]**2 + x[i+1]**2))
        
        # Add a global scaling factor with increased complexity
        result *= (1.0 + 0.07 * np.sum(np.abs(x)))
        
        return result