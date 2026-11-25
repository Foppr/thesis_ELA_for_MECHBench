import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin with modified adaptive scaling
        f_val = np.sum(x**2) * (1.0 + 0.15 * np.sin(0.3 * np.sum(x**2)))
        
        # Enhanced multiple local minima using modified trigonometric functions
        for i in range(self.dim):
            f_val += 0.25 * np.sin(8 * x[i]) * np.cos(3 * x[i]) * np.exp(-0.12 * abs(x[i]))
            
        # Modified saddle point structure with stronger directional dependency
        if self.dim >= 2:
            diff_sum = 0
            for i in range(self.dim - 1):
                diff_sum += (x[i] - x[i+1])**2 * (1.0 + 0.1 * np.sin(0.5 * x[i] * x[i+1]))
            f_val += 0.12 * diff_sum
            
        # Additional landscape complexity with shifted Gaussian peaks
        for i in range(0, self.dim, 2):
            if i + 1 < self.dim:
                f_val += 0.18 * np.exp(-0.5 * ((x[i] - 1.5)**2 + (x[i+1] + 1.5)**2))
                
        return f_val