import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Chaotic sine wave components with varying frequencies and amplitudes
        chaotic = 0.0
        for i in range(self.dim):
            freq = 2 * np.pi * (i + 1) * (1.0 + 0.3 * np.sin(i * np.pi / 4))
            amp = 1.0 / (1.0 + 0.1 * i)
            chaotic += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i])
        
        # Radial basis function components with adaptive centers and widths
        rbf = 0.0
        for i in range(self.dim):
            center = np.sin(i * np.pi / 3)
            width = 0.5 + 0.5 * np.cos(i * np.pi / 4)
            rbf += np.exp(-0.5 * ((x_scaled[i] - center) / width)**2)
        
        # Adaptive conditioning based on dimensionality and distance
        dist_from_origin = np.sqrt(np.sum(x_scaled**2))
        condition_factor = 1.0 + 0.5 * (self.dim - 1) * np.tanh(dist_from_origin)
        
        # Cross-terms with chaotic coupling coefficients
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin((i + j) * np.pi / 6) * np.cos((i - j) * np.pi / 8)
                cross_terms += coupling * x_scaled[i] * x_scaled[j] * np.exp(-0.5 * (x_scaled[i]**2 + x_scaled[j]**2))
        
        # Polynomial shaping with mixed degrees
        poly_shaping = np.sum(x_scaled**2 + 0.3 * x_scaled**4 + 0.1 * x_scaled**6)
        
        # Global minimum at origin with additional penalty for distance
        penalty = 0.5 * dist_from_origin**2
        
        # Combine all components with optimized weights
        return 1.5 * chaotic + 2.0 * rbf + condition_factor * cross_terms + 0.8 * poly_shaping + penalty