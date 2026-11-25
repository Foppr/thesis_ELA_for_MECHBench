import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic sine-cosine wave interactions with varying frequencies and amplitudes
        chaotic_wave = np.sum(np.sin(7 * np.pi * x_norm) * np.cos(9 * np.pi * x_norm) * np.sin(11 * np.pi * x_norm))
        
        # Asymmetric quartic potential with skewed curvature
        asymmetric_quartic = np.sum(x_norm**4 * (1 + 0.3 * np.sin(3 * x_norm)))
        
        # Non-separable high-order polynomial interactions with mixed coupling
        poly_interaction = np.sum((x_norm[:-1] ** 3 + x_norm[1:] ** 3) * np.exp(-0.5 * (x_norm[:-1] - x_norm[1:])**2))
        
        # Added noise term to increase robustness testing
        noise = 0.1 * np.random.normal(0, 1, self.dim).sum()
        
        # Exponential weighting for gradient complexity
        exp_weighted = np.sum(np.exp(-0.1 * np.abs(x_norm)) * x_norm**2)
        
        # Cross-dimensional coupling with dynamic interaction strengths
        cross_coupling = 0.5 * np.sum((x_norm[:-1] - x_norm[1:])**3 * np.cos(0.5 * (x_norm[:-1] + x_norm[1:])))
        
        return chaotic_wave + asymmetric_quartic + poly_interaction + noise + exp_weighted + cross_coupling