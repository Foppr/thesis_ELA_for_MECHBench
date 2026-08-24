import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Add quadratic term for conditioning
        result += 0.15 * np.sum(x**2)
        
        # Add periodic terms with varying frequencies and phases
        for i in range(self.dim):
            result += 6 * np.sin(2.5 * np.pi * x[i] / (1 + 0.15 * i)) * np.cos(3.5 * np.pi * x[i] / (1 + 0.25 * i))
        
        # Add stronger cross-interaction terms
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Increased cross-interaction
                result += 3 * np.sin(x[i]) * np.cos(x[j]) * np.exp(-0.02 * (x[i] - x[j])**2)
        
        # Add a global shaping term with higher exponent
        result += 0.02 * np.sum(np.abs(x)**4)
        
        # Add a noise-like component with different frequencies
        for i in range(self.dim):
            result += 0.6 * np.sin(12 * x[i]) * np.cos(6 * x[i])
        
        # Shift the global minimum to (1,1,...,1)
        result += 0.5 * np.sum((x - 1.0)**2)
        
        return result