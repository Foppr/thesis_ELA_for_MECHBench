import numpy as np

class AdaptiveMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute frequency factors for stability
        self.freq_factors = np.arange(1, dim + 1) * 0.8
        
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Polynomial terms with varying degrees
        poly_terms = [np.sum(x_norm**(2 + i)) * (0.5 + i * 0.1) for i in range(5)]
        f1 = sum(poly_terms)
        
        # Trigonometric components with dynamic frequencies
        trig_terms = [
            np.sum(np.sin(self.freq_factors * x_norm * (1 + 0.2 * np.sin(x_norm * 0.5)))),
            np.sum(np.cos(self.freq_factors * x_norm * (1 + 0.15 * np.cos(x_norm * 0.7))))
        ]
        f2 = sum(trig_terms)
        
        # Radial basis function components with adaptive widths
        rb_widths = 0.5 + 0.3 * np.sin(np.arange(self.dim) * 0.5)
        f3 = np.sum(np.exp(-np.sum((x_norm.reshape(-1, 1) - x_norm.reshape(1, -1))**2, axis=1) / (2 * rb_widths**2)))
        
        # Cross-dimensional coupling with non-linear interaction
        f4 = 0.3 * np.sum(np.sin(x_norm[:-1] * x_norm[1:] * (1 + 0.1 * np.sin(x_norm[:-1] + x_norm[1:]))))
        
        # Adaptive scaling based on dimension
        scale_factor = 1.0 + 0.2 * np.sin(self.dim * 0.3)
        f5 = scale_factor * np.sum(np.abs(x_norm)**(1.5 + 0.3 * np.sin(np.arange(self.dim) * 0.4)))
        
        # Multi-scale oscillation with amplitude modulation
        f6 = np.sum(np.sin(20 * x_norm * np.exp(-0.1 * np.abs(x_norm))) * np.cos(15 * x_norm * np.exp(-0.05 * np.abs(x_norm))))
        
        # Chaotic sine-cosine interaction
        f7 = 0.25 * np.sum(np.sin(x_norm * np.cos(x_norm * 1.2)) * np.cos(x_norm * np.sin(x_norm * 0.8)))
        
        # Fractional dimensionality effect
        f8 = 0.15 * np.sum(np.abs(x_norm)**(1.3 + 0.4 * np.sin(np.arange(self.dim) * 0.6)))
        
        # Dynamic penalty with exponential decay
        f9 = 0.2 * np.sum(np.exp(-0.5 * (x_norm**2 + 0.1 * np.abs(x_norm))))
        
        # Asymmetric multimodal components
        f10 = 0.18 * np.sum(np.sin(12 * x_norm) * np.exp(-0.3 * x_norm**2) + np.cos(10 * x_norm) * np.exp(-0.2 * x_norm**2))
        
        # Combined high-order polynomial and trigonometric
        f11 = 0.12 * np.sum((x_norm**3 + np.sin(x_norm))**2)
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11