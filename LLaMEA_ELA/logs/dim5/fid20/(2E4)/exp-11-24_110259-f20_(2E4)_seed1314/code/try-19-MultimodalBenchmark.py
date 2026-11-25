import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Radial component with gaussian ridges and cubic modulation
        r_squared = np.sum(x_scaled**2)
        radial_term = np.exp(-r_squared / 2.0) * (1.0 + 0.3 * r_squared**3 + 0.2 * np.sin(7.0 * r_squared))
        
        # Chaotic angular interactions with perturbed trigonometric terms
        angular_terms = []
        for i in range(self.dim):
            angle = np.arctan2(x_scaled[i], x_scaled[(i+1) % self.dim]) if self.dim > 1 else 0
            # Add chaotic modulation to angles
            chaotic_mod = 1.0 + 0.3 * np.sin(13.0 * angle) * np.cos(11.0 * angle)
            angular_terms.append(np.sin(9.0 * angle) * chaotic_mod + np.cos(7.0 * angle) * chaotic_mod)
        
        # Product of angular terms creates complex interaction
        angular_product = np.prod(angular_terms) if angular_terms else 1.0
        
        # Saddle-point perturbations with multiple Gaussian hills
        saddle_terms = []
        for i in range(self.dim):
            gauss_val = np.exp(-((x_scaled[i] - 0.5)**2 + (x_scaled[(i+1) % self.dim] + 0.3)**2) / 0.5)
            saddle_terms.append(gauss_val)
        
        saddle_term = np.sum(saddle_terms) if saddle_terms else 0.0
        
        # High-frequency oscillations with asymmetric cubic modulation
        high_freq = np.sum((np.sin(15.0 * x_scaled) * np.cos(13.0 * x_scaled)) ** 4)
        
        # Combine all terms with different weights and add noise
        result = 1.0 - radial_term + 0.5 * angular_product + 0.2 * saddle_term + 0.1 * high_freq
        
        return result