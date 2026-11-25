import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Radial component with enhanced exponential decay and plateau
        r_squared = np.sum(x_scaled**2)
        radial_term = np.exp(-r_squared / 1.5) * (1.0 + 0.5 * np.exp(-r_squared / 0.5))
        
        # Angular components with multiple high-frequency oscillations
        angular_terms = []
        for i in range(self.dim):
            angle = np.arctan2(x_scaled[i], x_scaled[(i+1) % self.dim]) if self.dim > 1 else 0
            angular_terms.append(np.sin(9.5 * angle) + np.cos(7.5 * angle) + 0.5 * np.sin(13.5 * angle))
        
        # Product of angular terms creates complex interaction with added cubic term
        angular_product = np.prod(angular_terms) if angular_terms else 1.0
        
        # Additional high-frequency oscillations with cubic nonlinearity and cross-terms
        high_freq = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                high_freq += np.sin(15.5 * x_scaled[i]) * np.cos(11.5 * x_scaled[j]) * x_scaled[i]**3 * x_scaled[j]**2
        
        # Cross-dimensional interaction terms with modified frequencies
        cross_terms = 0.0
        for i in range(self.dim):
            cross_terms += np.sin(8.5 * x_scaled[i]) * np.cos(6.5 * x_scaled[(i+2) % self.dim])
        
        # Combine all terms with different weights and add noise component
        result = 1.5 - radial_term + 0.6 * angular_product + 0.2 * high_freq + 0.1 * cross_terms
        
        return result