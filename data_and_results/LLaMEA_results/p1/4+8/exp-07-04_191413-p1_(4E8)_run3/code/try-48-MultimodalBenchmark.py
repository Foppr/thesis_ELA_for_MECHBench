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
        
        # Enhanced oscillatory components with multiple frequencies
        oscillatory = np.sum(np.sin(15 * np.pi * x_scaled**2) * np.cos(12 * np.pi * x_scaled**2))
        
        # Radial symmetry terms with exponential decay
        radial = np.sum(np.exp(-x_scaled**2) * np.sin(8 * np.pi * x_scaled)**3)
        
        # Cross-dimensional interaction with non-linear coupling
        cross_term = 0.15 * np.sum(x_scaled[:-1]**2 * x_scaled[1:]**2)
        
        # Additional noise-like component to increase robustness challenge
        noise = 0.05 * np.sum(np.sin(20 * np.pi * x_scaled) * np.cos(18 * np.pi * x_scaled))
        
        # Combine with different weights
        return quadratic + 0.7 * chaotic_waves + 0.3 * oscillatory + 0.2 * radial + cross_term + noise