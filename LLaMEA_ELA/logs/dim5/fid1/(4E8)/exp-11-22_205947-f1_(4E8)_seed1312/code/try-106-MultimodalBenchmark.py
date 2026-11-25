import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial conditioning with chaotic exponents
        exponents = np.linspace(2, 6, self.dim)
        poly_term = np.sum((x ** exponents) * (1 + 0.1 * np.sin(x * 2)))
        
        # Fractal-like radial sinusoidal component with chaotic frequencies
        radial_sine = 0.0
        for i in range(self.dim):
            freq1 = 2.0 + 0.5 * np.sin(i * 0.7)
            freq2 = 3.0 + 0.3 * np.cos(i * 0.9)
            freq3 = 5.0 + 0.4 * np.sin(i * 1.1)
            radial_sine += np.sin(freq1 * x[i]) * np.cos(freq2 * x[i]) + \
                          np.sin(freq3 * x[i]) * np.cos(freq1 * x[i]) + \
                          np.sin(freq2 * x[i]) * np.cos(freq3 * x[i])
        
        # Multi-scale radial basis with chaotic widths and offsets
        rbfs = 0.0
        for i in range(self.dim):
            width = 0.5 + 0.8 * np.abs(np.sin(i * 0.4 + 1.0))
            offset = 3.0 * np.cos(i * 0.6 + 0.5)
            rbfs += np.exp(-0.5 * ((x[i] - offset) / width) ** 2)
        
        # Cross-dimensional coupling with chaotic interactions
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):
                freq_i = 1.0 + 0.3 * np.sin(i * 0.8)
                freq_j = 1.5 + 0.2 * np.cos(j * 0.6)
                cross_coupling += np.sin(freq_i * x[i] + freq_j * x[j]) * \
                                 np.cos(freq_i * (x[i] - x[j]) + freq_j * (x[i] + x[j]))
        
        # Adaptive conditioning with chaotic modulation
        condition_factor = 1.0 + 0.3 * np.log(self.dim + 1) + 0.2 * np.sin(self.dim * 0.8 + 1.0)
        
        # Final combination with enhanced scaling and modulation
        return condition_factor * (poly_term + 0.4 * radial_sine + 0.25 * rbfs + 0.2 * cross_coupling)