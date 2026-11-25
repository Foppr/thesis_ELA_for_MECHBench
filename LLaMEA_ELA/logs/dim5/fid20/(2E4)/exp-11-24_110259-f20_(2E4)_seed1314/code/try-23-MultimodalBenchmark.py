import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Radial component with exponential decay and additional quadratic term
        r_squared = np.sum(x_scaled**2)
        radial_term = np.exp(-r_squared / 2.0) + 0.3 * r_squared
        
        # Angular components with multiple oscillations and increased frequency
        angular_terms = []
        for i in range(self.dim):
            angle = np.arctan2(x_scaled[i], x_scaled[(i+1) % self.dim]) if self.dim > 1 else 0
            angular_terms.append(np.sin(9.0 * angle) + np.cos(7.0 * angle) + 0.5 * np.sin(13.0 * angle))
        
        # Product of angular terms creates complex interaction with added cubic term
        angular_product = np.prod(angular_terms) if angular_terms else 1.0
        angular_cubic = 0.2 * np.sum(np.array(angular_terms)**3)
        
        # Additional high-frequency oscillations with cubic nonlinearity and sinusoidal modulation
        high_freq = np.sum((np.sin(15.0 * x_scaled) * np.cos(11.0 * x_scaled) + 
                           0.3 * x_scaled**3) * np.exp(-r_squared / 3.0))
        
        # Combine all terms with different weights
        result = 1.5 - radial_term + 0.5 * angular_product + 0.2 * angular_cubic + 0.2 * high_freq
        
        return result