import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Quadratic base term for conditioning
        f1 = np.sum(x_norm**2)
        
        # Enhanced chaotic sine waves with modified frequencies and amplitudes
        f2 = np.sum(np.sin(20 * np.pi * x_norm + np.sin(9 * np.pi * x_norm)) ** 2)
        
        # Exponentially increasing frequency terms with modified exponents for complexity
        f3 = np.sum(np.sin(2**(np.arange(1, self.dim + 1) * 1.2) * np.pi * x_norm) ** 2)
        
        # Mixed polynomial terms with altered exponents for non-convexity and varied curvature
        f4 = np.sum(x_norm**4 + 0.4 * x_norm**6 + 0.15 * x_norm**8)
        
        # Cross-terms with enhanced trigonometric coupling to increase dimensionality interaction
        f5 = np.sum(np.cos(x_norm[:-1] * x_norm[1:] * np.cos(x_norm[:-1] + x_norm[1:])) ** 2)
        
        # Additional chaotic interference patterns with modified weights and structure
        f6 = np.sum(np.sin(7 * np.pi * x_norm * np.sin(4 * np.pi * x_norm)) ** 2)
        
        # New term: enhanced cross-dimensional coupling with higher-order interactions and modified exponents
        f7 = np.sum(np.cos(np.pi * x_norm[:-1] * x_norm[1:] * (x_norm[:-1] + x_norm[1:])) ** 4)
        
        # Further adjusted weights to balance contributions and improve discrimination
        return f1 + 0.85 * f2 + 0.5 * f3 + 0.12 * f4 + 0.4 * f5 + 0.22 * f6 + 0.25 * f7