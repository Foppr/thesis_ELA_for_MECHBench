import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Enhanced chaotic component with higher frequency interactions and phase shifts
        for i in range(self.dim):
            xi = x[i]
            # Add enhanced chaotic behavior with multiple frequencies and phase shifts
            result += (0.8 * np.sin(2.5 * xi) * np.cos(7.2 * xi) + 
                      0.6 * np.sin(4.1 * xi) * np.cos(9.3 * xi) + 
                      0.4 * np.sin(6.7 * xi) * np.cos(13.8 * xi) +
                      0.2 * np.sin(3.9 * xi) * np.cos(15.1 * xi))
        
        # Modified polynomial basin with higher degree and scaling
        poly_term = 0.5 * np.sum(x**6) / self.dim
        
        # Enhanced logarithmic barrier with exponential scaling
        log_term = 0.0
        for i in range(self.dim):
            log_term += np.log(1.0 + np.exp(np.abs(x[i]) / 3.0) / 5.0)
        
        # Add cross-term interactions for increased conditioning
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += 0.1 * np.sin(x[i] * x[j]) / (1.0 + np.abs(x[i] - x[j]))
        
        # Combine all terms with optimized weights
        result = 0.35 * result + 0.35 * poly_term + 0.2 * log_term + 0.1 * cross_term
        
        return result