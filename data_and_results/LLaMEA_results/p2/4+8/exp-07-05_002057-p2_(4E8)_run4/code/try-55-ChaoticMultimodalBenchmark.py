import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Chaotic component using sine and cosine with varying frequencies and chaotic perturbations
        for i in range(self.dim):
            xi = x[i]
            # Enhanced chaotic behavior with perturbed frequencies and amplitudes
            result += (0.9 * np.sin(xi) * np.cos(3.5 * xi) + 
                      0.7 * np.sin(2.2 * xi) * np.cos(4.8 * xi) + 
                      0.5 * np.sin(6.7 * xi) * np.cos(10.2 * xi) + 
                      0.3 * np.sin(3.9 * xi) * np.cos(8.1 * xi) + 
                      0.1 * np.sin(5.3 * xi) * np.cos(6.4 * xi))
        
        # Polynomial basin component with stronger cross-dimensional interactions
        poly_term = np.sum(x**4) / self.dim
        cross_term = 0.15 * np.sum(x**2) * np.sum(x**3) / (self.dim**2)
        
        # Enhanced logarithmic barrier with exponential scaling for sharper conditioning
        log_term = 0.0
        for i in range(self.dim):
            log_term += np.log(1.0 + 0.3 * np.abs(x[i]) / 5.0) * np.exp(-0.1 * np.abs(x[i]))
        
        # Additional quadratic cross-term for increased conditioning
        quad_cross = 0.05 * np.sum((x[i] - x[(i+1) % self.dim])**2 for i in range(self.dim))
        
        # Combine all terms with optimized weights
        result = 0.3 * result + 0.3 * poly_term + 0.2 * cross_term + 0.15 * log_term + 0.05 * quad_cross
        
        return result