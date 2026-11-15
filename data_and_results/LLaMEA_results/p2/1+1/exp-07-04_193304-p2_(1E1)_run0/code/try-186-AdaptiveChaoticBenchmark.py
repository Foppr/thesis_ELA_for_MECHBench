import numpy as np

class AdaptiveChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute frequency factors for stability
        self.freqs = np.arange(1, dim + 1) * np.pi * 0.8
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Polynomial terms with adaptive exponents
        exponents = 2 + 0.5 * np.sin(np.arange(self.dim) * 0.7)
        poly_term = np.sum(np.abs(x_norm)**exponents)
        
        # Trigonometric components with varying frequencies
        trig_term = np.sum(np.sin(self.freqs * x_norm) * np.cos(self.freqs * x_norm))
        
        # Radial basis function with localized minima
        centers = np.linspace(-1, 1, min(5, self.dim))
        if self.dim <= 5:
            rbfs = np.sum(np.exp(-5 * (x_norm - centers)**2))
        else:
            # For higher dimensions, use a subset of centers
            rbfs = np.sum(np.exp(-5 * (x_norm - centers[:self.dim//2])**2))
        
        # Chaotic sine-cosine coupling
        chaotic_term = np.sum(np.sin(x_norm * np.cos(x_norm * 1.5)) * np.exp(-0.3 * np.abs(x_norm)))
        
        # Adaptive conditioning based on dimension
        cond_factor = 1.0 + 0.2 * np.log(self.dim + 1)
        
        # Multi-modal structure with sharp valleys
        sharp_term = np.sum(np.sin(10 * x_norm) * np.exp(-0.1 * x_norm**2))
        
        # Cross-dimensional coupling with exponential decay
        coupling = 0.0
        for i in range(self.dim - 1):
            coupling += np.exp(-0.5 * (x_norm[i]**2 + x_norm[i+1]**2)) * np.sin(x_norm[i] * x_norm[i+1])
        
        # Combined fitness
        return cond_factor * (poly_term + 0.5 * trig_term + 0.3 * rbfs + 0.2 * chaotic_term + 0.1 * sharp_term + 0.05 * coupling)