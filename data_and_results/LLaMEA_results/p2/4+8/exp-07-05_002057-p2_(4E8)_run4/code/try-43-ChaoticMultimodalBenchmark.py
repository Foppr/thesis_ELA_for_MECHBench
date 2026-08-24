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
            # Add chaotic behavior with modified frequencies and amplitudes
            result += (0.8 * np.sin(xi) * np.cos(3 * xi) + 
                      0.6 * np.sin(2 * xi) * np.cos(5 * xi) + 
                      0.4 * np.sin(7 * xi) * np.cos(11 * xi) + 
                      0.2 * np.sin(4 * xi) * np.cos(9 * xi))
        
        # Polynomial basin component with cross-dimensional interactions
        poly_term = np.sum(x**4) / self.dim
        cross_term = 0.1 * np.sum(x**2) * np.sum(x**3) / (self.dim**2)
        
        # Enhanced logarithmic barrier with non-linear scaling
        log_term = 0.0
        for i in range(self.dim):
            log_term += np.log(1.0 + 0.5 * np.abs(x[i]) / 5.0)
        
        # Combine all terms with different weights
        result = 0.35 * result + 0.35 * poly_term + 0.2 * cross_term + 0.1 * log_term
        
        return result