import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial conditioning with varying exponents and adaptive weights
        poly_weights = 1.0 + 0.3 * np.sin(np.arange(self.dim) * 0.7)
        poly_term = np.sum(poly_weights * (x ** 2) + 0.15 * (x ** 3) + 0.02 * (x ** 4))
        
        # Radial sinusoidal component with chaotic frequency modulation
        radial_sine = 0.0
        for i in range(self.dim):
            freq1 = 2.0 + 0.5 * np.sin(i * 0.3)
            freq2 = 3.0 + 0.3 * np.cos(i * 0.4)
            freq3 = 5.0 + 0.7 * np.sin(i * 0.6)
            radial_sine += np.sin(freq1 * x[i]) * np.cos(freq2 * x[i]) + \
                          np.sin(freq3 * x[i]) * np.cos(freq3 * x[i] + 1.0) + \
                          np.sin(7.0 * x[i]) * np.cos(11.0 * x[i])
        
        # Multi-scale radial basis with chaotic widths and offsets
        rbfs = 0.0
        for i in range(self.dim):
            width = 0.5 + 0.8 * np.abs(np.sin(i * 0.4 + 1.0))
            offset = 3.0 * np.cos(i * 0.5 + 0.5)
            rbfs += np.exp(-0.5 * ((x[i] - offset) / width) ** 2)
        
        # Cross-dimensional coupling with chaotic interactions
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                coupling_freq = 1.0 + 0.2 * np.sin(i * 0.3 + j * 0.4)
                cross_coupling += np.sin(coupling_freq * (x[i] + x[j])) * np.cos(2.0 * coupling_freq * (x[i] - x[j]))
        
        # Adaptive conditioning with chaotic modulation
        condition_factor = 1.5 + 0.5 * np.sin(self.dim * 0.3) + 0.3 * np.cos(self.dim * 0.7)
        
        # Final combination with enhanced scaling and modulation
        return condition_factor * (poly_term + 0.4 * radial_sine + 0.25 * rbfs + 0.2 * cross_coupling)