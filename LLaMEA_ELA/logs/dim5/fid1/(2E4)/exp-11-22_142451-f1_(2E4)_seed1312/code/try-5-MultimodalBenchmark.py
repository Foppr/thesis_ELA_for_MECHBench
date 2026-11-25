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
            result += 0.2 * np.sin(10 * x[i]) * np.cos(7 * x[i])
            
        # Add coupling between variables with more complex interaction
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.02 * np.sin(x[i]**2 + x[j]**2) * np.cos(x[i] * x[j])
                
        # Add a fourth-order polynomial term to increase landscape complexity
        for i in range(self.dim):
            result += 0.05 * x[i]**4
            
        # Add cross-terms with different frequencies to create more intricate structure
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.01 * np.sin(2 * x[i]) * np.cos(3 * x[j]) * (x[i]**2 + x[j]**2)
                
        return result