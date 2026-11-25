import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base conditioning term with quadratic growth
        f1 = 0.5 * np.sum(x**2) / self.dim
        
        # Enhanced exponential decay modulated by trigonometric interference
        f2 = 0.35 * np.sum(np.exp(-0.4 * np.abs(x)) * np.sin(12.0 * x) * np.cos(8.0 * x))
        
        # Polynomial modulation with fractional powers and asymmetric coefficients
        f3 = 0.22 * np.sum((x**4.5 + 0.6 * x**3.7 + 0.4 * x**2.9 + 0.2 * x**2.1) / self.dim)
        
        # Saddle point structure with chaotic sine-cosine coupling
        f4 = 0.28 * np.sum(np.sin(18.0 * x) * np.cos(15.0 * x) * np.exp(-0.25 * x**2))
        
        # Cross-dimensional interaction with asymmetric coupling
        f5 = 0.12 * np.sum(np.sin(x[:-1] * x[1:]) * np.cos(0.9 * x[:-1] + 1.1 * x[1:]))
        
        # Fractal-like recursive interference with varying scales
        f6 = 0.18 * np.sum(np.sin(30.0 * np.sin(6.0 * x)) * np.cos(25.0 * np.cos(5.0 * x)))
        
        # Asymmetric polynomial with exponential weighting
        f7 = 0.20 * np.sum((x**4.0 + 0.4 * x**2.8 - 0.2 * x) * np.exp(-0.15 * np.abs(x)))
        
        # Multi-scale harmonic modulation with varying frequencies and amplitudes
        f8 = 0.14 * np.sum(np.sin(35.0 * x + np.sin(18.0 * x)) * np.cos(30.0 * x + np.cos(12.0 * x)))
        
        # Additional chaotic modulation with increased complexity
        f9 = 0.1 * np.sum(np.sin(20.0 * np.sin(3.0 * x)) * np.cos(15.0 * np.cos(2.0 * x)) * np.exp(-0.1 * x**2))
        
        # Combine all components with carefully tuned weights for enhanced complexity
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9