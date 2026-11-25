import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_norm**2)
        
        # Chaotic harmonic potential with exponential decay
        f2 = np.sum(np.exp(-np.abs(x_norm)) * np.sin(10 * np.pi * x_norm)**2)
        
        # Asymmetric cubic coupling with varying coefficients
        f3 = np.sum((x_norm[:-1]**3 - 0.5 * x_norm[1:]**3)**2)
        
        # Multi-scale frequency modulation with exponential decay
        f4 = np.sum(np.sin(2**np.arange(self.dim) * x_norm)**2 * np.exp(-0.1 * np.abs(x_norm)))
        
        # Cross-dimensional exponential coupling with varying strengths
        f5 = np.sum(np.exp(-0.5 * (x_norm[:-1] - x_norm[1:])**2) * (x_norm[:-1]**4 + x_norm[1:]**4))
        
        # Quintic polynomial with asymmetric phase shifts
        f6 = np.sum((x_norm[:-1]**5 - x_norm[1:]**5)**2 * np.cos(0.5 * x_norm[:-1]))
        
        # Gradient-based chaotic term with sinusoidal modulation
        f7 = np.sum(np.sin(x_norm[:-1] * x_norm[1:]) * np.exp(-0.3 * (x_norm[:-1]**2 + x_norm[1:]**2)))
        
        # High-frequency noise component with varying amplitude
        f8 = np.sum(np.sin(20 * x_norm) * np.cos(15 * x_norm) * np.exp(-0.2 * np.abs(x_norm)))
        
        # Combined weighted sum with chaotic scaling factors
        return 0.4 * f1 + 1.2 * f2 + 0.6 * f3 + 0.8 * f4 + 1.0 * f5 + 0.5 * f6 + 0.7 * f7 + 0.9 * f8