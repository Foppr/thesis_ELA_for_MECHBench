import numpy as np

class ChaoticRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_norm**2)
        
        # High-frequency sinusoidal components with varying amplitudes
        f2 = 2.0 * np.sum(np.sin(50 * x_norm) * np.cos(30 * x_norm))
        
        # Polynomial penalty with increasing degree
        f3 = 0.5 * np.sum(x_norm**6)
        
        # Cross-dimensional interaction with chaotic coupling
        f4 = 0.3 * np.sum(np.sin(x_norm[:-1] * x_norm[1:]) * np.cos(x_norm[:-1] + x_norm[1:]))
        
        # Multi-scale oscillation with amplitude modulation
        f5 = 1.5 * np.sum(np.sin(20 * x_norm) * np.exp(-0.5 * x_norm**2))
        
        # Complex interaction with 3-dimensional jumps
        f6 = 0.2 * np.sum((x_norm[:-2] - 2 * x_norm[1:-1] + x_norm[2:])**2)
        
        # Chaotic sine-cosine combination with frequency mixing
        f7 = 0.4 * np.sum(np.sin(40 * np.pi * x_norm) * np.cos(25 * np.pi * x_norm) * np.sin(15 * x_norm))
        
        # Exponential decay with sinusoidal modulation
        f8 = 0.3 * np.sum(np.exp(-2.0 * np.abs(x_norm)) * np.sin(35 * x_norm))
        
        # Fifth-order polynomial with alternating signs
        f9 = 0.25 * np.sum(np.sign(x_norm) * np.abs(x_norm)**5)
        
        # Multi-modal term with varying frequencies
        f10 = 0.6 * np.sum(np.cos(60 * x_norm) + np.sin(45 * x_norm))
        
        # Cross-dimensional cubic interaction
        f11 = 0.15 * np.sum((x_norm[:-1] * x_norm[1:]) ** 3)
        
        # High-frequency noise component
        f12 = 0.1 * np.sum(np.sin(100 * x_norm) * np.cos(75 * x_norm))
        
        # Combined penalty with exponential and polynomial terms
        f13 = 0.2 * np.sum(np.exp(-1.5 * x_norm**2) + x_norm**4)
        
        # Fractional power interaction with non-integer exponents
        f14 = 0.3 * np.sum(np.abs(x_norm)**1.5)
        
        # Coupled oscillators with phase shifts
        f15 = 0.25 * np.sum(np.sin(30 * x_norm + 0.5) * np.cos(20 * x_norm - 0.3))
        
        # Hybrid polynomial-trigonometric term
        f16 = 0.1 * np.sum(np.sin(x_norm**2) * np.cos(x_norm))
        
        # Higher-order cross-dimensional interaction
        f17 = 0.1 * np.sum((x_norm[:-3] - x_norm[3:])**4)
        
        # Logarithmic penalty with trigonometric modulation
        f18 = 0.15 * np.sum(np.log(1 + np.abs(x_norm)) * np.sin(25 * x_norm))
        
        # Multi-scale chaotic interaction
        f19 = 0.2 * np.sum(np.sin(50 * x_norm) * np.cos(35 * x_norm) * np.sin(10 * x_norm))
        
        # Combined exponential and polynomial penalty
        f20 = 0.1 * np.sum(np.exp(-x_norm**2) * x_norm**3)
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13 + f14 + f15 + f16 + f17 + f18 + f19 + f20