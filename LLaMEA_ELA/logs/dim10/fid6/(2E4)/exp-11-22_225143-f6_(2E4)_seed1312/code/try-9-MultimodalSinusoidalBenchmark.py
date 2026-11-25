import numpy as np

class MultimodalSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range for consistency
        x_norm = x / 5.0
        
        # Base quadratic term with condition number variation
        f_val = np.sum(x_norm**2) * (1.0 + 0.1 * np.sum(np.abs(x_norm)))
        
        # Add chaotic sinusoidal modulations with varying frequencies
        for i in range(self.dim):
            f_val += 0.8 * np.sin(5 * np.pi * x_norm[i]) * np.cos(3 * np.pi * x_norm[i]) * np.sin(2 * np.pi * x_norm[i])
        
        # Add nested periodic interactions with exponential decay
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited interaction scope
                distance = np.abs(x_norm[i] - x_norm[j])
                f_val += 0.2 * np.sin(10 * np.pi * (x_norm[i] + x_norm[j])) * np.cos(5 * np.pi * (x_norm[i] - x_norm[j])) * np.exp(-distance)
        
        # Add highly non-separable high-order terms
        for i in range(self.dim):
            f_val += 0.15 * (np.sin(4 * np.pi * x_norm[i])**4 + np.cos(3 * np.pi * x_norm[i])**4)
        
        # Add global structure with multiple competing minima
        f_val += 0.25 * np.sum(np.sin(7 * np.pi * x_norm)**2) + 0.1 * np.sum(np.cos(6 * np.pi * x_norm)**2)
        
        # Add chaotic perturbation term for increased complexity
        chaos_term = 0.0
        for i in range(self.dim):
            chaos_term += np.sin(13 * x_norm[i]) * np.cos(11 * x_norm[i]) * np.sin(7 * x_norm[i])
        f_val += 0.3 * chaos_term
        
        return f_val