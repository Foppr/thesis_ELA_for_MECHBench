import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Base quadratic term for global attraction
        quadratic = np.sum(x_norm ** 2)
        
        # Hyperchaotic sinusoidal oscillations with exponentially decaying amplitudes
        chaotic = 2.0 * np.sum(np.sin(9 * np.pi * x_norm * np.exp(-0.3 * x_norm**2)) ** 3)
        
        # Multiple adaptive Gaussian peaks with varying widths and positions
        gaussian1 = 1.0 * np.sum(np.exp(-7 * (x_norm - 0.25 * np.sin(4 * x_norm)) ** 2))
        gaussian2 = 0.7 * np.sum(np.exp(-6 * (x_norm + 0.3 * np.cos(3 * x_norm)) ** 2))
        gaussian3 = 0.5 * np.sum(np.exp(-9 * (x_norm - 0.4 * np.tan(2 * x_norm)) ** 2))
        
        # Non-separable cross-term interactions with trigonometric coupling
        cross_term = 0.4 * np.sum(x_norm[:-1] * x_norm[1:] * np.sin(5 * np.pi * x_norm[:-1] * x_norm[1:]))
        
        # Additional high-frequency oscillatory component for increased complexity
        high_freq = 0.6 * np.sum(np.cos(12 * np.pi * x_norm * np.exp(-0.1 * x_norm**2)) ** 2)
        
        # Introduce a new complex interaction term to improve discrimination
        interaction_term = 0.3 * np.sum(np.sin(7 * np.pi * x_norm) * np.cos(4 * np.pi * x_norm) * 
                                       (x_norm[:-1] + x_norm[1:]) ** 2)
        
        # Add a new peak family with logarithmic decay
        log_peak = 0.8 * np.sum(np.exp(-5 * (x_norm - 0.3 * np.log(1 + np.abs(x_norm))) ** 2))
        
        # Dimension-dependent conditioning factor to increase problem difficulty
        condition_factor = 1.0 + 0.5 * np.log(self.dim + 1)
        
        # Combine all terms with different weights and scaling
        return condition_factor * (quadratic + chaotic + gaussian1 + gaussian2 + gaussian3 + 
                                 cross_term + high_freq + interaction_term + log_peak)