import numpy as np

class AdaptiveMultiScaleBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Quadratic base with adaptive conditioning
        f1 = 0.5 * np.sum(x_norm**2)
        
        # Trigonometric components with multi-scale frequencies
        freqs = np.logspace(0, 2, self.dim) * 2 * np.pi
        f2 = np.sum(np.sin(freqs * x_norm) * np.cos(freqs * x_norm))
        
        # Radial basis function component with adaptive width
        centers = np.linspace(-1, 1, self.dim)
        widths = 0.1 + 0.4 * np.sin(np.arange(self.dim) * 0.7)
        rbf = np.sum(np.exp(-0.5 * ((x_norm[:, np.newaxis] - centers) / widths)**2))
        
        # Multi-scale periodicity with amplitude modulation
        scales = np.logspace(0, 3, self.dim)
        f3 = np.sum(np.sin(scales * x_norm) * np.exp(-0.1 * np.abs(x_norm)))
        
        # Adaptive dimensionality coupling
        coupling_strength = 0.3 + 0.2 * np.sin(np.arange(self.dim) * 0.5)
        f4 = np.sum(coupling_strength * x_norm[:-1] * x_norm[1:])
        
        # Hybrid polynomial-trigonometric terms
        f5 = 0.2 * np.sum((x_norm**3 + np.sin(x_norm))**2)
        
        # Asymmetric penalty with exponential decay
        f6 = np.sum(np.exp(0.5 * x_norm**2) * (x_norm > 0) + np.exp(-0.5 * x_norm**2) * (x_norm <= 0))
        
        # Fractional dimensionality effect with periodic modulation
        mod_freq = 0.5 + 0.3 * np.sin(np.arange(self.dim) * 0.8)
        f7 = np.sum(np.abs(x_norm)**(1.5 + mod_freq))
        
        # Cross-dimensional interaction with logarithmic scaling
        f8 = 0.15 * np.sum(np.log(1.1 + np.abs(x_norm[:-1] * x_norm[1:])))
        
        # Multi-modal sine with dynamic amplitude
        f9 = np.sum(np.sin(10 * x_norm + 0.5 * np.sin(5 * x_norm)) * np.exp(-0.3 * x_norm**2))
        
        # Adaptive chaotic coupling with cosine modulation
        f10 = 0.25 * np.sum(np.cos(x_norm * np.sin(x_norm * 1.5)) * np.exp(-0.2 * np.abs(x_norm)))
        
        # Combined penalty and regularization
        f11 = 0.1 * np.sum(np.abs(x_norm)**3 + np.abs(x_norm)**0.5)
        
        # Multi-scale Gaussian-like penalty
        f12 = 0.3 * np.sum(np.exp(-0.5 * (x_norm / (0.5 + np.abs(x_norm)))**2))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12