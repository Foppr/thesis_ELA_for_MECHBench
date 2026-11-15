import numpy as np

class ChaoticAdaptiveBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_norm**2)
        
        # Sinusoidal modulation with adaptive frequency
        f2 = 2.0 * np.sum(np.sin(10 * np.pi * x_norm) * np.cos(15 * np.pi * x_norm))
        
        # Polynomial penalty with increasing degree
        f3 = 0.5 * np.sum(x_norm**3 + 0.3 * x_norm**4 + 0.1 * x_norm**5)
        
        # Chaotic interaction using logistic map-like behavior
        f4 = 1.5 * np.sum(np.sin(20 * np.pi * x_norm) * np.cos(25 * np.pi * x_norm) * 
                         np.sin(30 * np.pi * x_norm) * np.cos(35 * np.pi * x_norm))
        
        # Adaptive conditioning based on dimension
        f5 = 0.8 * np.sum((x_norm[:-1] * x_norm[1:]) * (1 + 0.1 * np.abs(x_norm[:-1] - x_norm[1:])))
        
        # Multi-scale oscillation component
        f6 = 1.2 * np.sum(np.sin(50 * x_norm) + np.cos(60 * x_norm) + 
                         np.sin(70 * x_norm) + np.cos(80 * x_norm))
        
        # Exponential penalty with dimension-dependent scaling
        f7 = 0.6 * np.sum(np.exp(2.0 * np.abs(x_norm)) - 1)
        
        # Cross-dimensional interaction with varying weights
        f8 = 0.4 * np.sum((x_norm[:-2] + x_norm[2:]) * (x_norm[:-1] - x_norm[1:]))
        
        # Fractional power term for non-smooth behavior
        f9 = 0.3 * np.sum(np.abs(x_norm)**1.5)
        
        # Complex trigonometric combination
        f10 = 0.7 * np.sum(np.sin(40 * np.pi * x_norm) * np.cos(50 * np.pi * x_norm) + 
                          np.cos(45 * np.pi * x_norm) * np.sin(55 * np.pi * x_norm))
        
        # Adaptive penalty based on local gradient
        grad_penalty = 0.0
        for i in range(1, self.dim-1):
            grad_penalty += np.abs(x_norm[i+1] - 2*x_norm[i] + x_norm[i-1])
        f11 = 0.5 * grad_penalty
        
        # High-frequency noise component
        f12 = 0.2 * np.sum(np.sin(100 * x_norm) + np.cos(110 * x_norm))
        
        # Mixed polynomial and exponential
        f13 = 0.3 * np.sum(x_norm**6 * np.exp(-0.5 * x_norm**2))
        
        # Dimension-dependent conditioning
        f14 = 0.4 * np.sum(x_norm**2 * (1 + 0.05 * np.abs(x_norm)))
        
        # Sine-cosine interaction with different frequencies
        f15 = 0.6 * np.sum(np.sin(30 * x_norm) * np.cos(40 * x_norm) * 
                          np.sin(50 * x_norm) * np.cos(60 * x_norm))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13 + f14 + f15