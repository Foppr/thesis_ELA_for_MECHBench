import numpy as np

class AdaptiveOscillatoryMultimodal:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        # Normalize input to [-pi, pi] range
        x_norm = (x - self.bounds.lb) * (2 * np.pi) / (self.bounds.ub - self.bounds.lb) - np.pi
        
        # Base polynomial and trigonometric components
        f = 0.0
        for i in range(self.dim):
            f += (x[i]**4 - 2 * x[i]**2 + 1) * np.sin(3 * x_norm[i]) + \
                 (x[i]**3 - x[i]) * np.cos(2 * x_norm[i])
        
        # Add multi-scale periodic interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Adaptive coupling with varying frequencies
                freq_i = 1.0 + 0.5 * np.sin(i)
                freq_j = 1.0 + 0.5 * np.cos(j)
                coupling = np.sin(freq_i * x_norm[i] + freq_j * x_norm[j]) * \
                           np.cos(freq_i * x_norm[i] - freq_j * x_norm[j])
                f += 0.2 * coupling * (1 + 0.1 * (i + j))
                
        # Introduce saddle point structure with hyperbolic terms
        for i in range(self.dim):
            f += 0.1 * np.tanh(x[i]) * np.sinh(x[i]) * np.cos(x[i])
            
        # Add fractal-like complexity through recursive polynomial terms
        for i in range(self.dim):
            f += 0.05 * (x[i]**6 + x[i]**5 + x[i]**4 + x[i]**3 + x[i]**2 + x[i])
            
        # Include gradient complexity with directional scaling
        scale_factor = 1.0 + 0.2 * np.sin(np.sum(x_norm) / self.dim)
        f *= scale_factor
        
        # Add noise-like perturbations for increased robustness
        noise = 0.03 * np.sum(np.sin(10 * x_norm) + np.cos(15 * x_norm))
        f += noise
        
        # Add global minimum attraction with polynomial scaling
        f += 0.1 * np.sum(x**6)
        
        return f