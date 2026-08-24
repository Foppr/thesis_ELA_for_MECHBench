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
        
        # Multiple cosine peaks with varying frequencies and weights
        cos_peaks = np.sum(np.cos(11 * np.pi * x_scaled) * np.exp(-0.5 * x_scaled**2) + 
                          0.5 * np.cos(19 * np.pi * x_scaled) * np.exp(-0.3 * x_scaled**2))
        
        # Cross-dimensional interaction with chaotic multiplier
        cross_term = 0.15 * np.sum(np.sin(5 * np.pi * x_scaled[:-1]) * x_scaled[1:] * np.exp(-0.7 * x_scaled[:-1]**2))
        
        # Nested chaotic sine wave component with higher frequency and nonlinearity
        chaotic_term = 0.4 * np.sum(np.sin(13 * np.pi * x_scaled) * np.sin(17 * np.pi * x_scaled) * 
                                   np.sin(23 * np.pi * x_scaled) * np.sin(29 * np.pi * x_scaled))
        
        # Secondary chaotic modulation with fractal-like behavior
        secondary_chaos = 0.2 * np.sum(np.sin(31 * np.pi * x_scaled**2) * np.cos(37 * np.pi * x_scaled) * 
                                      np.exp(-0.4 * x_scaled**2))
        
        # New nested chaotic component with cubic and quadratic base
        nested_chaos = 0.25 * np.sum(np.sin(41 * np.pi * x_scaled**3) * np.cos(47 * np.pi * x_scaled**2) * 
                                   np.sin(53 * np.pi * x_scaled))
        
        # Multi-modal peak component with varying amplitude and frequency
        multi_peak = 0.3 * np.sum(np.sin(25 * np.pi * x_scaled) * np.exp(-0.3 * x_scaled**2) * 
                                np.cos(21 * np.pi * x_scaled) * np.sin(19 * np.pi * x_scaled))
        
        # Fractal-like energy term for increased multimodality
        fractal_term = 0.18 * np.sum(np.sin(61 * np.pi * x_scaled**1.5) * np.cos(67 * np.pi * x_scaled**1.3) * 
                                   np.exp(-0.2 * x_scaled**2))
        
        # Add a new interaction term between every third dimension
        third_dim_interaction = 0.12 * np.sum(np.sin(9 * np.pi * x_scaled[::3]) * np.cos(13 * np.pi * x_scaled[1::3]) * 
                                            np.sin(17 * np.pi * x_scaled[2::3]))
        
        # Combine all terms with different weights
        return quadratic + 0.7 * exp_decay + 0.3 * cos_peaks + cross_term + chaotic_term + secondary_chaos + \
               nested_chaos + multi_peak + fractal_term + third_dim_interaction