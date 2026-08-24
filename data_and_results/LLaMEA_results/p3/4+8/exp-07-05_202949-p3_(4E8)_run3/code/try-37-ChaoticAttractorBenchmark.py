import numpy as np

class ChaoticAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with conditioning
        f_val = np.sum(x**2)
        
        # Add chaotic attractor components with nested structures
        for i in range(self.dim):
            # Fractional Brownian motion-like irregularities
            f_val += 0.5 * np.sin(10 * x[i]) * np.cos(7 * x[i]) * np.sin(3 * x[i])
            
            # Nested harmonic terms with varying frequencies
            f_val += 0.3 * np.sin(20 * x[i]) * np.cos(15 * x[i]) * np.sin(5 * x[i])
            
            # Dynamic shift based on parity of dimension index
            if i % 2 == 0:
                f_val += 0.2 * np.sin(5 * x[i]) * np.cos(3 * x[i])
            else:
                f_val += 0.2 * np.cos(5 * x[i]) * np.sin(3 * x[i])
        
        # Add fractional polynomial interactions
        f_val += 0.1 * np.sum(np.abs(x)**1.3)
        
        # Add cross-dimensional chaotic coupling
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited range for complexity
                f_val += 0.05 * np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
        
        # Add dynamic global minimum that shifts based on input parity
        shift = np.zeros(self.dim)
        for i in range(self.dim):
            if i % 2 == 0:
                shift[i] = 0.5 * np.sin(x[i])
            else:
                shift[i] = 0.5 * np.cos(x[i])
        
        # Add penalty for deviation from dynamic minimum
        f_val += 0.1 * np.sum((x - shift)**2)
        
        # Add chaotic saddle point structure
        f_val += 0.05 * np.sum(np.sin(x)**3 + np.cos(x)**3)
        
        # Add multi-scale fractal-like structure
        f_val += 0.03 * np.sum(np.sin(2 * x) * np.cos(4 * x) * np.sin(8 * x))
        
        return f_val