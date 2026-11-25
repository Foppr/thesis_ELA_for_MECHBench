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
        
        # Create radial basis components with varying centers and widths
        centers = np.linspace(-3, 3, min(5, self.dim))
        widths = np.linspace(0.5, 2.0, min(5, self.dim))
        
        for i in range(min(5, self.dim)):
            # Radial basis function component
            rb_value = np.exp(-np.sum((x - centers[i])**2) / (2 * widths[i]**2))
            result += rb_value
            
            # Add trigonometric modulation to create complexity
            result += 0.5 * np.sin(2 * np.pi * x[i]) * np.cos(3 * np.pi * x[i])
            
        # Add interaction terms between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Trigonometric interaction term
                result += 0.3 * np.sin(x[i] * x[j]) * np.cos(0.5 * (x[i] + x[j]))
                
        # Add a global sinusoidal component to increase multimodality
        result += 2 * np.sin(0.5 * np.sum(x_norm**2)) * np.cos(0.3 * np.sum(x_norm))
        
        # Add conditioning to make optimization harder
        conditioning = 1 + 0.1 * np.sum(np.abs(x_norm))
        result = result * conditioning
        
        return result