import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameter
        self.r = 3.99
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Polynomial terms
        f1 = np.sum(x_norm**2)
        f2 = 0.5 * np.sum(x_norm**4)
        f3 = 0.1 * np.sum(x_norm**6)
        
        # Sinusoidal components with varying frequencies
        f4 = 0.3 * np.sum(np.sin(10 * x_norm))
        f5 = 0.2 * np.sum(np.cos(15 * x_norm))
        f6 = 0.15 * np.sum(np.sin(20 * x_norm))
        
        # Cross-terms to increase conditioning
        f7 = 0.1 * np.sum(x_norm[:-1] * x_norm[1:])
        f8 = 0.05 * np.sum((x_norm[:-2] - x_norm[2:])**2)
        
        # Chaotic component using logistic map
        chaotic = np.zeros_like(x_norm)
        x_chaos = 0.5 * np.ones_like(x_norm)
        for _ in range(10):
            x_chaos = self.r * x_chaos * (1 - x_chaos)
        chaotic = x_chaos
        
        # Integrate chaotic signal into objective
        f9 = 0.2 * np.sum(chaotic * x_norm)
        
        # Gaussian-like penalty for large values
        f10 = 0.1 * np.sum(np.exp(-0.5 * x_norm**2))
        
        # Exponential barrier for boundary avoidance
        f11 = 0.05 * np.sum(np.exp(2.0 * (1 - np.abs(x_norm))))
        
        # Interaction between distant variables
        if self.dim > 3:
            f12 = 0.03 * np.sum(x_norm[:-3] * x_norm[3:])
        else:
            f12 = 0.0
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12