import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos expansion with mixed powers and interaction terms
        chaos_term = np.sum(0.5 * x**4 + 0.3 * x**3.2 - 0.8 * x**2.5 + 0.1 * x**1.8 + 0.05 * x**0.9)
        
        # Implicit constraint-based ruggedness with sine and cosine interactions
        constraint_term = np.sum(np.sin(np.pi * x) * np.cos(np.pi * x) * 
                                (1 + 0.1 * np.sin(3 * np.pi * x) * np.cos(2 * np.pi * x)))
        
        # Adaptive coupling with dimension-dependent weights
        adaptive_coupling = 0
        for i in range(self.dim - 1):
            weight = 0.5 + 0.5 * np.sin(np.pi * (i + 1) / self.dim)
            adaptive_coupling += weight * (x[i]**2 + x[i+1]**2) * np.sin(np.pi * (x[i] + x[i+1]))
        
        # Fractional Brownian motion inspired term with long-range dependence
        fbm_term = np.sum(0.2 * np.sin(2 * np.pi * x) * np.cos(1.5 * np.pi * x) * 
                         np.exp(-0.1 * np.abs(x)) * np.log(1 + np.abs(x)))
        
        # Multi-scale oscillatory component with varying frequencies
        multiscale_term = np.sum(np.sin(5 * x) * np.cos(3 * x) * 
                                np.exp(-0.05 * x**2) * (1 + 0.2 * np.sin(7 * x)))
        
        # Combine all terms with optimized weights
        return 0.3 * chaos_term + 0.25 * constraint_term + 0.2 * adaptive_coupling + 0.15 * fbm_term + 0.1 * multiscale_term + 1.5