import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Radial component with exponential decay and cubic modification
        r_squared = np.sum(x_scaled**2)
        radial_term = np.exp(-r_squared / 2.0) * (1.0 + 0.5 * r_squared**3)
        
        # Angular components with multiple oscillations and higher frequencies
        angular_terms = []
        for i in range(self.dim):
            angle = np.arctan2(x_scaled[i], x_scaled[(i+1) % self.dim]) if self.dim > 1 else 0
            angular_terms.append(np.sin(8.0 * angle) + np.cos(6.0 * angle) + 0.3 * np.sin(12.0 * angle))
        
        # Product of angular terms creates complex interaction with cubic modification
        angular_product = np.prod(angular_terms) if angular_terms else 1.0
        angular_product = angular_product * (1.0 + 0.2 * np.abs(angular_product)**3)
        
        # Additional high-frequency oscillations with cubic nonlinearity
        high_freq = np.sum(np.sin(15.0 * x_scaled) * np.cos(11.0 * x_scaled) * np.tanh(x_scaled))
        
        # Combine all terms with different weights to create challenging landscape
        result = 1.0 - radial_term + 0.4 * angular_product + 0.15 * high_freq
        
        return result