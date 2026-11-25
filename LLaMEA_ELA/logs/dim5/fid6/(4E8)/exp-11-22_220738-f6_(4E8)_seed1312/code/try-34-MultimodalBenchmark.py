import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin with modified adaptive scaling
        f_val = np.sum(x**2) * (1.0 + 0.2 * np.sin(0.4 * np.sum(x**2)))
        
        # Enhanced multiple local minima using modified trigonometric functions
        for i in range(self.dim):
            f_val += 0.3 * np.sin(10 * x[i]) * np.cos(4 * x[i]) * np.exp(-0.15 * abs(x[i]))
            
        # Modified saddle point structure with stronger directional dependency
        if self.dim >= 2:
            diff_sum = 0
            for i in range(self.dim - 1):
                diff_sum += (x[i] - x[i+1])**2 * (1.0 + 0.2 * np.sin(0.7 * x[i] * x[i+1]))
            f_val += 0.15 * diff_sum
            
        # Additional landscape complexity with shifted Gaussian peaks
        for i in range(0, self.dim, 2):
            if i + 1 < self.dim:
                f_val += 0.22 * np.exp(-0.5 * ((x[i] - 2.0)**2 + (x[i+1] + 2.0)**2))
                
        # Cross-dimensional coupling term to increase problem difficulty
        cross_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += x[i] * x[j] * np.sin(0.3 * (x[i]**2 + x[j]**2))
        f_val += 0.1 * cross_term
        
        return f_val