import numpy as np

class AdaptiveMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Polynomial base with varying degrees
        f1 = np.sum(x_norm**2)
        f2 = 0.7 * np.sum(x_norm**3)
        f3 = 0.4 * np.sum(x_norm**4)
        
        # Trigonometric components with adaptive frequencies
        freqs = np.arange(1, self.dim + 1) * (1.5 + 0.5 * np.sin(np.arange(self.dim) * 0.3))
        f4 = np.sum(np.sin(freqs * x_norm) * np.cos(freqs * x_norm))
        f5 = np.sum(np.sin(freqs * x_norm**2) * np.cos(freqs * x_norm**2))
        
        # Radial basis function component with adaptive centers
        centers = np.linspace(-1, 1, self.dim)
        f6 = np.sum(np.exp(-5 * (x_norm - centers)**2))
        
        # Asymmetric penalty terms
        f7 = np.sum(np.where(x_norm > 0, 0.8 * x_norm**2, 1.2 * x_norm**2))
        f8 = np.sum(np.where(x_norm < 0, 0.6 * np.abs(x_norm)**1.5, 0.4 * np.abs(x_norm)**1.5))
        
        # Cross-dimensional coupling with dynamic weights
        weights = 1.0 + 0.3 * np.sin(np.arange(self.dim-1) * 0.7)
        f9 = np.sum(weights * (x_norm[:-1]**2 + x_norm[1:]**2) * np.sin(x_norm[:-1] * x_norm[1:]))
        
        # Multi-scale oscillation with amplitude modulation
        f10 = np.sum(np.sin(10 * x_norm) * np.exp(-0.3 * np.abs(x_norm)) * (1 + 0.2 * np.sin(5 * x_norm)))
        
        # Adaptive dimensionality effect
        dim_factor = 1.0 + 0.2 * np.sin(self.dim * 0.5)
        f11 = dim_factor * np.sum(np.sin(x_norm * 3.0) * np.cos(x_norm * 2.0))
        
        # Fractional power and logarithmic interaction
        f12 = 0.5 * np.sum(np.abs(x_norm)**1.8 * np.log(1.1 + np.abs(x_norm)))
        
        # Chaotic sine-cosine interaction
        f13 = 0.3 * np.sum(np.sin(x_norm * np.cos(x_norm * 1.3)) * np.cos(x_norm * np.sin(x_norm * 1.7)))
        
        # Adaptive penalty with exponential decay
        f14 = 0.4 * np.sum(np.exp(-0.5 * np.abs(x_norm)) * (1 + 0.3 * np.sin(8 * x_norm)))
        
        # Combined high-order polynomial and trigonometric term
        f15 = 0.6 * np.sum((x_norm**3 + np.sin(x_norm))**2)
        
        # Multi-modal component with varying amplitudes
        f16 = 0.8 * np.sum(np.sin(7 * x_norm + 0.5 * np.sin(3 * x_norm)) * np.exp(-0.2 * x_norm**2))
        
        # Dynamic scaling based on dimensionality
        scale_factor = 1.0 + 0.1 * np.log(self.dim + 1)
        f17 = scale_factor * np.sum(np.cos(x_norm * 4.0) * np.exp(-0.1 * np.abs(x_norm)))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13 + f14 + f15 + f16 + f17