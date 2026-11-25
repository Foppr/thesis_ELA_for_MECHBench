import numpy as np

class HybridDeceptiveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Spherical component for global basin attraction
        spherical = np.sum(x_norm**2)
        
        # Elliptic component with varying condition numbers
        elliptic = np.sum((x_norm**2) * (2**(np.arange(self.dim) / (self.dim - 1))))
        
        # Deceptive component with multiple local optima
        deceptive = np.sum(np.sin(10 * np.pi * x_norm) * np.cos(5 * np.pi * x_norm))
        
        # Dynamic noise injection based on position
        noise = np.sum(0.1 * np.sin(20 * x_norm) * np.random.uniform(0.8, 1.2, self.dim))
        
        # Cross-dimensional interaction with varying coupling strength
        cross_dim = np.sum(np.abs(x_norm[:-1] - x_norm[1:]) * (1 + 0.5 * np.sin(3 * x_norm[:-1])))
        
        # Asymmetric landscape with different curvature in positive and negative directions
        asymmetric = np.sum(np.where(x_norm > 0, x_norm**1.5, -x_norm**1.7))
        
        # Multi-scale periodic modulation
        periodic_modulation = np.sum(np.sin(8 * x_norm) * np.cos(6 * x_norm) * 
                                    (1 + 0.3 * np.sin(4 * x_norm)))
        
        # Combined function with adaptive weights
        return 0.5 * spherical + 0.3 * elliptic + 0.2 * deceptive + 0.1 * noise + \
               0.15 * cross_dim + 0.25 * asymmetric + 0.1 * periodic_modulation