import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Radial component with exponential decay and additional quadratic term
        r_squared = np.sum(x_scaled**2)
        radial_term = np.exp(-r_squared / 2.0) + 0.3 * (1.0 - r_squared)**2
        
        # Angular components with multiple oscillations and cross-terms
        angular_terms = []
        for i in range(self.dim):
            angle = np.arctan2(x_scaled[i], x_scaled[(i+1) % self.dim]) if self.dim > 1 else 0
            angular_terms.append(np.sin(9.0 * angle) + np.cos(7.0 * angle) + 0.5 * np.sin(3.0 * angle)**2)
        
        # Product of angular terms creates complex interaction with added cross-terms
        angular_product = np.prod(angular_terms) if angular_terms else 1.0
        
        # Additional high-frequency oscillations with cubic nonlinearity and mixed trigonometric terms
        high_freq = np.sum(np.sin(15.0 * x_scaled) * np.cos(11.0 * x_scaled) * x_scaled**3)
        
        # Cross-terms between dimensions to increase conditioning difficulty
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_terms += np.sin(8.0 * x_scaled[i]) * np.cos(6.0 * x_scaled[j])
        
        # Combine all terms with different weights and add a constant offset
        result = 1.5 - radial_term + 0.5 * angular_product + 0.2 * high_freq + 0.1 * cross_terms
        
        return result