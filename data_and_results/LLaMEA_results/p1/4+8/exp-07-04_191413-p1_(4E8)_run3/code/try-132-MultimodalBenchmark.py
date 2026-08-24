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
        
        # Exponential decay terms with sinusoidal modulation (modified frequency)
        exp_decay = np.sum(np.exp(-x_scaled**2) * np.sin(5 * np.pi * x_scaled)**2)
        
        # Additional cosine peaks with different frequency and weight
        cos_peaks = np.sum(np.cos(9 * np.pi * x_scaled) * np.exp(-0.3 * x_scaled**2))
        
        # Add a cross-dimensional interaction term with chaotic multiplier
        cross_term = 0.1 * np.sum(np.sin(3 * np.pi * x_scaled[:-1]) * x_scaled[1:] * np.exp(-0.5 * x_scaled[:-1]**2))
        
        # Introduce nested chaotic sine wave component with enhanced nonlinearity
        chaotic_term = 0.3 * np.sum(np.sin(7 * np.pi * x_scaled) * np.sin(11 * np.pi * x_scaled) * np.sin(13 * np.pi * x_scaled))
        
        # Add a secondary chaotic modulation to increase multimodality
        secondary_chaos = 0.15 * np.sum(np.sin(17 * np.pi * x_scaled**2) * np.cos(19 * np.pi * x_scaled))
        
        # Introduce a new nested chaotic component with higher frequency and different base
        nested_chaos = 0.2 * np.sum(np.sin(23 * np.pi * x_scaled**3) * np.cos(29 * np.pi * x_scaled**2))
        
        # Add a multi-modal peak component with varying amplitude
        multi_peak = 0.25 * np.sum(np.sin(15 * np.pi * x_scaled) * np.exp(-0.2 * x_scaled**2) * np.cos(13 * np.pi * x_scaled))
        
        # Introduce a highly chaotic component with fractional powers and nested interactions
        fractional_chaos = 0.35 * np.sum(np.sin(31 * np.pi * x_scaled**1.5) * np.cos(37 * np.pi * x_scaled**1.7) * np.sin(41 * np.pi * x_scaled**2.3))
        
        # Add a complex multi-peak structure with exponential weighting and high-frequency modulation
        complex_peaks = 0.4 * np.sum(np.exp(-0.5 * x_scaled**2) * np.sin(25 * np.pi * x_scaled) * np.cos(33 * np.pi * x_scaled) * np.sin(47 * np.pi * x_scaled))
        
        # Add a strong cross-dimensional coupling with non-linear interaction
        strong_cross = 0.2 * np.sum(np.sin(5 * np.pi * x_scaled[:-1]**2) * x_scaled[1:]**3 * np.exp(-0.1 * x_scaled[:-1]**2))
        
        # Combine with different weights
        return quadratic + 0.6 * exp_decay + 0.2 * cos_peaks + cross_term + chaotic_term + secondary_chaos + nested_chaos + multi_peak + fractional_chaos + complex_peaks + strong_cross