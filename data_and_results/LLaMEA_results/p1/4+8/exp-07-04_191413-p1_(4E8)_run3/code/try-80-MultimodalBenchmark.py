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
        
        # Add a cross-dimensional interaction term with higher coupling strength
        cross_term = 0.3 * np.sum(x_scaled[:-1] * x_scaled[1:])
        
        # Add a new chaotic sine wave component with varying frequency
        chaotic_term = np.sum(np.sin(15 * np.pi * x_scaled) * np.exp(-0.5 * x_scaled**2))
        
        # Introduce nested chaotic components with different frequencies and coupling
        nested_chaotic = np.sum(np.sin(25 * np.pi * x_scaled) * np.cos(7 * np.pi * x_scaled) * np.exp(-0.2 * x_scaled**2))
        
        # Add a multi-scale sinusoidal modulation for enhanced multimodality
        multi_scale = np.sum(np.sin(3 * np.pi * x_scaled) * np.sin(10 * np.pi * x_scaled) * np.exp(-0.1 * x_scaled**2))
        
        # Introduce a non-separable cross-dimensional interaction with exponential coupling
        non_sep_term = 0.2 * np.sum(np.exp(-0.5 * (x_scaled[:-1]**2 + x_scaled[1:]**2)) * np.sin(8 * np.pi * x_scaled[:-1] * x_scaled[1:]))
        
        # Combine with different weights
        return quadratic + 0.6 * exp_decay + 0.2 * cos_peaks + cross_term + 0.1 * chaotic_term + 0.15 * nested_chaotic + 0.08 * multi_scale + non_sep_term