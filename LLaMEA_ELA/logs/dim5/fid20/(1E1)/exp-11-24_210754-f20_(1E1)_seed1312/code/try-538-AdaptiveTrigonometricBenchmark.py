import numpy as np

class AdaptiveTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = 0.3 * np.sum(x**2) / self.dim
        
        # Adaptive trigonometric modulation with dynamic frequency
        freq = 2.5 + 0.7 * np.sin(0.6 * np.sum(x))
        f2 = 0.45 * np.sum(np.sin(freq * x) * np.cos(1.8 * x))
        
        # Polynomial shaping with adaptive exponents
        exponents = 2.2 + 0.4 * np.sin(x)
        f3 = 0.28 * np.sum(x**exponents / self.dim)
        
        # Cross-dimensional coupling with varying weights
        weights = 1.2 + 0.3 * np.cos(0.4 * x[:-1] + 0.5 * x[1:])
        f4 = 0.22 * np.sum(weights * x[:-1] * x[1:] / self.dim)
        
        # Multi-scale harmonic interference with chaotic modulation
        f5 = 0.18 * np.sum(np.sin(12.0 * x + np.cos(6.0 * x)) * np.cos(9.0 * x - np.sin(5.0 * x)) * 
                          (1.0 + 0.12 * np.sin(3.5 * np.sum(x))))
        
        # Asymmetric exponential modulation with adaptive scaling
        f6 = 0.22 * np.sum((np.exp(0.6 * x) - np.exp(-0.4 * x)) * np.sin(3.5 * x) * 
                         (1.0 + 0.06 * np.cos(2.5 * x)))
        
        # Dynamic polynomial with adaptive coefficients and fractional powers
        coeffs = 1.2 + 0.15 * np.cos(x)
        f7 = 0.20 * np.sum((coeffs * x**3.5 + 0.6 * x**2.8) / self.dim)
        
        # Fractional cross-dimensional interaction with variable exponents
        f8 = 0.14 * np.sum((x[:-1]**2.0 * x[1:]**2.3 + x[:-1]**2.7 * x[1:]**1.9) / self.dim)
        
        # Chaotic sine-cosine coupling with time-varying parameters and feedback
        f9 = 0.18 * np.sum(np.sin(16.0 * x + np.sin(8.0 * x)) * np.cos(13.0 * x - np.cos(7.0 * x)) * 
                          (1.0 + 0.09 * np.sin(0.6 * np.sum(x))))
        
        # Combined adaptive structure with enhanced non-separability
        f10 = 0.12 * np.sum(np.exp(-0.12 * np.abs(x)) * np.sin(22.0 * x) * np.cos(20.0 * x) * 
                          (1.0 + 0.17 * np.cos(0.8 * x)))
        
        # Additional chaotic interference term for increased complexity
        f11 = 0.09 * np.sum(np.sin(27.0 * x + np.cos(14.0 * x)) * np.cos(24.0 * x - np.sin(12.0 * x)) * 
                           np.sin(0.35 * np.sum(x**2)))
        
        # Enhanced cross-dimensional coupling with sine-cosine interaction
        f12 = 0.16 * np.sum(np.sin(0.6 * x[:-1] + 0.4 * x[1:]) * np.cos(0.5 * x[:-1] - 0.7 * x[1:]) * 
                           (1.0 + 0.12 * np.sin(2.2 * np.sum(x))))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12