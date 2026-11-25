import numpy as np

class InterconnectedParabolicLandscape:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension mismatch")
        
        result = 0.0
        
        # Base parabolic terms with varying curvature
        for i in range(self.dim):
            # Create a valley structure with variable depth
            valley_depth = 1.0 + 0.5 * np.sin(i)
            result += valley_depth * (x[i] ** 2) * (1 + 0.3 * np.cos(5 * x[i]))
            
        # Add interaction terms between dimensions to create ridges and valleys
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Create interconnected structures using combined trigonometric functions
                interaction = np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                result += 0.8 * interaction * (1 + 0.2 * np.sin(i + j))
                
        # Add a global modulation term that changes the overall landscape shape
        global_modulation = 1.0 + 0.4 * np.sin(np.sum(x) / self.dim)
        result *= global_modulation
        
        # Add noise-like perturbations to increase complexity
        for i in range(self.dim):
            result += 0.1 * np.sin(7 * x[i]) * np.cos(3 * x[i])
            
        return result