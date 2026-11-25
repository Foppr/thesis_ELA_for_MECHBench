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
        exponents = 2.5 + 0.4 * np.sin(x)
        f3 = 0.3 * np.sum(x**exponents / self.dim)
        
        # Cross-dimensional coupling with varying weights (significantly modified)
        weights = 1.5 + 0.25 * np.cos(0.4 * x[:-1] + 0.5 * x[1:])  # Increased base weight
        f4 = 0.25 * np.sum(weights * x[:-1] * x[1:] / self.dim)
        
        # Multi-scale harmonic interference with chaotic modulation
        f5 = 0.2 * np.sum(np.sin(12.0 * x + np.cos(6.0 * x)) * np.cos(10.0 * x - np.sin(5.0 * x)) * 
                          (1.0 + 0.15 * np.sin(3.5 * np.sum(x))))
        
        # Asymmetric exponential modulation with adaptive scaling
        f6 = 0.25 * np.sum((np.exp(0.6 * x) - np.exp(-0.4 * x)) * np.sin(3.5 * x) * 
                         (1.0 + 0.08 * np.cos(2.5 * x)))
        
        # Dynamic polynomial with adaptive coefficients and fractional powers
        coeffs = 1.2 + 0.15 * np.cos(x)
        f7 = 0.22 * np.sum((coeffs * x**3.5 + 0.6 * x**2.8) / self.dim)
        
        # Fractional cross-dimensional interaction with variable exponents (heavily modified)
        f8 = 0.15 * np.sum((x[:-1]**2.0 * x[1:]**2.5 + x[:-1]**2.7 * x[1:]**1.9) / self.dim)
        
        # Chaotic sine-cosine coupling with time-varying parameters and feedback
        f9 = 0.2 * np.sum(np.sin(18.0 * x + np.sin(8.0 * x)) * np.cos(15.0 * x - np.cos(7.0 * x)) * 
                          (1.0 + 0.12 * np.sin(0.6 * np.sum(x))))
        
        # Combined adaptive structure with enhanced non-separability
        f10 = 0.15 * np.sum(np.exp(-0.15 * np.abs(x)) * np.sin(25.0 * x) * np.cos(20.0 * x) * 
                          (1.0 + 0.2 * np.cos(0.8 * x)))
        
        # Additional chaotic interference term for increased complexity
        f11 = 0.1 * np.sum(np.sin(30.0 * x + np.cos(15.0 * x)) * np.cos(25.0 * x - np.sin(12.0 * x)) * 
                           np.sin(0.4 * np.sum(x**2)))
        
        # Enhanced cross-dimensional coupling with sine-cosine interaction (heavily modified frequencies)
        f12 = 0.18 * np.sum(np.sin(0.7 * x[:-1] + 0.4 * x[1:]) * np.cos(0.5 * x[:-1] - 0.7 * x[1:]) * 
                           (1.0 + 0.15 * np.sin(2.5 * np.sum(x))))
        
        # Additional sine-cosine coupling with modified frequencies and weights
        f13 = 0.13 * np.sum(np.sin(2.5 * x[:-1] + 0.8 * x[1:]) * np.cos(1.8 * x[:-1] - 0.9 * x[1:]) * 
                          (1.0 + 0.08 * np.sin(3.5 * np.sum(x))))
        
        # Modified chaotic interference with different scaling
        f14 = 0.12 * np.sum(np.sin(20.0 * x + np.cos(10.0 * x)) * np.cos(18.0 * x - np.sin(9.0 * x)) * 
                           np.cos(0.25 * np.sum(x**3)))
        
        # Novel fractional harmonic interactions with resonance (heavily modified exponents)
        f15 = 0.14 * np.sum(np.sin(2.5 * x**1.5) * np.cos(2.0 * x**1.6) * 
                          (1.0 + 0.12 * np.sin(0.7 * np.sum(x**2.3))))
        
        # Dynamic resonance terms with time-varying coupling (heavily modified parameters)
        f16 = 0.09 * np.sum(np.sin(3.5 * x + 0.6 * np.sin(2.5 * x)) * 
                          np.cos(3.0 * x - 0.5 * np.cos(2.0 * x)) * 
                          (1.0 + 0.09 * np.cos(0.9 * np.sum(x**1.9))))
        
        # Enhanced fractional cross-dimensional interactions with multiple exponents
        f17 = 0.12 * np.sum((x[:-1]**2.5 * x[1:]**2.1 + x[:-1]**1.8 * x[1:]**2.9) / self.dim)
        
        # Adaptive harmonic modulation with dynamic phase shifts (heavily modified parameters)
        f18 = 0.16 * np.sum(np.sin(4.5 * x + 0.4 * np.cos(3.5 * x)) * 
                          np.cos(4.0 * x - 0.3 * np.sin(3.0 * x)) * 
                          (1.0 + 0.15 * np.sin(0.5 * np.sum(x**2.7))))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13 + f14 + f15 + f16 + f17 + f18