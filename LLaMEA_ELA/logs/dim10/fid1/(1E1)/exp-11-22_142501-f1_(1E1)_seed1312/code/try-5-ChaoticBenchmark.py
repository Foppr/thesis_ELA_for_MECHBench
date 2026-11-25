import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Exponential decay term
        exp_term = np.sum(np.exp(-x_scaled**2))
        
        # Trigonometric modulation with varying frequencies
        trig_term = np.sum(np.sin(2 * np.pi * x_scaled) * np.cos(3 * np.pi * x_scaled))
        
        # Polynomial distortion creating complex curvature
        poly_term = np.sum(x_scaled**4 - 2 * x_scaled**2)
        
        # Chaotic component using sine of exponential
        chaotic_term = np.sum(np.sin(np.exp(x_scaled)))
        
        # Logarithmic barrier terms to create gradient challenges
        barrier_term = np.sum(np.log(1.0 + np.abs(x_scaled)) * np.exp(-x_scaled**2))
        
        # Additional high-frequency oscillation component
        high_freq_term = np.sum(np.sin(10 * np.pi * x_scaled) * np.cos(7 * np.pi * x_scaled))
        
        # Combine all terms with different weights
        return 0.25 * exp_term + 0.35 * trig_term + 0.2 * poly_term + 0.15 * chaotic_term + 0.05 * barrier_term + 0.05 * high_freq_term + 2.0