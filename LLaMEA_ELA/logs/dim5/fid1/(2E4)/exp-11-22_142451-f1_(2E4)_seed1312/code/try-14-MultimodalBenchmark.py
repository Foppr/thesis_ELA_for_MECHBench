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
            result += 0.3 * np.sin(12 * x[i]) * np.cos(8 * x[i])
            
        # Add coupling between variables with more complex interaction
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.03 * np.sin(x[i]**2 + x[j]**2) * np.cos(x[i] * x[j])
                
        # Add a fourth-order polynomial term to increase landscape complexity
        for i in range(self.dim):
            result += 0.06 * x[i]**4
            
        # Add cross-terms with different frequencies to create more intricate structure
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.015 * np.sin(3 * x[i]) * np.cos(5 * x[j]) * (x[i]**2 + x[j]**2)
                
        # Add a fifth-order term to increase landscape complexity
        for i in range(self.dim):
            result += 0.02 * x[i]**5
            
        # Add a sixth-order term for even more complexity
        for i in range(self.dim):
            result += 0.01 * x[i]**6
            
        return result