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
            # Enhanced nested sine and cosine with varying frequencies
            term1 = np.sin(np.sin(np.cos(x_norm[i]) * x_norm[i]) * np.sin(x_norm[i]))
            term2 = np.cos(np.cos(np.sin(x_norm[i]) * x_norm[i]) * np.cos(x_norm[i]))
            f += term1 + term2
            
        # Add fractal-like interaction terms with exponential decay
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Increased interaction range
                # Enhanced exponential decay with trigonometric interaction
                decay = np.exp(-0.15 * (i + j))
                interaction = np.sin(x_norm[i] * x_norm[j]) * np.cos(x_norm[i] + x_norm[j]) + \
                              0.5 * np.sin(x_norm[i] + x_norm[j]) * np.cos(x_norm[i] * x_norm[j])
                f += decay * interaction
                
        # Add chaotic component with polynomial terms
        f += 0.4 * np.sum(np.sin(x_norm)**4 + np.cos(x_norm)**4)
        
        # Add global minimum attraction with modified polynomial
        f += 0.15 * np.sum(x**5)
        
        # Add noise-like perturbations for increased complexity with different frequencies
        noise = 0.07 * np.sum(np.sin(12 * x_norm) * np.cos(18 * x_norm) + 
                              0.3 * np.sin(8 * x_norm) * np.cos(14 * x_norm))
        f += noise
        
        # Add cross-dimensional coupling terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f += 0.05 * np.sin(x_norm[i] * x_norm[j] * (i + j)) * np.cos(x_norm[i] + x_norm[j])
                
        return f