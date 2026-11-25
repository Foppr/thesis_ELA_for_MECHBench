import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Radial component with exponential decay and polynomial modulation
        r_squared = np.sum(x_scaled**2)
        radial_term = np.exp(-r_squared / 2.0) * (1.0 + 0.5 * r_squared)
        
        # Chaotic angular components using sine and cosine with varying frequencies
        angular_sum = 0.0
        for i in range(self.dim):
            angle = np.arctan2(x_scaled[i], x_scaled[(i+1) % self.dim]) if self.dim > 1 else 0
            freq = 2.0 + 3.0 * np.sin(i * np.pi / self.dim)
            angular_sum += np.sin(freq * angle) * np.cos(freq * angle)
        
        # Non-separable interaction terms using product of sinusoids
        interaction_terms = []
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction_terms.append(np.sin(x_scaled[i] * x_scaled[j]))
        
        interaction_product = np.prod(interaction_terms) if interaction_terms else 1.0
        
        # Saddle point structure with negative quadratic terms
        quadratic_term = -0.2 * np.sum(x_scaled**4)
        
        # High-frequency chaotic oscillation component
        chaotic_oscillation = np.sum(np.sin(15.0 * x_scaled) * np.cos(13.0 * x_scaled) * np.sin(11.0 * x_scaled))
        
        # Combine all terms with different weights
        result = 2.0 - radial_term + 0.4 * angular_sum + 0.2 * interaction_product + quadratic_term + 0.15 * chaotic_oscillation
        
        return result