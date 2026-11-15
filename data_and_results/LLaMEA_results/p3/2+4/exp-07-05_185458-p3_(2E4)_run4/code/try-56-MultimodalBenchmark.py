import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Quadratic base term for conditioning
        f1 = np.sum(x_norm**2)
        
        # Chaotic sine waves with varying frequencies and amplitudes
        f2 = np.sum(np.sin(15 * np.pi * x_norm + np.sin(7 * np.pi * x_norm)) ** 2)
        
        # Exponentially increasing frequency terms for complexity
        f3 = np.sum(np.sin(2**(np.arange(1, self.dim + 1)) * np.pi * x_norm) ** 2)
        
        # Mixed polynomial terms for non-convexity and varied curvature
        f4 = np.sum(x_norm**4 + 0.3 * x_norm**6 + 0.1 * x_norm**8)
        
        # Cross-terms with trigonometric coupling to increase dimensionality interaction
        f5 = np.sum(np.cos(x_norm[:-1] * x_norm[1:] * np.cos(x_norm[:-1] + x_norm[1:])) ** 2)
        
        # Additional chaotic interference patterns with modified weights
        f6 = np.sum(np.sin(5 * np.pi * x_norm * np.sin(3 * np.pi * x_norm)) ** 2)
        
        # New term: enhanced cross-dimensional coupling with higher-order interactions
        f7 = np.sum(np.cos(np.pi * x_norm[:-1] * x_norm[1:] * (x_norm[:-1] + x_norm[1:])) ** 3)
        
        # Slight modification: increased weight on chaotic interference and adjusted polynomial exponents
        return f1 + 0.75 * f2 + 0.45 * f3 + 0.09 * f4 + 0.35 * f5 + 0.18 * f6 + 0.22 * f7