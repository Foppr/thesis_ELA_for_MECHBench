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
        
        # Chaotic sine wave component with adaptive conditioning
        chaotic = np.sum(np.sin(10 * np.pi * x_scaled + np.sin(3 * np.pi * x_scaled)) * np.exp(-0.5 * x_scaled**2))
        
        # New cross-dimensional interaction term with non-linear coupling
        cross_term = 0.1 * np.sum(np.sin(x_scaled[:-1] * x_scaled[1:]) * (x_scaled[:-1]**2 + x_scaled[1:]**2))
        
        # Add a small perturbation to increase landscape complexity
        perturbation = 0.05 * np.sum(np.sin(7 * np.pi * x_scaled) * np.cos(4 * np.pi * x_scaled))
        
        # Combine with different weights
        return quadratic + 0.6 * exp_decay + 0.2 * cos_peaks + 0.3 * chaotic + cross_term + perturbation