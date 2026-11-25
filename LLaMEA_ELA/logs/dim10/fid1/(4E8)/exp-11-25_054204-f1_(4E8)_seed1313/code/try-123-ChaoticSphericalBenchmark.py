import numpy as np

class ChaoticSphericalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequence for dynamic scaling
        self.chaotic_sequence = np.log(np.arange(1, dim + 1)) / np.log(dim + 1)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # Chaotic spherical harmonic component with dynamic frequencies
        f2 = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * self.chaotic_sequence[i]
            f2 -= 0.3 * np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Spherical harmonic interactions with adaptive coupling
        f3 = 0.2 * np.sum(np.sin(x) * np.cos(2.0 * x))
        
        # Logistic map chaotic modulation
        f4 = 0.15 * np.sum(np.sin(np.pi * np.log(1 + np.abs(x))) * np.cos(3.0 * x))
        
        # Cross-dimensional coupling with exponential weighting
        cross_interaction = 0.0
        for i in range(self.dim - 1):
            weight = np.exp(-i / (self.dim + 1))
            cross_interaction += weight * np.sin(x[i] * x[i+1])
        f5 = 0.25 * cross_interaction
        
        # Adaptive polynomial chaos with fractal-like behavior
        f6 = 0.1 * np.sum((x**4) * np.sin(2.0 * x))
        
        # Sigmoidal scaling with chaotic modulation
        f7 = 0.18 * np.sum(1.0 / (1.0 + np.exp(-x)) * np.cos(x))
        
        # Enhanced harmonic oscillation with dynamic frequency
        freq = 1.5 + 0.3 * np.sin(np.sum(x**2) / 10.0)
        f8 = 0.12 * np.sum(np.sin(freq * x) * np.cos(2.0 * x))
        
        # Nonlinear correlation with exponential weighting
        f9 = 0.08 * np.sum(np.exp(-x**2) * x**3)
        
        # Additional higher-order terms for increased complexity (mutated)
        f10 = 0.06 * np.sum(x**6 * np.cos(x/3))  # Slightly increased coefficient
        f11 = 0.11 * np.sum(np.abs(x)**2.5)       # Increased coefficient
        
        # New term: Fifth-order polynomial with sine modulation and dynamic scaling
        f12 = 0.07 * np.sum((x**5) * np.sin(1.5 * x) * np.cos(0.5 * np.sum(x**2)))
        
        # New term: Coupled exponential and trigonometric interactions
        f13 = 0.11 * np.sum(np.exp(-0.5 * x**2) * np.sin(3.0 * x))
        
        # New term: Multi-scale harmonic coupling with dimension-dependent modulation
        scale_factor = 1.0 + 0.3 * np.log(self.dim + 1)
        f14 = 0.1 * np.sum(np.sin(x) * np.cos(2.0 * x) * np.sin(0.5 * np.sum(x**2)))
        
        # New term: Adaptive chaotic coupling with modified logistic map
        logistic_mod = np.log(1 + np.abs(x)) * np.sin(x)
        f15 = 0.13 * np.sum(logistic_mod * np.cos(2.0 * x))
        
        return scale_factor * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13 + f14 + f15)