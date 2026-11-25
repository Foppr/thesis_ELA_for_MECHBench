import numpy as np

class MultimodalSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] 
        x_norm = x / 5.0
        
        # Enhanced polynomial valley component with adaptive exponents
        poly_term = 0
        for i in range(self.dim):
            # Adaptive exponents based on dimension position
            exponent = 2 + (i % 4) * 1.5
            poly_term += (x_norm[i]**exponent) * (1 + 0.4 * np.sin(5 * x_norm[i]) + 0.2 * np.cos(3 * x_norm[i]))
        
        # Modified cosine wave interference with frequency modulation
        cos_term = 0
        for i in range(self.dim):
            # Frequency modulation based on dimension index
            freq1 = 2 + (i % 5) * 0.5
            freq2 = 4 + (i * 3) % 6
            cos_term += np.cos(freq1 * x_norm[i]) * np.sin(freq2 * x_norm[i]) * \
                       (1 + 0.3 * np.sin(2 * x_norm[i]) * np.cos(3 * x_norm[i]))
        
        # Enhanced radial gradient with asymmetric peaks and valleys
        radial_term = 0
        for i in range(self.dim):
            r = np.abs(x_norm[i])
            # More complex radial function with multiple extrema
            radial_term += (r**4 - 3 * r**3 + 2 * r**2) * (1 + 0.5 * np.sin(6 * x_norm[i]) + 0.3 * np.cos(4 * x_norm[i]))
        
        # Increased cross-dimensional coupling with nonlinear interactions
        cross_term = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Extended coupling
                # Nonlinear interaction with dimension-dependent coupling strength
                coupling_strength = 1.5 / (1 + 0.3 * np.abs(i - j) + 0.1 * (i + j))
                cross_term += coupling_strength * (x_norm[i]**2.5) * (x_norm[j]**2.0) * \
                             np.cos(3 * x_norm[i] + 2 * x_norm[j]) * \
                             (1 + 0.2 * np.sin(x_norm[i] * x_norm[j]))
        
        # Additional harmonic component for increased complexity
        harmonic_term = 0
        for i in range(self.dim):
            harmonic_term += np.sin(8 * x_norm[i]) * np.cos(7 * x_norm[i]) * (1 + 0.1 * np.sin(4 * x_norm[i]))
        
        # Combine all components with optimized weights
        result = 1.5 * poly_term + 1.3 * cos_term + 1.2 * radial_term + 0.8 * cross_term + 0.6 * harmonic_term
        
        # Add small random noise for non-determinism
        noise = np.random.normal(0, 0.001)
        
        return result + noise