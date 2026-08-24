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
            for j in range(i+1, min(i+4, self.dim)):  # Reduced interaction range for better control
                # Enhanced exponential decay with trigonometric interaction
                decay = np.exp(-0.12 * (i + j))
                interaction = np.sin(x_norm[i] * x_norm[j]) * np.cos(x_norm[i] + x_norm[j]) + \
                              0.4 * np.sin(x_norm[i] + x_norm[j]) * np.cos(x_norm[i] * x_norm[j])
                f += decay * interaction
                
        # Add chaotic component with polynomial terms
        f += 0.35 * np.sum(np.sin(x_norm)**4 + np.cos(x_norm)**4)
        
        # Add global minimum attraction with modified polynomial
        f += 0.12 * np.sum(x**5)
        
        # Add noise-like perturbations for increased complexity with different frequencies
        noise = 0.06 * np.sum(np.sin(10 * x_norm) * np.cos(15 * x_norm) + 
                              0.25 * np.sin(7 * x_norm) * np.cos(13 * x_norm))
        f += noise
        
        # Add cross-dimensional coupling terms with enhanced complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Introduce more complex coupling with additional trigonometric interactions
                coupling = np.sin(x_norm[i] * x_norm[j] * (i + j)) * np.cos(x_norm[i] + x_norm[j]) + \
                          0.25 * np.cos(x_norm[i] * x_norm[j]) * np.sin(x_norm[i] - x_norm[j])
                f += 0.04 * coupling
                
        # Add higher-order fractal-like terms for increased multimodality
        for i in range(self.dim):
            f += 0.06 * np.sin(3 * x_norm[i]) * np.cos(5 * x_norm[i]) * np.sin(7 * x_norm[i])
            
        # Add a global scaling factor to adjust difficulty
        f *= 1.1
        
        return f