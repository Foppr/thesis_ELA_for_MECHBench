import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for efficiency
        self.consts = {
            'pi': np.pi,
            'e': np.e,
            'sqrt2': np.sqrt(2),
            'inv_sqrt2': 1.0 / np.sqrt(2)
        }
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Polynomial terms with varying degrees
        f1 = np.sum(x_norm**2)  # Quadratic
        f2 = 0.3 * np.sum(x_norm**4)  # Quartic
        f3 = 0.15 * np.sum(x_norm**6)  # Sextic
        
        # Trigonometric components with varying frequencies
        freqs = np.arange(1, self.dim + 1) * 2.0
        f4 = np.sum(np.sin(freqs * x_norm) * np.cos(freqs * x_norm))
        f5 = np.sum(np.sin(freqs * x_norm)**2 + np.cos(freqs * x_norm)**2)
        
        # Radial basis function components with adaptive widths
        widths = 0.5 + 0.5 * np.sin(np.arange(self.dim) * 0.7)
        f6 = np.sum(np.exp(-0.5 * (x_norm**2) / (widths**2)))
        
        # Cross-dimensional coupling with non-linear interaction
        f7 = 0.2 * np.sum(np.sin(x_norm[:-1] * x_norm[1:]) * np.cos(x_norm[:-1] + x_norm[1:]))
        
        # Chaotic sine-cosine interaction
        f8 = 0.15 * np.sum(np.sin(x_norm * np.cos(x_norm * 1.5)) * np.cos(x_norm * np.sin(x_norm * 1.2)))
        
        # Multi-modal structure with localized minima
        f9 = 0.25 * np.sum(np.sin(10 * x_norm) * np.exp(-0.1 * x_norm**2))
        
        # Adaptive scaling based on dimensionality
        dim_factor = 1.0 + 0.1 * np.log(self.dim + 1)
        f10 = dim_factor * np.sum(np.abs(x_norm)**(1.5 + 0.2 * np.sin(np.arange(self.dim) * 0.5)))
        
        # Sharp localized minima
        f11 = 0.3 * np.sum(np.exp(-10 * (x_norm - 0.3)**2) + np.exp(-10 * (x_norm + 0.3)**2))
        
        # Fractional power with oscillating exponent
        exponents = 1.8 + 0.4 * np.sin(np.arange(self.dim) * 0.8)
        f12 = 0.1 * np.sum(np.abs(x_norm)**exponents)
        
        # Hybrid polynomial-trigonometric term
        f13 = 0.2 * np.sum((x_norm**2 + np.sin(x_norm))**1.5)
        
        # Asymmetric penalty
        f14 = 0.1 * np.sum(np.exp(2 * np.abs(x_norm)) - 1)
        
        # Multi-scale oscillation
        f15 = 0.2 * np.sum(np.sin(20 * x_norm * np.log(1.1 + np.abs(x_norm))))
        
        # Combined result
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13 + f14 + f15