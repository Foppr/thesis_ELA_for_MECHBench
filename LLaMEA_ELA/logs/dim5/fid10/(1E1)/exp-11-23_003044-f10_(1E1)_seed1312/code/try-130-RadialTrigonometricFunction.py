import numpy as np

class RadialTrigonometricFunction:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension mismatch")
        
        # Normalize input to [-1, 1] for easier computation
        x_norm = x / 5.0
        
        # Initialize result
        result = 0.0
        
        # Radial basis components with multiple centers
        centers = np.linspace(-1, 1, min(5, self.dim))
        for i in range(self.dim):
            # Create radial basis function with varying width and height
            rbf_value = 0.0
            for j in range(min(3, len(centers))):
                center = centers[j]
                width = 0.5 + 0.5 * np.sin(j)
                height = 1.0 + 0.5 * np.cos(j)
                rbf_value += height * np.exp(-width * (x[i] - center)**2)
            
            result += rbf_value
            
        # Add trigonometric interaction terms between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Create complex interaction pattern
                interaction = np.sin(x[i]) * np.cos(x[j]) + \
                             np.cos(2*x[i]) * np.sin(3*x[j]) + \
                             0.5 * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                result += 0.3 * interaction
                
        # Add a global sinusoidal modulation
        global_mod = np.sin(np.sum(x_norm) * 2)
        result += 2 * global_mod
        
        # Add conditioning term to make optimization harder
        conditioning = 1 + 0.1 * np.sum(np.abs(x_norm)**1.5)
        result *= conditioning
        
        return result