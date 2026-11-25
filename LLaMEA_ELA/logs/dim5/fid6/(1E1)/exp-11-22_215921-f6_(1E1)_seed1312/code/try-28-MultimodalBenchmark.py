import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Base quadratic term for global attraction
        quadratic = np.sum(x_norm ** 2)
        
        # Enhanced hyperchaotic sinusoidal oscillations with double-frequency components
        chaotic = 2.0 * np.sum(np.sin(15 * np.pi * x_norm * np.exp(-0.3 * x_norm**2)) ** 4)
        
        # Multiple adaptive Gaussian peaks with varying widths, positions, and interaction terms
        gaussian1 = 1.5 * np.sum(np.exp(-12 * (x_norm - 0.2 * np.sin(7 * x_norm)) ** 2))
        gaussian2 = 1.0 * np.sum(np.exp(-9 * (x_norm + 0.4 * np.cos(6 * x_norm)) ** 2))
        gaussian3 = 0.8 * np.sum(np.exp(-15 * (x_norm - 0.4 * np.tan(5 * x_norm)) ** 2))
        
        # Stronger non-separable cross-term interactions with polynomial coupling
        cross_term = 0.8 * np.sum(x_norm[:-1] * x_norm[1:] * (np.sin(8 * np.pi * x_norm[:-1] * x_norm[1:])) ** 2)
        
        # Additional high-frequency oscillatory component with exponential modulation
        high_freq = 1.0 * np.sum(np.cos(20 * np.pi * x_norm * np.exp(-0.2 * x_norm**2)) ** 3)
        
        # New complex interaction term with cubic coupling and adaptive scaling
        interaction_term = 0.6 * np.sum(np.sin(10 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm) * 
                                       (x_norm[:-1] + x_norm[1:]) ** 3)
        
        # New peak family with hyperbolic tangent modulation and multi-scale structure
        tanh_peak = 1.2 * np.sum(np.exp(-8 * (x_norm - 0.3 * np.tanh(4 * x_norm)) ** 2))
        
        # Additional logarithmic decay peak with sinusoidal modulation
        log_modulated = 0.7 * np.sum(np.exp(-5 * (x_norm - 0.2 * np.log(1 + np.abs(x_norm)) * np.sin(3 * x_norm)) ** 2))
        
        # Dimension-dependent conditioning factor to increase problem difficulty
        condition_factor = 1.0 + 0.8 * np.log(self.dim + 1)
        
        # Combine all terms with different weights and scaling
        return condition_factor * (quadratic + chaotic + gaussian1 + gaussian2 + gaussian3 + 
                                 cross_term + high_freq + interaction_term + tanh_peak + log_modulated)