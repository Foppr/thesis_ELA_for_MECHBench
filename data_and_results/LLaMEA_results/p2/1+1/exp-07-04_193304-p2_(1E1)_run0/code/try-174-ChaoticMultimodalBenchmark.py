import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Quadratic base with adaptive scaling
        f1 = 0.5 * np.sum(x_norm**2)
        
        # Trigonometric components with varying frequencies and amplitudes
        freqs = np.arange(1, self.dim + 1) * np.pi * 0.8
        f2 = np.sum(np.sin(freqs * x_norm) * np.cos(freqs * x_norm))
        f3 = np.sum(np.sin(freqs * x_norm**2) * np.cos(freqs * x_norm**2))
        
        # Logarithmic penalty with adaptive base
        f4 = np.sum(np.log(1.1 + np.abs(x_norm)) * x_norm**2)
        
        # Multi-scale oscillation with exponential decay
        f5 = np.sum(np.sin(30 * x_norm * np.log(1.2 + np.abs(x_norm))) * np.exp(-0.3 * x_norm**2))
        
        # Fractional power with sinusoidal modulation
        f6 = np.sum(np.abs(x_norm)**(1.5 + 0.5 * np.sin(np.arange(self.dim) * 0.7)) * np.cos(15 * x_norm))
        
        # Cross-dimensional coupling with hyperbolic functions
        f7 = 0.1 * np.sum(np.tanh(x_norm[:-1] * x_norm[1:]) * np.sin(10 * x_norm[:-1]))
        
        # Adaptive chaotic interaction
        f8 = np.sum(np.sin(x_norm * np.tanh(x_norm * 1.5)) * np.cos(x_norm * np.tanh(x_norm * 0.8)))
        
        # Gaussian-like penalty with dynamic variance
        f9 = 0.2 * np.sum(np.exp(-0.5 * (x_norm / (1.0 + 0.2 * np.abs(x_norm)))**2))
        
        # High-order polynomial with sinusoidal modulation
        f10 = 0.05 * np.sum((x_norm**4 + np.sin(x_norm))**2)
        
        # Multi-modal sine with dynamic amplitude
        f11 = 0.15 * np.sum(np.sin(20 * x_norm + np.sin(8 * x_norm)) * np.exp(-0.2 * x_norm**2))
        
        # Dimensionality-dependent scaling
        f12 = 0.1 * np.sum(x_norm**3 * np.sin(5 * x_norm * np.log(1.1 + np.abs(x_norm))))
        
        # Complex interaction with inverse hyperbolic functions
        f13 = 0.08 * np.sum(np.arctanh(x_norm) * np.sin(12 * x_norm))
        
        # Asymmetric exponential decay
        f14 = 0.12 * np.sum(np.exp(-0.4 * np.abs(x_norm)) * np.sin(18 * x_norm))
        
        # Fractional dimensionality effect with oscillation
        f15 = 0.09 * np.sum(np.abs(x_norm)**(1.3 + 0.4 * np.cos(np.arange(self.dim) * 0.5)))
        
        # Combined chaotic and polynomial terms
        f16 = 0.11 * np.sum((x_norm**2 + np.sin(x_norm * 0.5)) * np.cos(x_norm * 1.2))
        
        # Multi-scale penalty with varying exponents
        f17 = 0.07 * np.sum(np.exp(-0.6 * np.abs(x_norm)) * np.sin(25 * x_norm))
        
        # Adaptive coupling with logarithmic scaling
        f18 = 0.13 * np.sum(np.sin(x_norm * np.log(1.1 + np.abs(x_norm))) * np.cos(x_norm * 0.9))
        
        # Complex cross-term with trigonometric modulation
        f19 = 0.06 * np.sum(np.sin(x_norm[:-2] * x_norm[1:-1] * x_norm[2:]) * np.cos(7 * x_norm[:-2]))
        
        # Hybrid logarithmic and exponential interaction
        f20 = 0.08 * np.sum(np.log(1.2 + np.abs(x_norm)) * np.exp(-0.5 * x_norm**2))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13 + f14 + f15 + f16 + f17 + f18 + f19 + f20