import numpy as np

class MultimodalSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range for consistency
        x_norm = x / 5.0
        
        # Base quadratic term with strong conditioning and interaction
        f_val = np.sum(x_norm**2) * (1.0 + 0.2 * np.sum(np.abs(x_norm)))
        
        # Enhanced chaotic sinusoidal modulations with higher frequencies and stronger coupling
        for i in range(self.dim):
            f_val += 1.5 * np.sin(9 * np.pi * x_norm[i]) * np.cos(7 * np.pi * x_norm[i]) * np.sin(5 * np.pi * x_norm[i])
        
        # Extended interaction scope with stronger coupling and exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):  # Full interaction scope
                distance = np.abs(x_norm[i] - x_norm[j])
                f_val += 0.4 * np.sin(18 * np.pi * (x_norm[i] + x_norm[j])) * np.cos(12 * np.pi * (x_norm[i] - x_norm[j])) * np.exp(-3*distance)
        
        # Increased non-separability through higher-order terms and nested patterns
        for i in range(self.dim):
            f_val += 0.35 * (np.sin(7 * np.pi * x_norm[i])**4 + np.cos(6 * np.pi * x_norm[i])**4)
        
        # Enhanced global structure with multiple competing minima and interference
        f_val += 0.45 * np.sum(np.sin(11 * np.pi * x_norm)**2) + 0.25 * np.sum(np.cos(10 * np.pi * x_norm)**2)
        
        # Stronger chaotic perturbation with more complex interaction patterns
        chaos_term = 0.0
        for i in range(self.dim):
            chaos_term += np.sin(21 * x_norm[i]) * np.cos(19 * x_norm[i]) * np.sin(17 * x_norm[i]) * np.cos(15 * x_norm[i])
        f_val += 0.5 * chaos_term
        
        # Cross-dimensional coupling with higher-order interactions and stronger interference
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.3 * np.sin(8 * np.pi * (x_norm[i]**2 + x_norm[j]**2)) * np.cos(6 * np.pi * (x_norm[i]*x_norm[j])) * np.exp(-1.5*distance)
        
        # Additional high-order non-separable terms for increased complexity
        for i in range(self.dim):
            f_val += 0.2 * np.sin(13 * np.pi * x_norm[i])**3 * np.cos(11 * np.pi * x_norm[i])**3
        
        return f_val