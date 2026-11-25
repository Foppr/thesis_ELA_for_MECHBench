import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced chaotic wave interactions with frequency modulation
        freq_mod = 2 + 0.5 * np.sin(3 * x_norm)
        chaotic_wave = np.sum(np.sin(freq_mod * np.pi * x_norm) * np.cos(freq_mod * np.pi * x_norm))
        
        # Asymmetric quartic potential with skewed curvature and spatially varying coefficients
        asym_coeff = 1 + 0.3 * np.sin(x_norm)
        asymmetric_quartic = np.sum(asym_coeff * x_norm**4)
        
        # Non-separable high-order polynomial interactions with dynamic coupling
        poly_interaction = np.sum((x_norm[:-1]**3 + x_norm[1:]**3) * np.exp(-0.2 * (x_norm[:-1] - x_norm[1:])**2))
        
        # Added repulsive force field to increase gradient complexity and escape local minima
        repulsion = 0.2 * np.sum(1 / (1 + np.exp(-5 * (x_norm[:-1] - x_norm[1:])**2)))
        
        # Exponential weighting for gradient complexity with adaptive scaling
        exp_weighted = np.sum(np.exp(-0.2 * np.abs(x_norm)) * x_norm**3)
        
        # Cross-dimensional coupling with phase-locked harmonic interactions
        cross_coupling = 0.4 * np.sum((x_norm[:-1] - x_norm[1:])**3 * np.sin(0.5 * (x_norm[:-1] + x_norm[1:])))
        
        # Add noise term to increase robustness testing
        noise = 0.1 * np.random.normal(0, 1)
        
        return chaotic_wave + asymmetric_quartic + poly_interaction + repulsion + exp_weighted + cross_coupling + noise