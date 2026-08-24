import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Periodic parabolic ridges in each dimension
        ridge_term = np.sum((x_scaled**2) * np.cos(8 * np.pi * x_scaled)**2)
        
        # Logarithmic barrier terms near the boundaries
        barrier_term = np.sum(np.log(1 + 10 * (1 - np.abs(x_scaled))**2))
        
        # Asymmetric skewing based on dimension index
        skew_term = np.sum(x_scaled * np.exp(-0.5 * np.sum(x_scaled**2)) * 
                          np.sin(4 * np.pi * x_scaled) * 
                          (1 + 0.3 * np.arange(self.dim)))
        
        # Cross-dimensional interaction with varying weights
        cross_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += (x_scaled[i] * x_scaled[j] * 
                              np.sin(6 * np.pi * x_scaled[i]) * 
                              np.cos(3 * np.pi * x_scaled[j]) * 
                              np.exp(-0.1 * (x_scaled[i]**2 + x_scaled[j]**2)))
        
        # Combine all terms with different weights
        return 0.4 * ridge_term + 0.3 * barrier_term + 0.2 * skew_term + 0.1 * cross_term