import numpy as np

class AdaptiveOscillatoryMultimodal:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        # Normalize input to [-pi, pi] range
        x_norm = (x - self.bounds.lb) * (2 * np.pi) / (self.bounds.ub - self.bounds.lb) - np.pi
        
        # Base polynomial and trigonometric components with modified exponents
        f = 0.0
        for i in range(self.dim):
            f += (x[i]**5 - 2 * x[i]**3 + x[i]) * np.sin(2 * x_norm[i]) + \
                 (x[i]**4 - x[i]**2) * np.cos(3 * x_norm[i])
        
        # Add multi-scale periodic interactions with stronger coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Enhanced adaptive coupling with frequency modulation
                freq_i = 1.5 + 0.8 * np.sin(i * 0.5)
                freq_j = 1.5 + 0.8 * np.cos(j * 0.5)
                coupling = np.sin(freq_i * x_norm[i] + freq_j * x_norm[j]) * \
                           np.cos(freq_i * x_norm[i] - freq_j * x_norm[j])
                f += 0.3 * coupling * (1 + 0.2 * (i + j))
                
        # Enhanced saddle point structure with hyperbolic terms
        for i in range(self.dim):
            f += 0.15 * np.tanh(x[i]) * np.sinh(x[i]) * np.cos(1.5 * x[i])
            
        # Modified fractal-like complexity through recursive polynomial terms
        for i in range(self.dim):
            f += 0.08 * (x[i]**7 + x[i]**6 + x[i]**5 + x[i]**4 + x[i]**3 + x[i]**2 + x[i])
            
        # Increased gradient complexity with directional scaling
        scale_factor = 1.0 + 0.3 * np.sin(np.sum(x_norm) / self.dim)
        f *= scale_factor
        
        # Enhanced noise-like perturbations
        noise = 0.05 * np.sum(np.sin(12 * x_norm) + np.cos(18 * x_norm))
        f += noise
        
        # Strengthened global minimum attraction
        f += 0.15 * np.sum(x**7)
        
        return f