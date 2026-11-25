import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Radial component with enhanced exponential decay and modified quadratic term
        r_squared = np.sum(x_scaled**2)
        radial_term = np.exp(-r_squared) + 0.3 * r_squared**2
        
        # Angular components with adjusted oscillations and phase shifts
        angular_terms = []
        for i in range(self.dim):
            angle = np.arctan2(x_scaled[i], x_scaled[(i+1) % self.dim]) if self.dim > 1 else 0
            angular_terms.append(np.sin(10.0 * angle + i * np.pi/5) + np.cos(7.0 * angle + i * np.pi/4))
        
        # Product of angular terms with modified modulation
        angular_product = np.prod(angular_terms) if angular_terms else 1.0
        angular_modulation = 0.6 * (1.0 + np.sin(4.0 * r_squared))
        
        # Additional high-frequency oscillations with adjusted cubic nonlinearity and cross-terms
        high_freq = np.sum(np.sin(20.0 * x_scaled) * np.cos(15.0 * x_scaled) + 0.4 * x_scaled**3)
        cross_terms = np.sum(x_scaled[:-1] * x_scaled[1:] * np.sin(6.0 * x_scaled[:-1]))
        
        # Combine all terms with refined weights and improved conditioning factor
        conditioning_factor = 1.0 + 0.15 * np.sin(3.0 * r_squared)
        result = conditioning_factor * (1.0 - radial_term + 0.6 * angular_product * angular_modulation + 0.25 * high_freq + 0.15 * cross_terms)
        
        return result