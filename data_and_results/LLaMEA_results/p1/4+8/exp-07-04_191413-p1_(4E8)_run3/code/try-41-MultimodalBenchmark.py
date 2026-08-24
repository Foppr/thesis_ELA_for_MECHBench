import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Quadratic term for conditioning
        quadratic = np.sum(x_scaled**2)
        
        # Chaotic sine waves with varying frequencies and amplitudes
        chaotic = np.sum(np.sin(10 * np.pi * x_scaled) * np.cos(7 * np.pi * x_scaled) * np.exp(-0.5 * x_scaled**2))
        
        # Enhanced exponential decay with higher frequency trigonometric modulation
        exp_decay = np.sum(np.exp(-x_scaled**2) * np.sin(8 * np.pi * x_scaled)**4)
        
        # Additional sine peaks with varying amplitudes and frequencies
        sin_peaks = np.sum(np.sin(12 * np.pi * x_scaled) * np.exp(-0.2 * x_scaled**2))
        
        # Radial symmetry term with multiple local minima and chaotic behavior
        radial = np.sum((x_scaled**2 + 0.05) * np.exp(-x_scaled**2) * np.cos(6 * np.pi * x_scaled) * np.sin(3 * np.pi * x_scaled))
        
        # Cross-term interaction with chaotic coupling
        cross_term = np.sum(x_scaled[:-1] * x_scaled[1:] * np.sin(3 * np.pi * x_scaled[:-1]) * np.cos(2 * np.pi * x_scaled[1:]))
        
        # Adaptive conditioning based on dimensionality
        adaptive_cond = np.sum(np.abs(x_scaled) * np.exp(-0.1 * x_scaled**2))
        
        # Combine all terms with different weights
        return 2.0 * quadratic + 1.2 * chaotic + 0.8 * exp_decay + 0.6 * sin_peaks + 0.4 * radial + 0.3 * cross_term + 0.2 * adaptive_cond