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
            result += (0.8 * np.sin(xi) * np.cos(3.7 * xi) + 
                      0.6 * np.sin(2.1 * xi) * np.cos(4.9 * xi) + 
                      0.4 * np.sin(6.8 * xi) * np.cos(10.1 * xi) + 
                      0.2 * np.sin(3.8 * xi) * np.cos(8.2 * xi) + 
                      0.1 * np.sin(5.2 * xi) * np.cos(6.5 * xi))
        
        # Polynomial basin component with stronger cross-dimensional interactions
        poly_term = np.sum(x**4) / self.dim
        cross_term = 0.2 * np.sum(x**2) * np.sum(x**3) / (self.dim**2)
        
        # Enhanced logarithmic barrier with exponential scaling for sharper conditioning
        log_term = 0.0
        for i in range(self.dim):
            log_term += np.log(1.0 + 0.4 * np.abs(x[i]) / 5.0) * np.exp(-0.15 * np.abs(x[i]))
        
        # Additional quadratic cross-term for increased conditioning
        quad_cross = 0.08 * np.sum((x[i] - x[(i+1) % self.dim])**2 for i in range(self.dim))
        
        # Add a new component: Gaussian radial basis function with chaotic modulation
        rbf_term = 0.0
        for i in range(self.dim):
            rbf_term += np.exp(-0.5 * (x[i] - np.sin(0.5 * i))**2 / (0.5 + 0.1 * np.sin(0.3 * i)))
        
        # Combine all terms with optimized weights
        result = 0.25 * result + 0.3 * poly_term + 0.15 * cross_term + 0.18 * log_term + 0.07 * quad_cross + 0.05 * rbf_term
        
        return result