import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.array(x)
        
        # Global minimum at origin
        if np.allclose(x, 0):
            return 0.0
            
        # Base function with multiple local minima
        result = 0.0
        
        # Sum of quadratic terms with different coefficients
        for i in range(self.dim):
            result += (x[i] ** 2) * (i + 1)
            
        # Add sinusoidal perturbations to create local minima
        for i in range(self.dim):
            result += 0.1 * np.sin(5 * x[i]) * np.cos(3 * x[(i + 1) % self.dim])
            
        # Add exponential interference terms for increased complexity
        for i in range(self.dim):
            result += 0.05 * np.exp(-0.5 * (x[i] ** 2)) * np.sin(2 * np.pi * x[i])
            
        # Add cross-term interactions with higher frequency components
        for i in range(self.dim):
            j = (i + 2) % self.dim
            result += 0.03 * np.sin(10 * x[i]) * np.cos(7 * x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
            
        # Add a global scaling factor to ensure the function is well-conditioned
        result *= 1.0 + 0.1 * np.sum(x ** 2)
        
        # Add a highly oscillatory component for increased difficulty
        result += 0.2 * np.prod(np.sin(0.5 * x))
        
        return result