import numpy as np

class MultimodalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for periodic components
        self.freqs = np.arange(1, dim + 1) * np.pi / 2.0
        self.amplitudes = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Radial basis function component with adaptive conditioning
        rbfs = np.sum(self.amplitudes * np.exp(-np.sum((x_scaled[:, None] - x_scaled[None, :])**2, axis=0) / (2.0 * (0.5 + 0.5 * np.sin(self.freqs))**2)))
        
        # Periodic wave interaction component
        wave_term = np.sum(np.sin(self.freqs * x_scaled) * np.cos(self.freqs * x_scaled))
        
        # Adaptive polynomial with mixed degrees
        poly_term = np.sum((x_scaled**6 + 0.7 * x_scaled**4 + 0.3 * x_scaled**2) * (1.0 + 0.2 * np.sin(3 * x_scaled)))
        
        # Coupled sine-wave chaotic component
        chaotic_term = np.sum(np.sin(x_scaled**2 + 0.5 * np.sin(2 * x_scaled)) * np.cos(x_scaled + 0.3 * np.cos(3 * x_scaled)))
        
        # Cross-dimension interaction with varying weights
        cross_term = np.sum(np.sin(x_scaled[:-1] * x_scaled[1:]) * np.cos(x_scaled[:-1] + x_scaled[1:]) * 
                           (1.0 + 0.1 * np.sin(2 * (x_scaled[:-1] - x_scaled[1:]))))
        
        # Combine all components with different weights
        return 0.3 * rbfs + 0.25 * wave_term + 0.2 * poly_term + 0.15 * chaotic_term + 0.1 * cross_term + 1.5