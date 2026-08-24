import numpy as np

class HybridChaoticMultiModal:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Quadratic base with adaptive scaling
        f1 = 0.5 * np.sum(x_norm**2)
        
        # Sinusoidal modulations with varying frequencies and amplitudes
        freqs = np.arange(1, self.dim + 1) * 2.0
        f2 = 0.3 * np.sum(np.sin(freqs * x_norm) * np.cos(freqs * x_norm * 0.7))
        
        # Logarithmic barrier terms
        f3 = 0.2 * np.sum(np.log(1.1 + np.abs(x_norm)) * x_norm**2)
        
        # Multi-modal sine-cosine combinations
        f4 = 0.25 * np.sum(np.sin(8 * x_norm) * np.cos(5 * x_norm) * np.exp(-0.3 * x_norm**2))
        
        # Adaptive coupling between dimensions
        if self.dim > 1:
            coupling = np.sum(np.sin(x_norm[:-1] * x_norm[1:]) * (1 + 0.2 * np.sin(np.arange(self.dim-1))))
            f5 = 0.15 * coupling
        else:
            f5 = 0.0
        
        # Fractional power with dynamic exponent
        exponents = 1.5 + 0.5 * np.sin(np.arange(self.dim) * 0.8)
        f6 = 0.18 * np.sum(np.abs(x_norm)**exponents)
        
        # Hyperbolic tangent based chaotic interaction
        f7 = 0.22 * np.sum(np.tanh(x_norm * np.sin(x_norm * 1.3)))
        
        # Gaussian-like penalty with dimension-dependent variance
        variance = 1.0 + 0.3 * np.sin(np.arange(self.dim) * 0.5)
        f8 = 0.14 * np.sum(np.exp(-0.5 * (x_norm / variance)**2))
        
        # Cross-dimensional polynomial interactions
        if self.dim > 2:
            poly_interaction = np.sum(x_norm[:-2]**2 * x_norm[1:-1] * x_norm[2:])
            f9 = 0.1 * poly_interaction
        else:
            f9 = 0.0
            
        # Adaptive frequency sine with amplitude modulation
        f10 = 0.2 * np.sum(np.sin(12 * x_norm * (1 + 0.1 * np.cos(x_norm))) * np.exp(-0.2 * x_norm**2))
        
        # Combined exponential and trigonometric terms
        f11 = 0.16 * np.sum(np.exp(-np.abs(x_norm)) * np.sin(6 * x_norm))
        
        # Multi-scale oscillation with dynamic frequency
        f12 = 0.13 * np.sum(np.sin(15 * x_norm * np.log(1.2 + np.abs(x_norm))))
        
        # Dimensionality-dependent scaling
        scale_factor = 1.0 + 0.2 * np.sin(np.sum(x_norm) * 0.3)
        f13 = 0.11 * np.sum(x_norm**4) * scale_factor
        
        # Asymmetric penalty with logarithmic scaling
        f14 = 0.19 * np.sum(np.log(1.05 + x_norm**2) * np.exp(-0.25 * np.abs(x_norm)))
        
        # Final combined function
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13 + f14