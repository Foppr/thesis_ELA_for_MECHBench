import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Base quadratic term for global attraction
        quadratic = np.sum(x_norm ** 2)
        
        # Enhanced hyperchaotic sinusoidal oscillations with varying frequencies
        chaotic = 1.5 * np.sum(np.sin(11 * np.pi * x_norm * np.exp(-0.4 * x_norm**2)) ** 3)
        
        # Modified Gaussian peaks with adaptive widths and positions
        gaussian1 = 1.2 * np.sum(np.exp(-8 * (x_norm - 0.3 * np.sin(5 * x_norm)) ** 2))
        gaussian2 = 0.9 * np.sum(np.exp(-5 * (x_norm + 0.2 * np.cos(4 * x_norm)) ** 2))
        gaussian3 = 0.6 * np.sum(np.exp(-10 * (x_norm - 0.35 * np.tan(3 * x_norm)) ** 2))
        
        # Revised non-separable cross-term interactions with stronger coupling
        cross_term = 0.6 * np.sum(x_norm[:-1] * x_norm[1:] * np.sin(7 * np.pi * x_norm[:-1] * x_norm[1:]))
        
        # Additional high-frequency oscillatory component with modified amplitude
        high_freq = 0.8 * np.sum(np.cos(15 * np.pi * x_norm * np.exp(-0.2 * x_norm**2)) ** 2)
        
        # Dimension-dependent conditioning factor with increased variability
        condition_factor = 1.0 + 0.7 * np.log(self.dim + 1)
        
        # Combine all terms with adjusted weights for better balance
        return condition_factor * (quadratic + chaotic + gaussian1 + gaussian2 + gaussian3 + cross_term + high_freq)