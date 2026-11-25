import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_norm**2)
        
        # Chaotic sine-cosine wave structure with modified frequencies
        f2 = 0.4 * np.sum(np.sin(12 * x_norm) * np.cos(8 * x_norm))
        
        # Asymmetric quartic potentials with varying exponents
        f3 = 0.3 * np.sum(np.where(x_norm > 0, x_norm**5, -x_norm**3))
        
        # Non-separable high-order polynomial interactions with altered coupling
        poly_interaction = 0.0
        for i in range(self.dim - 1):
            poly_interaction += (x_norm[i]**4 + x_norm[i+1]**2) * np.exp(-0.15 * (i + 1))
        f4 = 0.25 * np.sum(poly_interaction)
        
        # Multi-scale fractal noise with varying frequencies
        f5 = 0.2 * np.sum(np.sin(25 * x_norm) + np.sin(70 * x_norm) + np.sin(200 * x_norm))
        
        # Cross-dimension coupling with exponential weights
        cross_term = 0.0
        for i in range(self.dim - 1):
            cross_term += np.exp(-0.25 * (i + 1)) * np.sin(35 * x_norm[i]) * np.cos(25 * x_norm[i+1])
        f6 = 0.15 * np.sum(cross_term)
        
        # Degenerate saddle points with piecewise cubic functions
        f7 = 0.15 * np.sum(np.where(x_norm > 0, x_norm**4, -x_norm**2))
        
        # Add controlled noise for robustness testing
        noise = 0.06 * np.random.standard_normal(self.dim)
        f8 = 0.06 * np.sum(noise**2)
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8