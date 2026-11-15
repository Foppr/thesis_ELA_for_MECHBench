import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Enhanced chaotic component with nested sinusoidal perturbations
        for i in range(self.dim):
            xi = x[i]
            # Complex chaotic structure with multiple frequency combinations
            result += (0.9 * np.sin(xi) * np.cos(5 * xi) * np.sin(3 * xi) + 
                      0.7 * np.sin(2 * xi) * np.cos(7 * xi) * np.sin(4 * xi) + 
                      0.5 * np.sin(9 * xi) * np.cos(13 * xi) * np.sin(6 * xi) + 
                      0.3 * np.sin(4 * xi) * np.cos(11 * xi) * np.sin(8 * xi))
        
        # Higher-order polynomial basin with nested interactions
        poly_term = np.sum(x**6) / self.dim
        cross_term = 0.15 * np.sum(x**3) * np.sum(x**4) / (self.dim**2)
        nested_term = 0.05 * np.sum(x**2) * np.sum(x**5) / (self.dim**2)
        
        # Nested logarithmic barrier with exponential scaling
        log_term = 0.0
        for i in range(self.dim):
            log_term += np.log(1.0 + 0.3 * np.abs(x[i]) / 5.0) * np.exp(-0.1 * np.abs(x[i]))
        
        # Additional cross-dimensional coupling with chaotic modulation
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_term += np.sin(x[i] * x[j]) * np.cos(2 * x[i] + x[j])
        
        # Combine all terms with different weights
        result = 0.4 * result + 0.3 * poly_term + 0.15 * cross_term + 0.1 * nested_term + 0.05 * log_term + 0.05 * coupling_term
        
        return result