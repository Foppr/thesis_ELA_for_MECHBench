import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Quadratic term for conditioning
        quadratic = np.sum(x_scaled**2)
        
        # Enhanced chaotic sine waves with multiple frequency components
        chaotic = np.sum(np.sin(15 * np.pi * x_scaled) * np.cos(11 * np.pi * x_scaled) * np.exp(-0.3 * x_scaled**2))
        
        # Enhanced exponential decay with higher frequency trigonometric modulation
        exp_decay = np.sum(np.exp(-x_scaled**2) * np.sin(10 * np.pi * x_scaled)**5)
        
        # Additional sine peaks with varying amplitudes and frequencies
        sin_peaks = np.sum(np.sin(15 * np.pi * x_scaled) * np.exp(-0.3 * x_scaled**2))
        
        # Radial symmetry term with multiple local minima and chaotic behavior
        radial = np.sum((x_scaled**2 + 0.03) * np.exp(-x_scaled**2) * np.cos(8 * np.pi * x_scaled) * np.sin(4 * np.pi * x_scaled))
        
        # Enhanced cross-term interaction with chaotic coupling
        cross_term = np.sum(x_scaled[:-1] * x_scaled[1:] * np.sin(5 * np.pi * x_scaled[:-1]) * np.cos(4 * np.pi * x_scaled[1:]))
        
        # Adaptive conditioning based on dimensionality with enhanced complexity
        adaptive_cond = np.sum(np.abs(x_scaled) * np.exp(-0.2 * x_scaled**2))
        
        # Additional high-frequency oscillatory component for increased complexity
        high_freq = np.sum(np.sin(20 * np.pi * x_scaled) * np.cos(18 * np.pi * x_scaled) * np.exp(-0.1 * x_scaled**2))
        
        # Combine all terms with different weights
        return 2.5 * quadratic + 1.5 * chaotic + 1.0 * exp_decay + 0.8 * sin_peaks + 0.6 * radial + 0.5 * cross_term + 0.3 * adaptive_cond + 0.4 * high_freq