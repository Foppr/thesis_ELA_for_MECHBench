import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.gaussian_scale = 1.0
        self.barrier_strength = 2.0
        self.coupling_freq = 1.5
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Gaussian radial basis function component
        gaussian_term = 0.0
        for i in range(self.dim):
            gaussian_term += np.exp(-self.gaussian_scale * (x[i]**2))
            
        # Logarithmic barrier terms to enforce boundaries
        barrier_term = 0.0
        for i in range(self.dim):
            barrier_term += self.barrier_strength * (np.log(25.0 - x[i]**2) + np.log(25.0 - x[i]**2))
            
        # Sinusoidal coupling between dimensions
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_term += np.sin(self.coupling_freq * x[i] * x[j]) * (1 + 0.2 * np.sin(i + j))
                
        # Adaptive conditioning with dimension-dependent scaling
        condition_term = 0.0
        for i in range(self.dim):
            adaptive_scale = 1.0 + 0.5 * np.sin(0.3 * i)
            condition_term += adaptive_scale * (x[i]**4 + x[i]**2)
            
        # Cross-dimensional polynomial interaction
        poly_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_interaction += (x[i]**3) * (x[j]**2) * np.cos(0.5 * (x[i] + x[j]))
                
        # Global modulation based on sum of variables
        global_mod = 1.0 + 0.3 * np.sin(np.sum(x) * 0.2)
        
        return global_mod * (gaussian_term + 0.3 * barrier_term + 0.4 * coupling_term + 
                            0.25 * condition_term + 0.35 * poly_interaction)