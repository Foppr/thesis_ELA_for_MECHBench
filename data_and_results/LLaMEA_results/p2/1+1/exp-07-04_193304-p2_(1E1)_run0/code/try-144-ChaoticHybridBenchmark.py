import numpy as np

class ChaoticHybridBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Quadratic base with adaptive conditioning
        f1 = 0.5 * np.sum(x_norm**2)
        
        # Trigonometric components with varying frequencies and amplitudes
        freqs = np.arange(1, self.dim + 1) * np.pi * 0.8
        f2 = 0.3 * np.sum(np.sin(freqs * x_norm) * np.cos(freqs * x_norm))
        
        # Logarithmic penalty with adaptive scaling
        f3 = 0.25 * np.sum(np.log(1.1 + np.abs(x_norm)) * x_norm**2)
        
        # Multi-scale chaotic interaction using sine and cosine combinations
        f4 = 0.2 * np.sum(np.sin(x_norm * np.cos(x_norm * 1.5)) * np.exp(-0.3 * np.abs(x_norm)))
        
        # Fractional power terms with dynamic exponents
        exponents = 2.0 + 0.5 * np.sin(np.arange(self.dim) * 0.7)
        f5 = 0.15 * np.sum(np.abs(x_norm)**exponents)
        
        # Cross-dimensional coupling with adaptive weights
        weights = 1.0 + 0.3 * np.sin(np.arange(self.dim-1) * 0.5)
        f6 = 0.18 * np.sum(weights * x_norm[:-1] * x_norm[1:])
        
        # Hyperbolic tangent based chaotic interaction
        f7 = 0.22 * np.sum(np.tanh(x_norm * np.sin(x_norm * 1.2)))
        
        # Adaptive exponential decay with dimensionality scaling
        decay_rates = 0.1 + 0.2 * np.sin(np.arange(self.dim) * 0.6)
        f8 = 0.14 * np.sum(np.exp(-decay_rates * np.abs(x_norm)))
        
        # Multi-modal sine with varying amplitude and frequency
        f9 = 0.19 * np.sum(np.sin(15 * x_norm + np.sin(8 * x_norm)) * np.exp(-0.25 * x_norm**2))
        
        # Gaussian-like penalty with dynamic variance
        f10 = 0.28 * np.sum(np.exp(-0.5 * (x_norm / (1.2 + np.abs(x_norm)))**2))
        
        # Fractional-order derivative inspired term
        f11 = 0.12 * np.sum(np.abs(x_norm)**1.7 * np.cos(x_norm * 1.1))
        
        # Adaptive scaling with exponential decay
        f12 = 0.16 * np.sum(np.exp(-0.5 * np.abs(x_norm)) * np.sin(12 * x_norm))
        
        # Combined polynomial and trigonometric term
        f13 = 0.11 * np.sum((x_norm**2 + np.sin(x_norm))**1.5)
        
        # High-frequency oscillation with amplitude modulation
        f14 = 0.21 * np.sum(np.sin(25 * x_norm) * np.exp(-0.3 * x_norm**2))
        
        # Multi-scale oscillation with dynamic frequency
        f15 = 0.17 * np.sum(np.sin(30 * x_norm * np.log(1.1 + np.abs(x_norm))))
        
        # Adaptive chaotic coupling with logarithmic scaling
        f16 = 0.13 * np.sum(np.sin(x_norm * np.cos(x_norm * 2.0)) * np.exp(-0.2 * np.abs(x_norm)))
        
        # Complex cross-term interactions
        f17 = 0.08 * np.sum(np.sin(x_norm[:-2] * x_norm[1:-1] * x_norm[2:]))
        
        # Dimensionality-dependent penalty
        f18 = 0.1 * np.sum(np.abs(x_norm)**(1.3 + 0.4 * np.sin(np.arange(self.dim) * 0.8)))
        
        # Combined chaotic and polynomial interaction
        f19 = 0.15 * np.sum(np.sin(x_norm * np.exp(-0.1 * x_norm)) * x_norm**2)
        
        # Asymmetric penalty with logarithmic behavior
        f20 = 0.23 * np.sum(np.exp(-0.4 * (x_norm**2 + 0.15 * np.abs(x_norm))))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13 + f14 + f15 + f16 + f17 + f18 + f19 + f20