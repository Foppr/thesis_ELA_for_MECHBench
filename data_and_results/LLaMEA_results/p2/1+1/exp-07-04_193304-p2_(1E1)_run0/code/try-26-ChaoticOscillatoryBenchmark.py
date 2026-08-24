import numpy as np

class ChaoticOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_norm**2)
        
        # High-frequency sine oscillation with exponential decay envelope
        f2 = 2.0 * np.sum(np.sin(50 * np.pi * x_norm) * np.exp(-0.5 * x_norm**2))
        
        # Asymmetric penalty based on sign and magnitude
        f3 = 1.5 * np.sum(np.where(x_norm > 0, x_norm**3, -0.5 * x_norm**3))
        
        # Multi-scale chaotic modulation using nested trigonometric functions
        f4 = 0.8 * np.sum(np.sin(10 * np.pi * np.cos(20 * np.pi * x_norm)))
        
        # Exponentially weighted cubic terms with alternating signs
        f5 = 0.6 * np.sum((-1)**np.arange(self.dim) * np.abs(x_norm)**3 * np.exp(-0.1 * np.abs(x_norm)))
        
        # Cross-dimensional interaction with varying coupling strengths
        f6 = 0.4 * np.sum((x_norm[:-1] * x_norm[1:] * np.sin(15 * np.pi * x_norm[:-1]))**2)
        
        # Logarithmic barrier near boundaries to penalize out-of-range values
        f7 = 0.3 * np.sum(np.log(1 + 10 * x_norm**2))
        
        # Gaussian mixture with different variances and means
        f8 = 0.5 * np.sum(np.exp(-0.5 * (x_norm - 0.3)**2) + 0.5 * np.exp(-0.5 * (x_norm + 0.3)**2))
        
        # Fractional power and sine combination for non-integer curvature
        f9 = 0.2 * np.sum(np.abs(x_norm)**1.5 * np.sin(30 * x_norm))
        
        # Multi-modal component with varying frequencies and amplitudes
        f10 = 0.7 * np.sum(np.cos(35 * np.pi * x_norm) * np.exp(-0.3 * x_norm**2))
        
        # Asymmetric exponential penalty
        f11 = 0.9 * np.sum(np.exp(2 * np.abs(x_norm)) - 1)
        
        # High-order polynomial with alternating coefficients
        f12 = 0.1 * np.sum(x_norm**7 * np.cos(25 * x_norm))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12