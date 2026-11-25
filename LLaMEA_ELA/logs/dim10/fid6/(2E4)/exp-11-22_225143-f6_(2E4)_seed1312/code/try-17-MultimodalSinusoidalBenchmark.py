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
            f_val += 1.5 * np.sin(9 * np.pi * x_norm[i]) * np.cos(7 * np.pi * x_norm[i]) * np.sin(5 * np.pi * x_norm[i])
        
        # Add nested periodic interactions with extended interaction scope and stronger coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):  # Full interaction scope
                distance = np.abs(x_norm[i] - x_norm[j])
                f_val += 0.4 * np.sin(20 * np.pi * (x_norm[i] + x_norm[j])) * np.cos(10 * np.pi * (x_norm[i] - x_norm[j])) * np.exp(-3*distance)
        
        # Add highly non-separable high-order terms with increased complexity
        for i in range(self.dim):
            f_val += 0.3 * (np.sin(7 * np.pi * x_norm[i])**4 + np.cos(6 * np.pi * x_norm[i])**4)
        
        # Add global structure with multiple competing minima and enhanced interference
        f_val += 0.4 * np.sum(np.sin(11 * np.pi * x_norm)**2) + 0.2 * np.sum(np.cos(10 * np.pi * x_norm)**2)
        
        # Add stronger chaotic perturbation term for increased complexity
        chaos_term = 0.0
        for i in range(self.dim):
            chaos_term += np.sin(20 * x_norm[i]) * np.cos(18 * x_norm[i]) * np.sin(14 * x_norm[i]) * np.cos(12 * x_norm[i])
        f_val += 0.5 * chaos_term
        
        # Add cross-dimensional coupling with higher-order interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.25 * np.sin(8 * np.pi * (x_norm[i]**2 + x_norm[j]**2)) * np.cos(6 * np.pi * (x_norm[i]*x_norm[j]))
        
        # Add novel hyper-chaotic interaction terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    f_val += 0.15 * np.sin(12 * np.pi * (x_norm[i] + x_norm[j] + x_norm[k])) * np.cos(9 * np.pi * (x_norm[i]**2 - x_norm[j]**2)) * np.exp(-1.5*(np.abs(x_norm[i]-x_norm[j]) + np.abs(x_norm[j]-x_norm[k])))
        
        # Add fractional power interaction for additional complexity
        fractional_term = 0.0
        for i in range(self.dim):
            fractional_term += np.sin(13 * np.pi * x_norm[i])**1.5 + np.cos(11 * np.pi * x_norm[i])**1.5
        f_val += 0.2 * fractional_term
        
        return f_val