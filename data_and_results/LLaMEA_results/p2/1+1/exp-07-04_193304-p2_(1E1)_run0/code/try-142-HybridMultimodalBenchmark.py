import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for stability
        self.consts = np.arange(1, dim + 1) * np.pi / 4.0
    
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Polynomial terms with varying degrees
        f1 = np.sum(x_norm**2)
        f2 = 0.7 * np.sum(x_norm**3)
        f3 = 0.3 * np.sum(x_norm**4)
        
        # Trigonometric components with dynamic frequencies
        f4 = np.sum(np.sin(self.consts * x_norm) * np.cos(self.consts * x_norm))
        f5 = np.sum(np.sin(x_norm * np.sin(x_norm)) * np.cos(x_norm * np.cos(x_norm)))
        
        # Radial basis function components with adaptive widths
        widths = 0.5 + 0.5 * np.sin(np.arange(self.dim) * 0.7)
        f6 = np.sum(np.exp(-0.5 * (x_norm**2) / (widths**2 + 1e-8)))
        
        # Cross-dimensional coupling with non-linear interaction
        f7 = 0.5 * np.sum(np.sin(x_norm[:-1] * x_norm[1:]) * np.cos(x_norm[:-1] + x_norm[1:]))
        
        # Adaptive scaling based on dimensionality
        scale_factor = 1.0 + 0.3 * np.sin(np.sum(x_norm**2))
        f8 = scale_factor * np.sum(np.abs(x_norm)**1.5)
        
        # Multi-modal sine with varying amplitudes
        f9 = 0.8 * np.sum(np.sin(10 * x_norm + np.sin(5 * x_norm)) * np.exp(-0.3 * x_norm**2))
        
        # Fractional dimensionality effect
        f10 = 0.4 * np.sum(np.abs(x_norm)**(1.3 + 0.7 * np.sin(np.arange(self.dim) * 0.5)))
        
        # Dynamic exponential decay with parameter modulation
        f11 = np.sum(np.exp(-np.abs(x_norm) * (1.2 + 0.8 * np.sin(x_norm))))
        
        # Complex coupling with hyperbolic functions
        f12 = 0.6 * np.sum(np.tanh(x_norm * np.sin(x_norm)) * np.cos(x_norm * np.cos(x_norm)))
        
        # Adaptive penalty with multi-scale behavior
        f13 = 0.5 * np.sum(np.exp(-0.2 * (x_norm**2 + 0.1 * np.abs(x_norm))))
        
        # High-frequency oscillation with amplitude modulation
        f14 = 0.3 * np.sum(np.sin(20 * x_norm) * np.cos(15 * x_norm) * np.exp(-0.1 * x_norm**2))
        
        # Combined chaotic and polynomial behavior
        f15 = 0.4 * np.sum((x_norm**2 + np.sin(x_norm))**1.5)
        
        # Dynamic coupling with logarithmic scaling
        f16 = 0.5 * np.sum(np.log(1.1 + np.abs(x_norm)) * np.sin(x_norm))
        
        # Multi-scale radial interaction
        f17 = 0.3 * np.sum(np.exp(-0.3 * (x_norm**2 + 0.2 * np.abs(x_norm))))
        
        # Non-uniform frequency sine-cosine interaction
        f18 = 0.6 * np.sum(np.sin(15 * x_norm) * np.cos(12 * x_norm) * np.exp(-0.2 * x_norm**2))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13 + f14 + f15 + f16 + f17 + f18