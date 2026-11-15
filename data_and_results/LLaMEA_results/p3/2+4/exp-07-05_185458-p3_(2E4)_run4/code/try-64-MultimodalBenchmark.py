import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Quadratic base term for conditioning
        f1 = np.sum(x_norm**2)
        
        # Enhanced chaotic sine waves with varying frequencies and amplitudes
        f2 = np.sum(np.sin(25 * np.pi * x_norm + np.sin(10 * np.pi * x_norm)) ** 2)
        
        # Exponentially increasing frequency terms for complexity with modified exponents
        f3 = np.sum(np.sin(2**(np.arange(1, self.dim + 1) * 1.7) * np.pi * x_norm) ** 2)
        
        # Mixed polynomial terms with increased nonlinearity and varied curvature
        f4 = np.sum(x_norm**6 + 0.5 * x_norm**8 + 0.2 * x_norm**10)
        
        # Cross-terms with enhanced trigonometric coupling to increase dimensionality interaction
        f5 = np.sum(np.cos(x_norm[:-1] * x_norm[1:] * np.cos(x_norm[:-1] + x_norm[1:])) ** 2)
        
        # Additional chaotic interference patterns with modified weights and structure
        f6 = np.sum(np.sin(7 * np.pi * x_norm * np.sin(5 * np.pi * x_norm)) ** 2)
        
        # New term: enhanced cross-dimensional coupling with higher-order interactions and modified exponents
        f7 = np.sum(np.cos(np.pi * x_norm[:-1] * x_norm[1:] * (x_norm[:-1] + x_norm[1:])) ** 5)
        
        # Additional term: introduces asymmetric polynomial coupling to break symmetry and increase difficulty
        f8 = np.sum(np.abs(x_norm)**4.0 + 0.25 * np.abs(x_norm)**6.0)
        
        # Slight modification: adjusted weights on chaotic interference and polynomial exponents for better balance
        return f1 + 0.9 * f2 + 0.55 * f3 + 0.15 * f4 + 0.45 * f5 + 0.25 * f6 + 0.3 * f7 + 0.2 * f8