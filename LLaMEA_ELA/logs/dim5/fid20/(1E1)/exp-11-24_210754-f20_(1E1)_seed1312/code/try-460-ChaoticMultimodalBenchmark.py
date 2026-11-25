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
        f2 = 0.4 * np.sum(np.exp(-0.7 * np.abs(x)) * np.sin(12.0 * x) * np.cos(9.0 * x))
        
        # Polynomial modulation with higher-order fractional powers and asymmetric coefficients
        f3 = 0.25 * np.sum((x**5.1 + 0.8 * x**4.3 + 0.6 * x**3.7 + 0.4 * x**2.9 + 0.2 * x**1.8) / self.dim)
        
        # Saddle point structure with chaotic sine-cosine coupling and fractal scaling
        f4 = 0.3 * np.sum(np.sin(18.0 * x) * np.cos(15.0 * x) * np.exp(-0.4 * x**2))
        
        # Stronger cross-dimensional interaction with asymmetric coupling and harmonic modulation
        f5 = 0.2 * np.sum(np.sin(x[:-1] * x[1:]) * np.cos(0.9 * x[:-1] + 1.3 * x[1:]) * np.exp(-0.1 * np.abs(x[:-1] - x[1:])))
        
        # Fractal-like recursive interference with multiple scales and enhanced chaos
        f6 = 0.2 * np.sum(np.sin(30.0 * np.sin(6.0 * x)) * np.cos(25.0 * np.cos(5.0 * x)) * np.exp(-0.15 * x**2))
        
        # Asymmetric polynomial with exponential weighting and additional harmonic term
        f7 = 0.22 * np.sum((x**4.1 + 0.6 * x**3.2 - 0.4 * x**2.1 + 0.1 * x) * np.exp(-0.25 * np.abs(x)))
        
        # Multi-scale harmonic modulation with increased frequency and amplitude variations
        f8 = 0.15 * np.sum(np.sin(35.0 * x + np.sin(20.0 * x)) * np.cos(30.0 * x + np.cos(15.0 * x)))
        
        # Additional chaotic coupling term with higher-order trigonometric interactions
        f9 = 0.18 * np.sum(np.sin(22.0 * np.sin(8.0 * x)) * np.cos(18.0 * np.cos(7.0 * x)) * np.exp(-0.3 * x**2))
        
        # Cross-dimensional coupling with exponential weighting and polynomial modulation
        f10 = 0.12 * np.sum(np.exp(-0.5 * np.abs(x[:-1] - x[1:])) * (x[:-1]**2.5 + x[1:]**3.1) * np.sin(10.0 * x[:-1] + 15.0 * x[1:]))
        
        # Combine all components with carefully tuned weights for enhanced complexity
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10