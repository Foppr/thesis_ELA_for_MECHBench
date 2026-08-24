import numpy as np

class ChaoticFractalMultimodal:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        # Normalize input to [-pi, pi] range
        x_norm = (x - self.bounds.lb) * (2 * np.pi) / (self.bounds.ub - self.bounds.lb) - np.pi
        
        # Base chaotic component with nested trigonometric functions
        f = 0.0
        for i in range(self.dim):
            # Nested sine and cosine with varying frequencies
            term1 = np.sin(np.sin(np.cos(x_norm[i]) * x_norm[i]))
            term2 = np.cos(np.cos(np.sin(x_norm[i]) * x_norm[i]))
            f += term1 + term2
            
        # Add fractal-like interaction terms with exponential decay
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited interaction
                # Exponential decay with trigonometric interaction
                decay = np.exp(-0.1 * (i + j))
                interaction = np.sin(x_norm[i] * x_norm[j]) * np.cos(x_norm[i] + x_norm[j])
                f += decay * interaction
                
        # Add chaotic component with polynomial terms
        f += 0.3 * np.sum(np.sin(x_norm)**3 + np.cos(x_norm)**3)
        
        # Add global minimum attraction
        f += 0.1 * np.sum(x**4)
        
        # Add noise-like perturbations for increased complexity
        noise = 0.05 * np.sum(np.sin(10 * x_norm) * np.cos(15 * x_norm))
        f += noise
        
        return f