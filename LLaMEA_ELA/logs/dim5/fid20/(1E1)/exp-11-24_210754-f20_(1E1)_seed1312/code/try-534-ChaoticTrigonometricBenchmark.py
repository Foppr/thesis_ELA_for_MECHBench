import numpy as np

class ChaoticTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base chaotic quadratic term with dynamic conditioning
        f1 = 0.25 * np.sum(np.sin(3.0 * x) * np.cos(2.0 * x)) / self.dim
        
        # Fractional polynomial shaping with time-varying exponents
        exponents = 2.5 + 0.8 * np.sin(0.7 * np.sum(x))
        f2 = 0.3 * np.sum(np.abs(x)**exponents / self.dim)
        
        # Dynamic cross-dimensional coupling with chaotic weights
        weights = 1.5 + 0.5 * np.sin(2.0 * x[:-1] + 1.3 * x[1:] + 0.8 * np.sum(x))
        f3 = 0.25 * np.sum(weights * x[:-1] * x[1:] / self.dim)
        
        # Multi-scale chaotic sine-cosine interference
        f4 = 0.2 * np.sum(np.sin(12.0 * x + np.cos(8.0 * x)) * np.cos(10.0 * x - np.sin(6.0 * x)))
        
        # Asymmetric exponential modulation with chaotic parameters
        f5 = 0.18 * np.sum((np.exp(0.4 * x) - np.exp(-0.6 * x)) * np.sin(4.0 * x + np.cos(2.0 * x)))
        
        # Fractional harmonic coupling with dynamic frequencies
        freq1 = 3.0 + 1.2 * np.sin(0.5 * x[0])
        freq2 = 2.5 + 0.9 * np.cos(0.3 * x[-1])
        f6 = 0.22 * np.sum(np.sin(freq1 * x) * np.cos(freq2 * x) * np.sin(2.0 * x))
        
        # Chaotic polynomial with adaptive coefficients
        coeffs = 1.2 + 0.3 * np.sin(x * 1.5)
        f7 = 0.15 * np.sum((coeffs * x**2.8 + 0.4 * x**2.2) / self.dim)
        
        # Multi-scale fractional cross-dimensional interaction
        f8 = 0.13 * np.sum((x[:-1]**1.9 * x[1:]**2.3 + x[:-1]**2.6 * x[1:]**1.4) / self.dim)
        
        # Coupled chaotic sine-cosine with time-varying phases
        f9 = 0.17 * np.sum(np.sin(18.0 * x + np.sin(9.0 * x)) * np.cos(15.0 * x - np.cos(7.0 * x)))
        
        # Combined chaotic structure with asymmetric modulation
        f10 = 0.12 * np.sum(np.exp(-0.15 * np.abs(x)) * np.sin(25.0 * x) * np.cos(22.0 * x))
        
        # Additional chaotic trigonometric interference
        f11 = 0.08 * np.sum(np.sin(20.0 * x + np.cos(15.0 * x)) * np.cos(18.0 * x - np.sin(12.0 * x)))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11