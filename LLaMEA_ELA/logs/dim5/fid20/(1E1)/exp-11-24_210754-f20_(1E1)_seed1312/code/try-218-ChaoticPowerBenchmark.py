import numpy as np

class ChaoticPowerBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base conditioning term with exponential scaling
        f1 = np.sum(np.exp(0.5 * x**2) - 1.0) / self.dim
        
        # Trigonometric coupling with varying frequencies and amplitudes
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            freq = 20.0 * (1.0 + 0.5 * np.sin(i * 0.7))
            amp = 1.0 + 0.3 * np.cos(i * 0.9)
            f2 += amp * np.sin(freq * xi) * np.cos(freq * xi**1.5)
        
        # Power-law interaction with asymmetric scaling
        f3 = 0.0
        for i in range(self.dim):
            xi = x[i]
            power = 2.5 + 0.8 * np.sin(i * 0.6)
            f3 += np.abs(xi)**power
        
        # Exponential decay with sinusoidal modulation
        f4 = 0.1 * np.sum(np.exp(-0.5 * np.abs(x)) * np.sin(15.0 * x))
        
        # Multi-scale fractal-like structure using recursive power terms
        f5 = 0.2 * np.sum(np.sin(30.0 * np.log(np.abs(x) + 1.0)) * np.cos(20.0 * np.exp(-x**2)))
        
        # Asymmetric cross-terms with variable coupling strength
        f6 = 0.05 * np.sum((x[:-1]**2.3 + 0.7 * x[1:]**1.9) * np.sin(0.5 * (x[:-1] + x[1:])))

        # Combined chaotic signal with varying phase shifts
        f7 = 0.15 * np.sum(np.sin(25.0 * x + np.sin(x)) * np.cos(18.0 * x + np.cos(x)))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7