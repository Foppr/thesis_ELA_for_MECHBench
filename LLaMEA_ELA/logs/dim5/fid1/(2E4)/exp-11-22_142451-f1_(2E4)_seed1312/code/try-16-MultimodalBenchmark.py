import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for global minimum at origin
        result = np.sum(x**2)
        
        # Add multiple local minima using higher frequency sinusoidal terms
        for i in range(self.dim):
            result += 0.4 * np.sin(15 * x[i]) * np.cos(10 * x[i])
            
        # Add coupling between variables with more complex interaction
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.04 * np.sin(x[i]**3 + x[j]**3) * np.cos(x[i] * x[j]**2)
                
        # Add a fourth-order polynomial term to increase landscape complexity
        for i in range(self.dim):
            result += 0.08 * x[i]**4
            
        # Add cross-terms with different frequencies to create more intricate structure
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.02 * np.sin(4 * x[i]) * np.cos(6 * x[j]) * (x[i]**3 + x[j]**3)
                
        # Add a fifth-order term to increase landscape complexity
        for i in range(self.dim):
            result += 0.03 * x[i]**5
            
        # Add a sixth-order term for even more complexity
        for i in range(self.dim):
            result += 0.015 * x[i]**6
            
        # Add adaptive scaling based on dimensionality
        result *= (1 + 0.1 * self.dim)
        
        return result