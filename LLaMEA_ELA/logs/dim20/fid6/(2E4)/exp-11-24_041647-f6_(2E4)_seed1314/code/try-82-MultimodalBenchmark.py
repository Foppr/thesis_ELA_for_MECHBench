import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Polynomial chaos expansion with dynamic exponents and mixed terms
        poly_term = 0.0
        for i in range(self.dim):
            exponent = 2 + 0.5 * np.sin(i * 0.8) + 0.3 * np.cos(i * 0.6)
            poly_term += (x_normalized[i] ** exponent) * (1.0 + 0.2 * np.sin(5 * x_normalized[i]))
        
        # Radial basis function with adaptive width and multi-scale peaks
        radial_term = 0.0
        for i in range(self.dim):
            width = 0.5 + 0.3 * np.sin(i * 0.4)
            peak_height = 1.5 + 0.5 * np.cos(i * 0.7)
            radial_term += peak_height * np.exp(-0.5 * (x_normalized[i] / width) ** 2)
        
        # Dynamic coupling terms with varying interaction strengths
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                strength = 0.8 + 0.4 * np.sin(0.5 * (i + j)) * np.cos(0.3 * (i - j))
                coupling_term += strength * np.sin(15 * x_normalized[i] * x_normalized[j]) * np.cos(12 * x_normalized[i] + 8 * x_normalized[j])
        
        # Adaptive sinusoidal modulation with frequency scaling and phase shifts
        modulated_term = 0.0
        for i in range(self.dim):
            freq_scale = 1.0 + 0.3 * np.sin(i * 0.9)
            phase_shift = 0.2 * np.cos(i * 0.5)
            modulated_term += np.sin(freq_scale * x_normalized[i] + phase_shift) * np.cos(freq_scale * x_normalized[i] * 0.7)
        
        # Fractional dimensionality effect with weighted contributions
        fractional_term = 0.0
        for i in range(self.dim):
            weight = (i + 1) / self.dim
            fractional_term += weight * np.tan(0.5 * x_normalized[i]) ** 2
        
        # Combined landscape with adaptive weighting based on dimensionality
        total = (0.3 * poly_term + 
                0.25 * radial_term + 
                0.2 * coupling_term + 
                0.15 * modulated_term + 
                0.1 * fractional_term)
        
        # Add noise component for increased complexity
        noise = 0.02 * np.random.rand()
        
        return total + noise