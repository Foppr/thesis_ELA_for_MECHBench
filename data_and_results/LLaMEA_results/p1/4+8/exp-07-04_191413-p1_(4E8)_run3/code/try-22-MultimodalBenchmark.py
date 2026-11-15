import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Quadratic term for conditioning
        quadratic = np.sum(x_scaled**2)
        
        # Enhanced exponential decay with higher frequency trigonometric modulation
        exp_decay = np.sum(np.exp(-x_scaled**2) * np.sin(5 * np.pi * x_scaled)**3)
        
        # Additional sine peaks with varying amplitudes and frequencies
        sin_peaks = np.sum(np.sin(9 * np.pi * x_scaled) * np.exp(-0.3 * x_scaled**2))
        
        # Radial symmetry term with multiple local minima
        radial = np.sum((x_scaled**2 + 0.1) * np.exp(-x_scaled**2) * np.cos(4 * np.pi * x_scaled))
        
        # Cross-term interaction for increased complexity
        cross_term = np.sum(x_scaled[:-1] * x_scaled[1:] * np.sin(2 * np.pi * x_scaled[:-1]))
        
        # Combine all terms with different weights
        return 1.5 * quadratic + 0.7 * exp_decay + 0.5 * sin_peaks + 0.3 * radial + 0.2 * cross_term