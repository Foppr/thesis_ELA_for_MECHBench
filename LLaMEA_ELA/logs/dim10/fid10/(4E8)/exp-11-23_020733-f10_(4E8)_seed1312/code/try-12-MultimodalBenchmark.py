import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Main quadratic term (global minimum at origin)
        result = np.sum(x**2)
        
        # Add multiple local minima using higher-order sinusoidal terms
        for i in range(self.dim):
            result += 0.2 * np.sin(7 * x[i]) * np.cos(4 * x[i]) + 0.1 * np.sin(3 * x[i])**2
            
        # Add interaction terms between dimensions with mixed frequencies
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.1 * np.sin(2 * x[i]) * np.cos(3 * x[j]) + 0.05 * np.sin(x[i] + x[j])**3
                
        # Add polynomial interaction terms to increase landscape complexity
        for i in range(self.dim):
            result += 0.05 * x[i]**4 + 0.03 * x[i]**6
            
        # Add cross-dimensional polynomial terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.02 * (x[i]**3) * (x[j]**2)
                
        # Add a more complex noise component
        result += 0.01 * np.sum(np.sin(15 * x) + np.cos(8 * x))
        
        return result