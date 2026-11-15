import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic logistic map inspired terms for irregularity
        logistic_terms = np.sum(4 * x_norm * (1 - x_norm**2))
        
        # Enhanced sinusoidal frequency interactions with dynamic modulation
        sin_freq = np.sum(np.sin(7 * x_norm) * np.cos(9 * x_norm) * np.exp(-0.2 * x_norm**2))
        
        # Modified polynomial cross-terms with adaptive exponents
        poly_cross = np.sum((x_norm[0] * x_norm[1])**4) + \
                     0.5 * np.sum(x_norm**4 * np.sin(4 * np.pi * x_norm))
        
        # Adaptive conditioning with exponential weighting
        adapt_cond = np.sum(x_norm**2 * np.exp(-0.2 * np.abs(x_norm)))
        
        # Additional nonlinear couplings with mixed trigonometric and power terms
        nonlinear_coupling = 0.4 * np.sum(np.sin(3 * x_norm) * np.cos(7 * x_norm) * x_norm**2)
        
        # Cross-dimensional interaction terms with chaotic behavior
        cross_dim = np.sum(np.sin(x_norm[0] * x_norm[1]) * np.cos(x_norm[0] + x_norm[1]))
        
        # Add a small noise term to create more complex landscape
        noise = 0.02 * np.random.random()
        
        # Combine all terms to create a multimodal landscape
        return logistic_terms + sin_freq + poly_cross + adapt_cond + nonlinear_coupling + cross_dim + noise