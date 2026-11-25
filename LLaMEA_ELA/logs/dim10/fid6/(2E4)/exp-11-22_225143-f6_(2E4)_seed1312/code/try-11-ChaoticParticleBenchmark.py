import numpy as np

class ChaoticParticleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term with conditioning
        f_val = 0.3 * np.sum(x_norm**2)
        
        # Chaotic particle interactions with exponential decay
        for i in range(self.dim):
            f_val += 0.5 * np.exp(-5.0 * np.abs(x_norm[i])) * np.sin(10 * x_norm[i])
        
        # Fractal-like terrain with recursive sine components
        for i in range(self.dim):
            f_val += 0.2 * np.sin(20 * x_norm[i]) * np.cos(15 * x_norm[i]) * np.sin(8 * x_norm[i])
        
        # Dynamic saddle points that depend on all dimensions
        saddle_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                saddle_term += np.sin(x_norm[i] * x_norm[j]) * (x_norm[i]**2 + x_norm[j]**2)
        f_val += 0.4 * saddle_term
        
        # Multi-scale oscillations with varying amplitudes
        for i in range(self.dim):
            f_val += 0.1 * np.sin(50 * x_norm[i]) * np.cos(30 * x_norm[i]) * np.sin(10 * x_norm[i])
        
        # Add a deceptive valley structure around the origin
        f_val += 0.25 * np.sum((x_norm**6) * np.cos(4 * np.pi * x_norm))
        
        return f_val