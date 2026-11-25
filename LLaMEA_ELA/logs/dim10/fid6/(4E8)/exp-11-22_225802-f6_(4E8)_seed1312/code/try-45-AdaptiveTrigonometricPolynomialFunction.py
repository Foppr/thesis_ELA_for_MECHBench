import numpy as np

class AdaptiveTrigonometricPolynomialFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-pi, pi] for trigonometric stability
        scaled_x = x * (np.pi / 5.0)
        
        # Base polynomial component with mixed degrees
        result = 0.0
        for i in range(self.dim):
            result += 0.5 * (x[i]**4) + 0.3 * (x[i]**3) + 0.1 * (x[i]**2)
            
        # Add trigonometric oscillations with varying frequencies
        for i in range(self.dim):
            result += 0.8 * np.sin(2 * scaled_x[i]) * np.cos(5 * scaled_x[i])
            
        # Include logarithmic barrier terms to create steep gradients near boundaries
        for i in range(self.dim):
            result += 0.2 * (np.log(np.abs(x[i]) + 1e-8) ** 2)
            
        # Add adaptive scaling based on the magnitude of variables
        adaptive_scale = np.mean(np.abs(x)) + 1.0
        
        # Incorporate cross-dimensional interactions with exponential coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.1 * np.exp(-adaptive_scale * np.abs(x[i] - x[j])) * np.sin(3 * (x[i] + x[j]))
                
        # Add a chaotic component with sine-cosine interactions
        for i in range(self.dim):
            result += 0.15 * np.sin(7 * scaled_x[i]) * np.cos(9 * scaled_x[i]) * np.sin(4 * scaled_x[i])
            
        # Include higher-order polynomial terms for conditioning difficulty
        for i in range(self.dim):
            result += 0.05 * (x[i]**6)
            
        # Add a global minimum attraction term
        result += 0.1 * np.sum(x**2) * (1.0 + 0.1 * np.sum(np.abs(x)))
        
        return result