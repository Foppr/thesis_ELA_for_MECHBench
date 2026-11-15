import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Chaotic component using sine and cosine with varying frequencies
        for i in range(self.dim):
            xi = x[i]
            # Add chaotic behavior with multiple frequencies
            result += (np.sin(xi) * np.cos(3 * xi) + 
                      np.sin(2 * xi) * np.cos(5 * xi) + 
                      0.5 * np.sin(7 * xi) * np.cos(11 * xi))
        
        # Polynomial basin component
        poly_term = np.sum(x**4) / self.dim
        
        # Logarithmic barrier to prevent escape from search space
        log_term = 0.0
        for i in range(self.dim):
            log_term += np.log(1.0 + np.abs(x[i]) / 5.0)
        
        # Combine all terms with different weights
        result = 0.4 * result + 0.3 * poly_term + 0.3 * log_term
        
        return result