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
        freq = 2.0 + 0.5 * np.sin(0.5 * np.sum(x))
        f2 = 0.4 * np.sum(np.sin(freq * x) * np.cos(1.5 * x))
        
        # Polynomial shaping with adaptive exponents
        exponents = 2.0 + 0.3 * np.sin(x)
        f3 = 0.25 * np.sum(x**exponents / self.dim)
        
        # Cross-dimensional coupling with varying weights
        weights = 1.0 + 0.2 * np.cos(0.3 * x[:-1] + 0.4 * x[1:])
        f4 = 0.2 * np.sum(weights * x[:-1] * x[1:] / self.dim)
        
        # Multi-scale harmonic interference with chaotic modulation
        f5 = 0.15 * np.sum(np.sin(10.0 * x + np.cos(5.0 * x)) * np.cos(8.0 * x - np.sin(4.0 * x)) * 
                          (1.0 + 0.1 * np.sin(3.0 * np.sum(x))))
        
        # Asymmetric exponential modulation with adaptive scaling
        f6 = 0.2 * np.sum((np.exp(0.5 * x) - np.exp(-0.3 * x)) * np.sin(3.0 * x) * 
                         (1.0 + 0.05 * np.cos(2.0 * x)))
        
        # Dynamic polynomial with adaptive coefficients and fractional powers
        coeffs = 1.0 + 0.1 * np.cos(x)
        f7 = 0.18 * np.sum((coeffs * x**3.2 + 0.5 * x**2.5) / self.dim)
        
        # Fractional cross-dimensional interaction with variable exponents
        f8 = 0.12 * np.sum((x[:-1]**1.7 * x[1:]**2.1 + x[:-1]**2.4 * x[1:]**1.6) / self.dim)
        
        # Chaotic sine-cosine coupling with time-varying parameters and feedback
        f9 = 0.16 * np.sum(np.sin(15.0 * x + np.sin(7.0 * x)) * np.cos(12.0 * x - np.cos(6.0 * x)) * 
                          (1.0 + 0.08 * np.sin(0.5 * np.sum(x))))
        
        # Combined adaptive structure with enhanced non-separability
        f10 = 0.1 * np.sum(np.exp(-0.1 * np.abs(x)) * np.sin(20.0 * x) * np.cos(18.0 * x) * 
                          (1.0 + 0.15 * np.cos(0.7 * x)))
        
        # Additional chaotic interference term for increased complexity
        f11 = 0.08 * np.sum(np.sin(25.0 * x + np.cos(13.0 * x)) * np.cos(22.0 * x - np.sin(11.0 * x)) * 
                           np.sin(0.3 * np.sum(x**2)))
        
        # Enhanced cross-dimensional coupling with sine-cosine interaction
        f12 = 0.14 * np.sum(np.sin(0.5 * x[:-1] + 0.3 * x[1:]) * np.cos(0.4 * x[:-1] - 0.6 * x[1:]) * 
                           (1.0 + 0.1 * np.sin(2.0 * np.sum(x))))
        
        # Additional sine-cosine coupling with modified frequencies and weights
        f13 = 0.1 * np.sum(np.sin(2.0 * x[:-1] + 0.7 * x[1:]) * np.cos(1.5 * x[:-1] - 0.8 * x[1:]) * 
                          (1.0 + 0.05 * np.sin(3.0 * np.sum(x))))
        
        # Modified chaotic interference with different scaling
        f14 = 0.09 * np.sum(np.sin(18.0 * x + np.cos(9.0 * x)) * np.cos(16.0 * x - np.sin(8.0 * x)) * 
                           np.cos(0.2 * np.sum(x**3)))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13 + f14