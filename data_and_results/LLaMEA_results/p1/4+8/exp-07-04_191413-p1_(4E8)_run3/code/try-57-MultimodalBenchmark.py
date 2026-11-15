import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Shift input to center the global minimum at (1,1,...,1)
        x_shifted = x - 1.0
        
        # Scale input to [-1, 1] range
        x_scaled = x_shifted / 5.0
        
        # Quadratic term for conditioning
        quadratic = np.sum(x_scaled**2)
        
        # Chaotic sine waves with varying frequencies and amplitudes
        chaotic_waves = np.sum(np.sin(10 * np.pi * x_scaled) * np.cos(7 * np.pi * x_scaled) * np.exp(-0.5 * x_scaled**2))
        
        # Cross-dimensional coupling with non-linear interaction
        cross_term = 0.2 * np.sum(np.sin(np.pi * x_scaled[:-1] * x_scaled[1:]))
        
        # Adaptive conditioning based on dimension
        adaptive_conditioning = np.sum((1 + 0.1 * self.dim) * np.exp(-x_scaled**2) * np.sin(3 * np.pi * x_scaled)**2)
        
        # Additional chaotic peaks with varying heights
        chaotic_peaks = np.sum(np.cos(15 * np.pi * x_scaled) * np.sin(12 * np.pi * x_scaled) * np.exp(-0.2 * x_scaled**2))
        
        # Combine all terms with different weights
        return quadratic + 0.8 * chaotic_waves + 0.3 * cross_term + 0.5 * adaptive_conditioning + 0.4 * chaotic_peaks