import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Calculate the multimodal function
        result = 0.0
        
        # Quadratic component (global minimum at origin)
        for i in range(self.dim):
            result += x[i]**2
        
        # Add higher-order polynomial perturbations for increased complexity
        for i in range(self.dim):
            result += 0.1 * x[i]**4 - 0.05 * x[i]**3
        
        # Add multiple sinusoidal components with different frequencies
        for i in range(self.dim):
            result += 0.08 * np.sin(7 * x[i]) + 0.06 * np.cos(4 * x[i]) + 0.04 * np.sin(2 * x[i])
        
        # Add coupling terms with varying strengths based on dimension index
        for i in range(self.dim - 1):
            coupling_strength = 0.03 + 0.02 * (i / self.dim)
            result += coupling_strength * (x[i] - x[i+1])**2
        
        # Add cross-dimensional interaction terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.02 * x[i] * x[j] * np.sin(0.5 * (x[i]**2 + x[j]**2))
        
        return result