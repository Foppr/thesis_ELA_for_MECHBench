import numpy as np

class MultimodalSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] 
        x_norm = x / 5.0
        
        # Polynomial valley component with varying exponents
        poly_term = 0
        for i in range(self.dim):
            # Create valleys with different curvatures
            exponent = 2 + 2 * (i % 3)  # Exponents: 2, 4, 6, 2, 4, 6...
            poly_term += (x_norm[i]**exponent) * (1 + 0.3 * np.sin(7 * x_norm[i]))
        
        # Cosine wave interference component with varying frequencies
        cos_term = 0
        for i in range(self.dim):
            # Create wave patterns that interfere constructively and destructively
            freq1 = 3 + i % 4
            freq2 = 5 + (i * 2) % 5
            cos_term += np.cos(freq1 * x_norm[i]) * np.sin(freq2 * x_norm[i]) * \
                       (1 + 0.2 * np.cos(4 * x_norm[i]))
        
        # Radial gradient component with asymmetric peaks
        radial_term = 0
        for i in range(self.dim):
            # Radial distance from center with asymmetric behavior
            r = np.abs(x_norm[i])
            radial_term += (r**3 - 2 * r**2 + r) * (1 + 0.4 * np.sin(5 * x_norm[i]))
        
        # Cross-dimensional coupling with polynomial interactions
        cross_term = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited coupling
                # Polynomial interaction between dimensions
                coupling_strength = 1.0 / (1 + 0.2 * np.abs(i - j))
                cross_term += coupling_strength * (x_norm[i]**2) * (x_norm[j]**3) * \
                             np.cos(2 * x_norm[i] + x_norm[j])
        
        # Combine all components with different weights
        result = 1.2 * poly_term + 1.5 * cos_term + 1.0 * radial_term + 0.7 * cross_term
        
        # Add small random noise for non-determinism
        noise = np.random.normal(0, 0.001)
        
        return result + noise