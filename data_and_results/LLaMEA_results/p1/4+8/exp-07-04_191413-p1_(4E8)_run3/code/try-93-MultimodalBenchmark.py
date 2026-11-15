import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quadratic conditioning term
        quadratic = np.sum(x_norm**2)
        
        # Multiple Gaussian peaks with varying heights and widths
        peaks = 0.0
        for i in range(1, 6):
            # Varying peak positions and widths
            peak_pos = np.sin(i * np.pi / 6) * np.ones(self.dim)
            peak_width = 0.5 + 0.5 * np.cos(i * np.pi / 4)
            peak_height = 1.0 + 0.5 * np.sin(i * np.pi / 3)
            
            # Gaussian peak contribution
            gaussian = peak_height * np.exp(-0.5 * np.sum(((x_norm - peak_pos) / peak_width)**2))
            peaks += gaussian
            
        # Sine modulation to increase multimodality
        sine_mod = np.sum(np.sin(10 * x_norm) * np.cos(5 * x_norm))
        
        # Cross-dimensional coupling with adaptive strength
        coupling = 0.0
        for i in range(self.dim - 1):
            coupling += (x_norm[i] * x_norm[i+1]) * (1 + 0.1 * np.sin(i * np.pi / self.dim))
            
        # Add a chaotic component using logistic map-like behavior
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(20 * x_norm[i]) * np.exp(-0.1 * x_norm[i]**2)
            
        # Combine all components with different weights
        return quadratic + 0.5 * peaks + 0.3 * sine_mod + 0.2 * coupling + 0.1 * chaotic