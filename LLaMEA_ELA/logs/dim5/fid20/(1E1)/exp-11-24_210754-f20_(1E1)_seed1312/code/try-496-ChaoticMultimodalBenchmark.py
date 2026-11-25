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
        f2 = 0.4 * np.sum(np.exp(-0.7 * np.abs(x)) * np.sin(15.0 * x) * np.cos(11.0 * x))
        
        # Stronger polynomial modulation with higher fractional powers and asymmetric coefficients
        f3 = 0.3 * np.sum((x**5.1 + 0.8 * x**4.3 + 0.6 * x**3.7 + 0.4 * x**2.9 + 0.2 * x**1.8) / self.dim)
        
        # Enhanced saddle point structure with chaotic sine-cosine coupling
        f4 = 0.3 * np.sum(np.sin(20.0 * x) * np.cos(15.0 * x) * np.exp(-0.4 * x**2))
        
        # Stronger cross-dimensional interaction with asymmetric coupling and additional terms
        f5 = 0.2 * np.sum(np.sin(x[:-1] * x[1:]) * np.cos(1.2 * x[:-1] + 1.8 * x[1:]) + 
                          np.sin(0.7 * x[:-1]) * np.cos(0.9 * x[1:]))
        
        # Enhanced fractal-like recursive interference with varying scales and additional harmonics
        f6 = 0.25 * np.sum(np.sin(30.0 * np.sin(7.0 * x)) * np.cos(25.0 * np.cos(6.0 * x)) + 
                           np.sin(18.0 * np.sin(4.0 * x)) * np.cos(15.0 * np.cos(3.0 * x)))
        
        # Enhanced asymmetric polynomial with exponential weighting and additional terms
        f7 = 0.25 * np.sum((x**4.1 + 0.6 * x**3.2 - 0.4 * x**2.1 + 0.1 * x) * np.exp(-0.3 * np.abs(x)))
        
        # Multi-scale harmonic modulation with varying frequencies, amplitudes, and phase shifts
        f8 = 0.2 * np.sum(np.sin(35.0 * x + np.sin(20.0 * x)) * np.cos(30.0 * x + np.cos(15.0 * x)) + 
                          np.sin(25.0 * x + np.sin(10.0 * x)) * np.cos(20.0 * x + np.cos(8.0 * x)))
        
        # Additional chaotic interference term with higher frequency modulation
        f9 = 0.15 * np.sum(np.sin(40.0 * np.sin(8.0 * x)) * np.cos(35.0 * np.cos(7.0 * x)) * 
                           np.exp(-0.2 * x**2))
        
        # Combined with novel coupling term for increased dimensionality interaction
        f10 = 0.1 * np.sum(np.sin(2.0 * x[:-1] + 3.0 * x[1:]) * np.cos(1.5 * x[:-1] - 2.5 * x[1:]) * 
                           np.exp(-0.1 * (x[:-1]**2 + x[1:]**2)))
        
        # Combine all components with carefully tuned weights for enhanced complexity
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10