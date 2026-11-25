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
        freq = 2.5 + 0.3 * np.sin(0.7 * np.sum(x))
        f2 = 0.4 * np.sum(np.sin(freq * x) * np.cos(1.8 * x))
        
        # Polynomial shaping with adaptive exponents
        exponents = 2.2 + 0.2 * np.sin(x)
        f3 = 0.25 * np.sum(x**exponents / self.dim)
        
        # Cross-dimensional coupling with varying weights (slightly modified)
        weights = 1.3 + 0.1 * np.cos(0.4 * x[:-1] + 0.5 * x[1:])  # Increased base weight
        f4 = 0.2 * np.sum(weights * x[:-1] * x[1:] / self.dim)
        
        # Multi-scale harmonic interference with chaotic modulation
        f5 = 0.15 * np.sum(np.sin(12.0 * x + np.cos(6.0 * x)) * np.cos(9.0 * x - np.sin(5.0 * x)) * 
                          (1.0 + 0.12 * np.sin(3.5 * np.sum(x))))
        
        # Asymmetric exponential modulation with adaptive scaling
        f6 = 0.2 * np.sum((np.exp(0.6 * x) - np.exp(-0.4 * x)) * np.sin(3.5 * x) * 
                         (1.0 + 0.06 * np.cos(2.5 * x)))
        
        # Dynamic polynomial with adaptive coefficients and fractional powers
        coeffs = 1.1 + 0.08 * np.cos(x)
        f7 = 0.18 * np.sum((coeffs * x**3.0 + 0.6 * x**2.3) / self.dim)
        
        # Fractional cross-dimensional interaction with variable exponents (modified)
        f8 = 0.12 * np.sum((x[:-1]**1.8 * x[1:]**2.2 + x[:-1]**2.5 * x[1:]**1.7) / self.dim)
        
        # Chaotic sine-cosine coupling with time-varying parameters and feedback
        f9 = 0.16 * np.sum(np.sin(14.0 * x + np.sin(8.0 * x)) * np.cos(13.0 * x - np.cos(7.0 * x)) * 
                          (1.0 + 0.09 * np.sin(0.6 * np.sum(x))))
        
        # Combined adaptive structure with enhanced non-separability
        f10 = 0.1 * np.sum(np.exp(-0.12 * np.abs(x)) * np.sin(22.0 * x) * np.cos(19.0 * x) * 
                          (1.0 + 0.16 * np.cos(0.8 * x)))
        
        # Additional chaotic interference term for increased complexity
        f11 = 0.08 * np.sum(np.sin(24.0 * x + np.cos(14.0 * x)) * np.cos(23.0 * x - np.sin(12.0 * x)) * 
                           np.sin(0.35 * np.sum(x**2)))
        
        # Enhanced cross-dimensional coupling with sine-cosine interaction (modified frequencies)
        f12 = 0.14 * np.sum(np.sin(0.7 * x[:-1] + 0.4 * x[1:]) * np.cos(0.5 * x[:-1] - 0.7 * x[1:]) * 
                           (1.0 + 0.12 * np.sin(2.2 * np.sum(x))))
        
        # Additional sine-cosine coupling with modified frequencies and weights
        f13 = 0.1 * np.sum(np.sin(2.5 * x[:-1] + 0.8 * x[1:]) * np.cos(1.7 * x[:-1] - 0.9 * x[1:]) * 
                          (1.0 + 0.06 * np.sin(3.2 * np.sum(x))))
        
        # Modified chaotic interference with different scaling
        f14 = 0.09 * np.sum(np.sin(19.0 * x + np.cos(10.0 * x)) * np.cos(17.0 * x - np.sin(9.0 * x)) * 
                           np.cos(0.25 * np.sum(x**3)))
        
        # Novel fractional harmonic interactions with resonance (modified exponents)
        f15 = 0.11 * np.sum(np.sin(2.2 * x**1.4) * np.cos(1.8 * x**1.5) * 
                          (1.0 + 0.09 * np.sin(0.65 * np.sum(x**2.1))))
        
        # Dynamic resonance terms with time-varying coupling (modified parameters)
        f16 = 0.07 * np.sum(np.sin(3.2 * x + 0.55 * np.sin(2.2 * x)) * 
                          np.cos(2.7 * x - 0.45 * np.cos(1.6 * x)) * 
                          (1.0 + 0.065 * np.cos(0.85 * np.sum(x**1.8))))
        
        # Enhanced fractional cross-dimensional interactions with multiple exponents
        f17 = 0.09 * np.sum((x[:-1]**2.4 * x[1:]**2.0 + x[:-1]**1.6 * x[1:]**2.8) / self.dim)
        
        # Adaptive harmonic modulation with dynamic phase shifts (modified parameters)
        f18 = 0.13 * np.sum(np.sin(4.2 * x + 0.35 * np.cos(3.2 * x)) * 
                          np.cos(3.7 * x - 0.25 * np.sin(2.7 * x)) * 
                          (1.0 + 0.11 * np.sin(0.45 * np.sum(x**2.5))))
        
        # Additional harmonic resonance term with modified scaling and coupling
        f19 = 0.06 * np.sum(np.sin(5.2 * x**1.3) * np.cos(4.2 * x**1.2) * 
                          (1.0 + 0.075 * np.sin(0.55 * np.sum(x**2.3))) * 
                          (1.0 + 0.045 * np.cos(0.35 * np.sum(x**1.9))))
        
        # Enhanced chaotic modulation with modified feedback and phase coupling
        f20 = 0.08 * np.sum(np.sin(21.0 * x + np.cos(11.0 * x)) * 
                          np.cos(19.0 * x - np.sin(10.0 * x)) * 
                          (1.0 + 0.095 * np.sin(0.45 * np.sum(x**2.7))) * 
                          (1.0 + 0.035 * np.cos(0.25 * np.sum(x**1.6))))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13 + f14 + f15 + f16 + f17 + f18 + f19 + f20