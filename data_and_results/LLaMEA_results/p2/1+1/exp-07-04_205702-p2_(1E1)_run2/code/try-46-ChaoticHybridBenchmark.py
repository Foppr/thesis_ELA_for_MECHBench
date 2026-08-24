import numpy as np

class ChaoticHybridBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Periodic component with varying frequencies and amplitudes
        f1 = np.sum(np.sin(2.0 * np.pi * x) * np.cos(3.0 * np.pi * x) * np.exp(-0.1 * np.sum(x**2)))
        
        # Exponential decay with sinusoidal modulation
        f2 = np.sum(np.exp(-0.5 * x**2) * np.sin(5.0 * x) * np.cos(2.0 * x))
        
        # Polynomial with chaotic scaling factors
        f3 = np.sum((x**4 + 0.5 * x**3 + 0.2 * x**2 + 0.1 * x + 0.05) * np.sin(0.5 * x))
        
        # Multi-modal Gaussian with dynamic centers and variances
        f4 = 0.0
        for i in range(self.dim):
            center = 2.0 * np.sin(0.3 * i)
            variance = 0.5 + 0.3 * np.cos(0.4 * i)
            f4 -= np.exp(-0.5 * ((x[i] - center) / variance)**2) * np.sin(3.0 * x[i])
        
        # Cross-dimensional interaction with chaotic coupling weights
        f5 = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                weight = 0.5 + 0.5 * np.sin(0.2 * i + 0.3 * j)
                f5 += weight * np.sin(x[i] * x[j]) * np.exp(-0.2 * (x[i] - x[j])**2)
        
        # Fractional-order chaotic component
        f6 = np.sum(np.sin(x**0.7) * np.cos(x**1.3) * np.exp(-0.05 * np.sum(np.abs(x)**0.8)))
        
        # High-frequency oscillation component
        f7 = 0.5 * np.sum(np.sin(20.0 * x) * np.cos(15.0 * x) * np.exp(-0.02 * np.sum(x**2)))
        
        # Saddle point inducing component
        f8 = 0.3 * np.sum(np.sin(x) * np.cos(x) * np.exp(-0.1 * np.sum(x**2)))
        
        # Asymmetric conditioning
        f9 = 0.2 * np.sum(np.abs(x)**2.5 * np.sin(0.4 * x))
        
        # Combined chaotic interaction
        f10 = 0.1 * np.sum(np.sin(x) * np.cos(x**2) * np.tan(0.1 * x) * np.exp(-0.03 * np.sum(x**3)))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10