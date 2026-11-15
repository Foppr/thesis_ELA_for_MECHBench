import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Quadratic base term for conditioning
        f1 = np.sum(x_norm**2)
        
        # Enhanced chaotic sine waves with higher frequency modulation and added phase shifts
        f2 = np.sum(np.sin(25 * np.pi * x_norm + np.sin(10 * np.pi * x_norm)) ** 2)
        
        # Exponentially increasing frequency terms with modified phase shifts
        f3 = np.sum(np.sin(2**(np.arange(1, self.dim + 1) + 0.5) * np.pi * x_norm + np.sin(4 * np.pi * x_norm)) ** 2)
        
        # Mixed polynomial terms with higher exponents and asymmetric coefficients
        f4 = np.sum(0.8 * x_norm**5 + 0.3 * x_norm**7 + 0.1 * x_norm**9)
        
        # Stronger cross-terms with trigonometric coupling and additional interaction
        f5 = np.sum(np.cos(x_norm[:-1] * x_norm[1:] * np.cos(x_norm[:-1] + x_norm[1:] + x_norm[:-1]**2)) ** 2)
        
        # Additional chaotic interference patterns with modified weights and nonlinear coupling
        f6 = np.sum(np.sin(8 * np.pi * x_norm * np.sin(5 * np.pi * x_norm) * np.cos(3 * np.pi * x_norm)) ** 2)
        
        # New term: higher-order cross-dimensional coupling with chaotic modulation
        f7 = np.sum(np.cos(np.pi * x_norm[:-1] * x_norm[1:] * (x_norm[:-1] + x_norm[1:] + x_norm[:-1]**3)) ** 4)
        
        # Additional term: asymmetric polynomial coupling with exponential decay and modified exponents
        f8 = np.sum(np.exp(-x_norm**2) * (x_norm**4 + 0.6 * x_norm**6) ** 2)
        
        # Slight modification: increased weight on chaotic interference and adjusted polynomial exponents
        return f1 + 0.98 * f2 + 0.65 * f3 + 0.18 * f4 + 0.48 * f5 + 0.30 * f6 + 0.35 * f7 + 0.20 * f8