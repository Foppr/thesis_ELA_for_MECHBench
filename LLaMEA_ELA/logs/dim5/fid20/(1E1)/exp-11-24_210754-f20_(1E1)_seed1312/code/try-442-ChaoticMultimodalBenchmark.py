import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base conditioning term with quadratic growth
        f1 = 0.5 * np.sum(x**2) / self.dim
        
        # Exponential decay modulated by trigonometric interference (mutated weights)
        f2 = 0.35 * np.sum(np.exp(-0.6 * np.abs(x)) * np.sin(12.0 * x) * np.cos(8.0 * x))
        
        # Polynomial modulation with fractional powers and asymmetric coefficients (mutated exponents)
        f3 = 0.22 * np.sum((x**4.5 + 0.6 * x**3.2 + 0.4 * x**2.5 + 0.15 * x**1.7) / self.dim)
        
        # Saddle point structure with chaotic sine-cosine coupling (mutated frequencies)
        f4 = 0.28 * np.sum(np.sin(18.0 * x) * np.cos(14.0 * x) * np.exp(-0.35 * x**2))
        
        # Cross-dimensional interaction with asymmetric coupling (mutated interaction)
        f5 = 0.12 * np.sum(np.sin(x[:-1] * x[1:]) * np.cos(0.9 * x[:-1] + 1.1 * x[1:]))
        
        # Fractal-like recursive interference with varying scales (mutated frequencies)
        f6 = 0.17 * np.sum(np.sin(28.0 * np.sin(6.0 * x)) * np.cos(22.0 * np.cos(4.5 * x)))
        
        # Asymmetric polynomial with exponential weighting (mutated coefficients)
        f7 = 0.20 * np.sum((x**3.9 + 0.4 * x**2.8 - 0.2 * x) * np.exp(-0.25 * np.abs(x)))
        
        # Multi-scale harmonic modulation with varying frequencies and amplitudes (mutated phases)
        f8 = 0.14 * np.sum(np.sin(32.0 * x + np.sin(16.0 * x)) * np.cos(27.0 * x + np.cos(11.0 * x)))
        
        # Combine all components with carefully tuned weights for enhanced complexity
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8