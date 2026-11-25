import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base conditioning term with quadratic growth
        f1 = 0.5 * np.sum(x**2) / self.dim
        
        # Exponential decay modulated by trigonometric interference
        f2 = 0.35 * np.sum(np.exp(-0.5 * np.abs(x)) * np.sin(12.0 * x) * np.cos(8.0 * x))
        
        # Polynomial modulation with fractional powers and asymmetric coefficients
        f3 = 0.22 * np.sum((x**4.5 + 0.8 * x**3.7 + 0.4 * x**2.9 + 0.15 * x**2.1) / self.dim)
        
        # Saddle point structure with chaotic sine-cosine coupling
        f4 = 0.28 * np.sum(np.sin(18.0 * x) * np.cos(15.0 * x) * np.exp(-0.35 * x**2))
        
        # Cross-dimensional interaction with asymmetric coupling
        f5 = 0.12 * np.sum(np.sin(x[:-1] * x[1:]) * np.cos(0.9 * x[:-1] + 1.3 * x[1:]))
        
        # Fractal-like recursive interference with varying scales
        f6 = 0.18 * np.sum(np.sin(28.0 * np.sin(6.0 * x)) * np.cos(23.0 * np.cos(5.0 * x)))
        
        # Asymmetric polynomial with exponential weighting
        f7 = 0.20 * np.sum((x**4.0 + 0.6 * x**2.8 - 0.35 * x) * np.exp(-0.25 * np.abs(x)))
        
        # Multi-scale harmonic modulation with varying frequencies and amplitudes
        f8 = 0.14 * np.sum(np.sin(33.0 * x + np.sin(18.0 * x)) * np.cos(28.0 * x + np.cos(12.0 * x)))
        
        # Additional chaotic coupling with higher frequency oscillations
        f9 = 0.25 * np.sum(np.sin(45.0 * x) * np.cos(40.0 * x) * np.exp(-0.15 * np.abs(x)))
        
        # Fractional power cross-dimensional interactions
        f10 = 0.17 * np.sum((x[:-1]**2.0 * x[1:]**2.5 + x[:-1]**3.0 * x[1:]**1.7) / self.dim)
        
        # Combined chaotic interference with dynamic scaling
        f11 = 0.12 * np.sum(np.sin(55.0 * np.sin(9.0 * x)) * np.cos(45.0 * np.cos(7.0 * x)) * np.exp(-0.25 * x**2))
        
        # Asymmetric fractional polynomial with mixed curvature
        f12 = 0.20 * np.sum((x**4.1 + 0.7 * x**3.3 - 0.45 * x**2.4 + 0.25 * x**1.5) * np.exp(-0.2 * np.abs(x)))
        
        # Enhanced cross-dimensional coupling with sine-cosine modulation
        f13 = 0.15 * np.sum(np.sin(22.0 * x[:-1] + 17.0 * x[1:]) * np.cos(20.0 * x[:-1] - 14.0 * x[1:]))
        
        # Multi-scale chaotic interference with exponential weighting
        f14 = 0.22 * np.sum(np.exp(-0.3 * np.abs(x)) * np.sin(38.0 * x) * np.cos(33.0 * x))
        
        # Combine all components with carefully tuned weights for enhanced complexity
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13 + f14