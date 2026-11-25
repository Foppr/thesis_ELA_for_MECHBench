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
            exponent = 2 + 3 * (i % 4)  # Exponents: 2, 5, 8, 11, 2, 5...
            poly_term += (x_norm[i]**exponent) * (1 + 0.4 * np.sin(5 * x_norm[i]) + 0.2 * np.cos(3 * x_norm[i]))
        
        # Modified cosine wave interference with phase shifts
        cos_term = 0
        for i in range(self.dim):
            freq1 = 2 + (i % 5)
            freq2 = 4 + ((i * 3) % 6)
            phase_shift = np.pi * (i % 3) / 3
            cos_term += np.cos(freq1 * x_norm[i] + phase_shift) * np.sin(freq2 * x_norm[i] + phase_shift) * \
                       (1 + 0.3 * np.sin(3 * x_norm[i]) * np.cos(2 * x_norm[i]))
        
        # Enhanced radial gradient component with multiple peaks
        radial_term = 0
        for i in range(self.dim):
            r = np.abs(x_norm[i])
            radial_term += (r**4 - 3 * r**3 + 2 * r**2) * (1 + 0.5 * np.sin(7 * x_norm[i]) + 0.3 * np.cos(4 * x_norm[i]))
        
        # Increased cross-dimensional coupling with trigonometric interactions
        cross_term = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Extended coupling
                coupling_strength = 1.5 / (1 + 0.3 * np.abs(i - j))
                interaction = np.sin(x_norm[i] + x_norm[j]) * np.cos(x_norm[i] - x_norm[j])
                cross_term += coupling_strength * (x_norm[i]**2) * (x_norm[j]**2) * interaction
        
        # Additional harmonic component for increased complexity
        harmonic_term = 0
        for i in range(self.dim):
            harmonic_term += np.sin(2 * x_norm[i]) * np.cos(3 * x_norm[i]) * (1 + 0.25 * np.sin(4 * x_norm[i]))
        
        # Combine all components with optimized weights
        result = 1.5 * poly_term + 1.8 * cos_term + 1.2 * radial_term + 1.0 * cross_term + 0.8 * harmonic_term
        
        # Add small random noise for non-determinism
        noise = np.random.normal(0, 0.001)
        
        return result + noise