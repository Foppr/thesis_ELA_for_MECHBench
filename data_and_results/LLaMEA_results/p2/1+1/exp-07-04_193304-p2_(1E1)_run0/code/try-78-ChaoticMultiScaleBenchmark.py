import numpy as np

class ChaoticMultiScaleBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_norm**2)
        
        # High-frequency sinusoidal components with varying amplitudes
        f2 = 2.0 * np.sum(np.sin(20 * x_norm) * np.cos(15 * x_norm))
        
        # Polynomial interaction with mixed degrees
        f3 = 0.5 * np.sum(x_norm**3 + x_norm**5 + x_norm**7)
        
        # Exponential decay with varying rates
        f4 = 0.3 * np.sum(np.exp(-3.0 * np.abs(x_norm)) + np.exp(-5.0 * x_norm**2))
        
        # Chaotic interaction using sine and cosine combinations
        f5 = 0.4 * np.sum(np.sin(25 * x_norm) * np.cos(20 * x_norm) * np.sin(10 * x_norm))
        
        # Cross-dimensional interaction with different jump sizes
        f6 = 0.2 * np.sum((x_norm[:-1] - 0.5 * x_norm[1:])**2 + (x_norm[:-2] - 0.3 * x_norm[2:])**2)
        
        # Multi-scale sinusoidal with varying frequencies and amplitudes
        f7 = 0.6 * np.sum(np.sin(30 * x_norm) + 0.5 * np.cos(40 * x_norm) + 0.3 * np.sin(50 * x_norm))
        
        # Additional chaotic component with polynomial modulation
        f8 = 0.3 * np.sum(np.sin(15 * x_norm**2) * np.cos(10 * x_norm**3))
        
        # Mixed power and exponential terms
        f9 = 0.2 * np.sum(np.abs(x_norm)**4 + np.exp(-2.0 * np.abs(x_norm)))
        
        # Complex interaction with multiple dimensional jumps
        f10 = 0.25 * np.sum((x_norm[:-3] - 0.2 * x_norm[3:])**2 + (x_norm[:-4] - 0.1 * x_norm[4:])**2)
        
        # High-order polynomial with alternating signs
        f11 = 0.15 * np.sum(x_norm**6 - x_norm**8 + x_norm**10)
        
        # Additional chaotic sine-cosine interaction with different phase shifts
        f12 = 0.35 * np.sum(np.sin(35 * x_norm + np.pi/4) * np.cos(25 * x_norm + np.pi/3))
        
        # Exponential term with variable base
        f13 = 0.2 * np.sum(np.exp(-4.0 * x_norm**2) + np.exp(-6.0 * np.abs(x_norm)))
        
        # Multi-scale sinusoidal with irregular amplitude modulation
        f14 = 0.4 * np.sum(np.sin(40 * x_norm) * (1 + 0.2 * np.sin(10 * x_norm)))
        
        # Additional cross-term with non-linear interaction
        f15 = 0.1 * np.sum((x_norm[:-1] * x_norm[1:] + 0.5 * x_norm[:-2] * x_norm[2:])**2)
        
        # High-frequency oscillation with amplitude decay
        f16 = 0.3 * np.sum(np.sin(60 * x_norm) * np.exp(-0.5 * x_norm**2))
        
        # Mixed trigonometric and polynomial with different scales
        f17 = 0.25 * np.sum(np.sin(20 * x_norm**2) + x_norm**4)
        
        # Additional chaotic interaction with complex phase relationships
        f18 = 0.3 * np.sum(np.sin(30 * x_norm) * np.cos(35 * x_norm) * np.sin(25 * x_norm))
        
        # Exponential decay with variable rate
        f19 = 0.15 * np.sum(np.exp(-7.0 * np.abs(x_norm)) + np.exp(-8.0 * x_norm**2))
        
        # Multi-scale interaction with different dimensional jumps
        f20 = 0.2 * np.sum((x_norm[:-5] - 0.1 * x_norm[5:])**2 + (x_norm[:-6] - 0.05 * x_norm[6:])**2)
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13 + f14 + f15 + f16 + f17 + f18 + f19 + f20