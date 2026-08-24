import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Enhanced chaotic component with varying frequencies and amplitudes
        for i in range(self.dim):
            xi = x[i]
            # Add chaotic behavior with multiple frequencies and amplitudes
            result += (0.7 * np.sin(xi) * np.cos(3 * xi) + 
                      0.5 * np.sin(2 * xi) * np.cos(5 * xi) + 
                      0.3 * np.sin(7 * xi) * np.cos(11 * xi) +
                      0.2 * np.sin(4 * xi) * np.cos(9 * xi))
        
        # Enhanced polynomial basin component
        poly_term = np.sum(x**4) / self.dim
        
        # Enhanced logarithmic barrier with stronger penalty near boundaries
        log_term = 0.0
        for i in range(self.dim):
            log_term += np.log(1.0 + 0.5 * np.abs(x[i]) / 5.0)
        
        # Add cross-term interactions for increased conditioning
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += 0.1 * np.sin(x[i]) * np.cos(x[j])
        
        # Combine all terms with optimized weights
        result = 0.5 * result + 0.3 * poly_term + 0.2 * log_term + 0.1 * cross_term
        
        return result