import numpy as np

class CorrelatedPeriodicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for consistent conditioning
        x_scaled = x / 5.0
        
        # Exponentially decaying correlation structure across dimensions
        f1 = 0.0
        for i in range(self.dim):
            decay_factor = np.exp(-i / (self.dim * 0.5))
            f1 += decay_factor * x_scaled[i]**2
        
        # Periodic modulation with varying frequencies and amplitudes
        f2 = 0.0
        for i in range(self.dim):
            freq = 2 * np.pi * (i + 1) / self.dim
            amp = 1.0 / (i + 1)
            f2 += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i])
        
        # Central attractive basin with Gaussian potential well
        center = np.zeros(self.dim)
        sigma = 1.5
        f3 = -np.exp(-0.5 * np.sum((x_scaled - center)**2) / sigma**2)
        
        # Cross-dimensional interaction with exponentially weighted terms
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = np.exp(-abs(i - j) / (self.dim * 0.3))
                f4 += weight * np.sin(x_scaled[i]) * np.cos(x_scaled[j])
        
        # Asymmetric penalty term with varying exponents
        f5 = 0.0
        for i in range(self.dim):
            exp = 1.5 + 0.5 * np.sin(i)
            f5 += 0.3 * np.abs(x_scaled[i])**exp
        
        return f1 + f2 + f3 + f4 + f5