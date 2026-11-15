import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Base polynomial terms with varying exponents
        f1 = np.sum(x_norm**2)
        f2 = 0.5 * np.sum(x_norm**3)
        f3 = 0.3 * np.sum(x_norm**4)
        f4 = 0.2 * np.sum(x_norm**5)
        
        # Sinusoidal components with non-uniform frequencies
        freqs = np.arange(1, self.dim + 1) * np.pi
        f5 = np.sum(np.sin(freqs * x_norm))
        f6 = np.sum(np.cos(freqs * x_norm))
        
        # Chaotic interaction using sine and cosine combinations
        f7 = np.sum(np.sin(x_norm * np.sin(x_norm)))
        f8 = np.sum(np.cos(x_norm * np.cos(x_norm)))
        
        # Exponential decay with varying rates
        rates = np.arange(1, self.dim + 1) * 0.2
        f9 = np.sum(np.exp(-rates * np.abs(x_norm)))
        
        # Cross-dimensional interactions with non-linear coupling
        f10 = 0.1 * np.sum(np.sin(x_norm[:-1] * x_norm[1:]))
        f11 = 0.1 * np.sum(np.cos(x_norm[:-1] * x_norm[1:]))
        
        # High-frequency oscillation with amplitude modulation
        f12 = np.sum(np.sin(20 * x_norm) * np.exp(-0.5 * x_norm**2))
        
        # Power-law interaction with varying exponents
        f13 = 0.05 * np.sum(np.abs(x_norm)**(3.5 + np.sin(np.arange(self.dim)) * 2))
        
        # Additional chaotic sine-cosine interaction
        f14 = 0.2 * np.sum(np.sin(15 * x_norm) * np.cos(12 * x_norm))
        
        # Modified exponential term with logarithmic scaling
        f15 = 0.15 * np.sum(np.exp(-np.abs(x_norm) * np.log(1 + np.abs(x_norm))))
        
        # Combined polynomial and trigonometric term
        f16 = 0.1 * np.sum((x_norm**2 + np.sin(x_norm))**2)
        
        # Fractional power term for added complexity
        f17 = 0.08 * np.sum(np.abs(x_norm)**1.7)
        
        # Non-uniform frequency sine term
        f18 = 0.25 * np.sum(np.sin(25 * x_norm * (1 + 0.1 * np.sin(x_norm))))
        
        # Gaussian-like penalty with adaptive variance
        f19 = 0.3 * np.sum(np.exp(-0.5 * (x_norm / (1 + np.abs(x_norm)))**2))
        
        # Mixed high-order and low-order interactions
        f20 = 0.1 * np.sum(x_norm**6 * np.sin(x_norm))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13 + f14 + f15 + f16 + f17 + f18 + f19 + f20