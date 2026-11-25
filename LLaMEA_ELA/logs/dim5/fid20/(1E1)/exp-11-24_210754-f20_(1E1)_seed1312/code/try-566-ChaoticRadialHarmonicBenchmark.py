import numpy as np

class ChaoticRadialHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base radial term for conditioning
        f1 = 0.2 * np.sum(x**2) / self.dim
        
        # Chaotic exponential modulation with adaptive scaling
        f2 = 0.3 * np.sum(np.exp(0.5 * np.abs(x)) * np.sin(3.0 * x) * 
                         (1.0 + 0.1 * np.cos(2.0 * x)))
        
        # Adaptive radial basis function with dynamic centers
        centers = 2.0 * np.sin(0.3 * np.arange(self.dim))
        f3 = 0.25 * np.sum(np.exp(-0.5 * np.sum((x - centers)**2, axis=0) / (1.0 + 0.2 * np.abs(x))))
        
        # Quaternion-like harmonic interactions with complex coupling
        f4 = 0.2 * np.sum(np.sin(2.0 * x[:-1] + 1.5 * x[1:]) * 
                         np.cos(1.8 * x[:-1] - 1.2 * x[1:]) * 
                         (1.0 + 0.15 * np.sin(0.7 * np.sum(x))))
        
        # Time-varying phase modulation with chaotic feedback
        f5 = 0.18 * np.sum(np.sin(4.0 * x + 0.3 * np.sin(2.0 * x)) * 
                          np.cos(3.5 * x - 0.2 * np.cos(1.5 * x)) * 
                          (1.0 + 0.1 * np.sin(0.5 * np.sum(x**2))))
        
        # Multi-scale exponential interference with adaptive weights
        f6 = 0.15 * np.sum(np.exp(-0.3 * np.abs(x)) * np.cos(5.0 * x) * 
                         (1.0 + 0.08 * np.sin(3.0 * x)))
        
        # Dynamic cross-dimensional coupling with polynomial weights
        weights = 1.5 + 0.2 * np.sin(0.4 * x[:-1] + 0.3 * x[1:])
        f7 = 0.16 * np.sum(weights * x[:-1]**1.5 * x[1:]**1.8 / self.dim)
        
        # Fractional harmonic interactions with variable exponents
        f8 = 0.14 * np.sum(np.sin(2.5 * x**1.3) * np.cos(1.9 * x**1.6) * 
                          (1.0 + 0.1 * np.sin(0.8 * np.sum(x**2.1))))
        
        # Enhanced radial basis with time-varying bandwidth
        f9 = 0.12 * np.sum(np.exp(-0.4 * np.sum((x - 0.5 * np.sin(x))**2, axis=0) / 
                                (0.8 + 0.1 * np.abs(x))))
        
        # Chaotic sine-cosine coupling with adaptive phase shifts
        f10 = 0.1 * np.sum(np.sin(6.0 * x + 0.4 * np.cos(3.0 * x)) * 
                          np.cos(5.0 * x - 0.3 * np.sin(2.5 * x)) * 
                          (1.0 + 0.05 * np.sin(0.6 * np.sum(x**1.8))))
        
        # Adaptive polynomial with dynamic coefficients
        coeffs = 1.2 + 0.15 * np.cos(0.5 * x)
        f11 = 0.13 * np.sum((coeffs * x**3.1 + 0.6 * x**2.7) / self.dim)
        
        # Multi-scale chaotic interference with variable frequencies
        f12 = 0.09 * np.sum(np.sin(8.0 * x + np.cos(4.0 * x)) * 
                           np.cos(7.0 * x - np.sin(3.5 * x)) * 
                           (1.0 + 0.12 * np.sin(0.4 * np.sum(x**2.3))))
        
        # Dynamic resonance terms with adaptive coupling
        f13 = 0.08 * np.sum(np.sin(2.8 * x + 0.6 * np.sin(1.8 * x)) * 
                          np.cos(2.3 * x - 0.5 * np.cos(1.4 * x)) * 
                          (1.0 + 0.09 * np.cos(0.7 * np.sum(x**1.9))))
        
        # Enhanced fractional cross-dimensional interactions
        f14 = 0.11 * np.sum((x[:-1]**2.1 * x[1:]**1.7 + x[:-1]**1.8 * x[1:]**2.2) / self.dim)
        
        # Complex harmonic modulation with dynamic phase coupling
        f15 = 0.07 * np.sum(np.sin(3.2 * x + 0.2 * np.cos(2.8 * x)) * 
                          np.cos(2.9 * x - 0.1 * np.sin(2.3 * x)) * 
                          (1.0 + 0.11 * np.sin(0.6 * np.sum(x**2.4))))
        
        # Adaptive exponential with time-varying modulation
        f16 = 0.1 * np.sum(np.exp(0.4 * x) * np.cos(4.5 * x) * 
                         (1.0 + 0.06 * np.sin(2.0 * x)))
        
        # Novel chaotic radial harmonic with quaternion-like structure
        f17 = 0.09 * np.sum(np.sin(3.0 * x**1.4) * np.cos(2.5 * x**1.5) * 
                          (1.0 + 0.08 * np.sin(0.6 * np.sum(x**2.2))))
        
        # Enhanced cross-dimensional coupling with multiple harmonic terms
        f18 = 0.08 * np.sum(np.sin(1.2 * x[:-1] + 0.8 * x[1:]) * 
                          np.cos(0.9 * x[:-1] - 0.7 * x[1:]) * 
                          (1.0 + 0.05 * np.sin(3.0 * np.sum(x))))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13 + f14 + f15 + f16 + f17 + f18