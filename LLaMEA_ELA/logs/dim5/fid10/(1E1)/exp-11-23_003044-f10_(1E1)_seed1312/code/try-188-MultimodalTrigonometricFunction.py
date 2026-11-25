import numpy as np

class MultimodalTrigonometricFunction:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension mismatch")
        
        # Normalize input to [-1, 1] for easier computation
        x_norm = x / 5.0
        
        # Base polynomial term with sinusoidal modulation
        result = 0.0
        for i in range(self.dim):
            # Quadratic base with sinusoidal perturbation
            result += x[i]**2 * (1 + 0.3 * np.sin(5 * x[i]))
            
            # Add higher frequency trigonometric components
            result += 0.5 * np.cos(7 * x[i]) * np.sin(4 * x[i])
            
            # Add interaction terms between dimensions with trigonometric modulation
            for j in range(i+1, self.dim):
                interaction = np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
                result += 0.2 * interaction
                
        # Add a global conditioning term that increases complexity with dimensionality
        condition_factor = 1.0 + 0.2 * np.sum(np.abs(x_norm))
        
        # Add a central peak to create multiple local optima
        central_peak = 2.0 * np.exp(-np.sum(x**2) / (2 * 0.5**2))
        result += central_peak
        
        return result * condition_factor