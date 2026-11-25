import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_norm**2)
        
        # Chaotic sine-cosine wave structure
        f2 = 0.3 * np.sum(np.sin(10 * x_norm) * np.cos(10 * x_norm))
        
        # Asymmetric quartic potentials with varying exponents
        f3 = 0.25 * np.sum(np.where(x_norm > 0, x_norm**4, -x_norm**4))
        
        # Non-separable high-order polynomial interactions
        poly_interaction = 0.0
        for i in range(self.dim - 1):
            poly_interaction += (x_norm[i]**3 + x_norm[i+1]**3) * np.exp(-0.1 * (i + 1))
        f4 = 0.2 * np.sum(poly_interaction)
        
        # Multi-scale fractal noise with varying frequencies
        f5 = 0.15 * np.sum(np.sin(20 * x_norm) + np.sin(60 * x_norm) + np.sin(180 * x_norm))
        
        # Cross-dimension coupling with exponential weights
        cross_term = 0.0
        for i in range(self.dim - 1):
            cross_term += np.exp(-0.2 * (i + 1)) * np.sin(30 * x_norm[i]) * np.cos(30 * x_norm[i+1])
        f6 = 0.1 * np.sum(cross_term)
        
        # Degenerate saddle points with piecewise cubic functions
        f7 = 0.1 * np.sum(np.where(x_norm > 0, x_norm**3, -x_norm**3))
        
        # Add controlled noise for robustness testing
        noise = 0.05 * np.random.standard_normal(self.dim)
        f8 = 0.05 * np.sum(noise**2)
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8