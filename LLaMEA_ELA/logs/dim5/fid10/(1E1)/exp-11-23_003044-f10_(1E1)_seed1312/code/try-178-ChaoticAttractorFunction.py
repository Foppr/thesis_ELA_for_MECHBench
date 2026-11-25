import numpy as np

class ChaoticAttractorFunction:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension mismatch")
        
        # Normalize input to [-1, 1] for easier computation
        x_norm = x / 5.0
        
        # Initialize chaotic system parameters
        a, b, c = 3.9, 0.1, 0.2
        result = 0.0
        
        # Create a chaotic landscape using a modified logistic map
        for i in range(self.dim):
            # Base chaotic term with sensitive dependence
            xi = x[i]
            chaotic_term = 0.0
            
            # Simulate chaotic dynamics for multiple steps
            for _ in range(10):
                chaotic_term = a * xi * (1 - xi)
                xi = chaotic_term
                
            # Add interaction between dimensions using a modified Henon map
            if i > 0:
                xi_prev = x[i-1]
                henon_x = 1.4 - a * xi_prev**2 + b * xi
                henon_y = c * xi_prev
                result += 0.5 * (henon_x**2 + henon_y**2)
            
            # Add sinusoidal modulation to create multiple local minima
            result += 2 * np.sin(5 * xi) * np.cos(3 * xi) + 0.1 * xi**4
            
        # Add a conditioning term that makes the landscape more challenging
        conditioning = 1.0 + 0.5 * np.sum(np.abs(x_norm))
        result = result * conditioning
        
        return result