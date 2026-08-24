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
        f2 = np.sum(np.sin(20 * np.pi * x_norm + np.sin(9 * np.pi * x_norm)) ** 2)
        
        # Exponentially increasing frequency terms for complexity with modified exponents
        f3 = np.sum(np.sin(2**(np.arange(1, self.dim + 1) * 1.6) * np.pi * x_norm) ** 2)
        
        # Mixed polynomial terms with increased nonlinearity and varied curvature
        f4 = np.sum(x_norm**5 + 0.4 * x_norm**7 + 0.15 * x_norm**9)
        
        # Cross-terms with enhanced trigonometric coupling to increase dimensionality interaction
        f5 = np.sum(np.cos(x_norm[:-1] * x_norm[1:] * np.cos(x_norm[:-1] + x_norm[1:])) ** 2)
        
        # Additional chaotic interference patterns with modified weights and structure
        f6 = np.sum(np.sin(6 * np.pi * x_norm * np.sin(4 * np.pi * x_norm)) ** 2)
        
        # New term: enhanced cross-dimensional coupling with higher-order interactions and modified exponents
        f7 = np.sum(np.cos(np.pi * x_norm[:-1] * x_norm[1:] * (x_norm[:-1] + x_norm[1:])) ** 4)
        
        # Additional term: introduces asymmetric polynomial coupling to break symmetry and increase difficulty
        f8 = np.sum(np.abs(x_norm)**3.5 + 0.2 * np.abs(x_norm)**5.5)
        
        # Slight modification: adjusted weights on chaotic interference and polynomial exponents for better balance
        return f1 + 0.85 * f2 + 0.5 * f3 + 0.12 * f4 + 0.4 * f5 + 0.2 * f6 + 0.25 * f7 + 0.15 * f8