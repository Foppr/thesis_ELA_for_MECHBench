import numpy as np

class ChaoticFractalMultimodal:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        # Normalize input to [-pi, pi] range
        x_norm = (x - self.bounds.lb) * (2 * np.pi) / (self.bounds.ub - self.bounds.lb) - np.pi
        
        # Base chaotic component with deeply nested trigonometric functions
        f = 0.0
        for i in range(self.dim):
            # Deeply nested sine and cosine with varying frequencies and powers
            term1 = np.sin(np.sin(np.cos(np.sin(x_norm[i]) * x_norm[i]) * x_norm[i]) * np.sin(x_norm[i]))
            term2 = np.cos(np.cos(np.sin(np.cos(x_norm[i]) * x_norm[i]) * x_norm[i]) * np.cos(x_norm[i]))
            f += term1 + term2
            
        # Add fractal-like interaction terms with enhanced exponential decay and higher-order interactions
        for i in range(self.dim):
            for j in range(i+1, min(i+7, self.dim)):  # Extended interaction range
                # Enhanced exponential decay with trigonometric interaction and polynomial coupling
                decay = np.exp(-0.2 * (i + j) ** 1.5)
                interaction = (np.sin(x_norm[i] * x_norm[j]) * np.cos(x_norm[i] + x_norm[j]) + 
                              0.5 * np.sin(x_norm[i] + x_norm[j]) * np.cos(x_norm[i] * x_norm[j]) +
                              0.3 * np.sin(x_norm[i] ** 2 * x_norm[j]) * np.cos(x_norm[i] * x_norm[j] ** 2))
                f += decay * interaction
                
        # Add chaotic component with higher-order polynomial terms
        f += 0.5 * np.sum(np.sin(x_norm)**6 + np.cos(x_norm)**6)
        
        # Add global minimum attraction with modified polynomial of higher degree
        f += 0.2 * np.sum(x**7)
        
        # Add noise-like perturbations with increased complexity and multiple frequencies
        noise = 0.1 * np.sum(np.sin(15 * x_norm) * np.cos(20 * x_norm) + 
                            0.4 * np.sin(10 * x_norm) * np.cos(16 * x_norm) +
                            0.2 * np.sin(12 * x_norm) * np.cos(18 * x_norm))
        f += noise
        
        # Add cross-dimensional coupling terms with enhanced interaction
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f += 0.08 * np.sin(x_norm[i] * x_norm[j] * (i + j) ** 1.2) * np.cos(x_norm[i] + x_norm[j] ** 1.5)
                
        # Add higher-order coupling between groups of variables
        for i in range(0, self.dim, 3):
            if i + 2 < self.dim:
                f += 0.03 * np.sin(x_norm[i] * x_norm[i+1] * x_norm[i+2]) * np.cos(x_norm[i] + x_norm[i+1] + x_norm[i+2])
                
        return f