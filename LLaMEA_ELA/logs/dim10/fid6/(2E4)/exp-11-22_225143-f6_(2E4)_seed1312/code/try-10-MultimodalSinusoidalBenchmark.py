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
            f_val += 1.2 * np.sin(7 * np.pi * x_norm[i]) * np.cos(5 * np.pi * x_norm[i]) * np.sin(3 * np.pi * x_norm[i])
        
        # Add nested periodic interactions with extended interaction scope and stronger coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):  # Full interaction scope
                distance = np.abs(x_norm[i] - x_norm[j])
                f_val += 0.3 * np.sin(15 * np.pi * (x_norm[i] + x_norm[j])) * np.cos(8 * np.pi * (x_norm[i] - x_norm[j])) * np.exp(-2*distance)
        
        # Add highly non-separable high-order terms with increased complexity
        for i in range(self.dim):
            f_val += 0.25 * (np.sin(5 * np.pi * x_norm[i])**4 + np.cos(4 * np.pi * x_norm[i])**4)
        
        # Add global structure with multiple competing minima and enhanced interference
        f_val += 0.35 * np.sum(np.sin(9 * np.pi * x_norm)**2) + 0.15 * np.sum(np.cos(8 * np.pi * x_norm)**2)
        
        # Add stronger chaotic perturbation term for increased complexity
        chaos_term = 0.0
        for i in range(self.dim):
            chaos_term += np.sin(17 * x_norm[i]) * np.cos(15 * x_norm[i]) * np.sin(11 * x_norm[i]) * np.cos(9 * x_norm[i])
        f_val += 0.4 * chaos_term
        
        # Add cross-dimensional coupling with higher-order interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.2 * np.sin(6 * np.pi * (x_norm[i]**2 + x_norm[j]**2)) * np.cos(4 * np.pi * (x_norm[i]*x_norm[j]))
        
        return f_val