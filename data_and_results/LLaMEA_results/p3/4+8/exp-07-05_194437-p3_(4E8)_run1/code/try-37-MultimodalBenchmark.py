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
        result += 0.3 * np.sum(x**2)
        
        # Add periodic terms with varying frequencies
        for i in range(self.dim):
            result += 7 * np.sin(3.0 * np.pi * x[i] / (1 + 0.2 * i)) * np.cos(4.0 * np.pi * x[i] / (1 + 0.3 * i))
        
        # Add a more complex interaction term with stronger coupling
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Increased cross-interaction
                result += 4 * np.sin(x[i]) * np.cos(x[j]) * np.exp(-0.03 * (x[i] - x[j])**2)
        
        # Add a global shaping term
        result += 0.03 * np.sum(np.abs(x)**3.7)
        
        # Add a noise-like component for added complexity
        for i in range(self.dim):
            result += 0.7 * np.sin(13 * x[i]) * np.cos(7 * x[i])
        
        return result