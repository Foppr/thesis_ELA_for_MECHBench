import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Exponential decay interaction terms
        f1 = np.sum(np.exp(-np.abs(x_norm)) * x_norm**2)
        
        # Sinusoidal modulation with varying frequencies
        f2 = np.sum(np.sin(2 * np.pi * x_norm) * np.cos(5 * np.pi * x_norm))
        
        # Chaotic logistic map inspired term
        f3 = 0.5 * np.sum(np.sin(np.pi * x_norm) * np.cos(np.pi * x_norm) * x_norm**3)
        
        # Saddle-point inducing cross-terms
        f4 = 0.3 * np.sum((x_norm[:-1]**2 - x_norm[1:]**2)**2)
        
        # Asymmetric exponential penalty
        f5 = 0.2 * np.sum(np.exp(2 * np.abs(x_norm)) - 2 * np.abs(x_norm) - 1)
        
        # Multi-scale oscillation
        f6 = 0.1 * np.sum(np.sin(10 * x_norm) * np.cos(3 * x_norm))
        
        # Mixed power and exponential
        f7 = 0.05 * np.sum(np.abs(x_norm)**3 * np.exp(-x_norm**2))
        
        # High-order polynomial with alternating signs
        f8 = 0.08 * np.sum((-1)**np.arange(self.dim) * x_norm**7)
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8