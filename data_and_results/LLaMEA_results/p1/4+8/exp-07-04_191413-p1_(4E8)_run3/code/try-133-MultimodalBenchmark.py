import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Shift and scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Quadratic term for conditioning
        quadratic = np.sum(x_scaled**2)
        
        # Enhanced exponential decay with sinusoidal modulation
        exp_decay = np.sum(np.exp(-x_scaled**2) * np.sin(7 * np.pi * x_scaled)**2)
        
        # Multi-frequency cosine peaks with varying weights
        cos_peaks = np.sum(np.cos(11 * np.pi * x_scaled) * np.exp(-0.5 * x_scaled**2) + 
                          0.5 * np.cos(19 * np.pi * x_scaled) * np.exp(-0.3 * x_scaled**2))
        
        # Cross-dimensional interaction with chaotic multiplier
        cross_term = 0.15 * np.sum(np.sin(5 * np.pi * x_scaled[:-1]) * x_scaled[1:] * np.exp(-0.4 * x_scaled[:-1]**2))
        
        # Nested chaotic sine wave component with higher nonlinearity
        chaotic_term = 0.35 * np.sum(np.sin(9 * np.pi * x_scaled) * np.sin(13 * np.pi * x_scaled) * np.sin(17 * np.pi * x_scaled))
        
        # Secondary chaotic modulation with different base
        secondary_chaos = 0.2 * np.sum(np.sin(23 * np.pi * x_scaled**2) * np.cos(27 * np.pi * x_scaled))
        
        # New nested chaotic component with cubic transformation
        nested_chaos = 0.25 * np.sum(np.sin(31 * np.pi * x_scaled**3) * np.cos(37 * np.pi * x_scaled**2))
        
        # Multi-modal peak component with varying amplitude and frequency
        multi_peak = 0.3 * np.sum(np.sin(21 * np.pi * x_scaled) * np.exp(-0.1 * x_scaled**2) * np.cos(19 * np.pi * x_scaled))
        
        # Add a new term with higher frequency oscillations and adaptive conditioning
        high_freq_term = 0.1 * np.sum(np.sin(41 * np.pi * x_scaled) * np.cos(47 * np.pi * x_scaled**2) * np.exp(-0.2 * x_scaled**2))
        
        # Combine all terms with optimized weights
        return quadratic + 0.7 * exp_decay + 0.3 * cos_peaks + cross_term + chaotic_term + secondary_chaos + nested_chaos + multi_peak + high_freq_term