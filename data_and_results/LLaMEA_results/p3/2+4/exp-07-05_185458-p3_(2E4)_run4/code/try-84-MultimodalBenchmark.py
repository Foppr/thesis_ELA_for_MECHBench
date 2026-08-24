import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Quadratic base term for conditioning
        f1 = np.sum(x_norm**2)
        
        # Enhanced chaotic sine waves with higher frequency modulation
        f2 = np.sum(np.sin(22 * np.pi * x_norm + np.sin(10 * np.pi * x_norm)) ** 2)
        
        # Exponentially increasing frequency terms with added phase shifts
        f3 = np.sum(np.sin(2**(np.arange(1, self.dim + 1) + 0.5) * np.pi * x_norm + np.sin(3.5 * np.pi * x_norm)) ** 2)
        
        # Mixed polynomial terms with higher exponents for increased non-convexity
        f4 = np.sum(x_norm**5 + 0.35 * x_norm**7 + 0.25 * x_norm**9)
        
        # Stronger cross-terms with trigonometric coupling and additional interaction
        f5 = np.sum(np.cos(x_norm[:-1] * x_norm[1:] * np.cos(x_norm[:-1] + x_norm[1:] + x_norm[:-1]**2.5)) ** 2)
        
        # Additional chaotic interference patterns with modified weights and nonlinear coupling
        f6 = np.sum(np.sin(7.5 * np.pi * x_norm * np.sin(4.2 * np.pi * x_norm) * np.cos(2.1 * np.pi * x_norm)) ** 2)
        
        # New term: higher-order cross-dimensional coupling with chaotic modulation
        f7 = np.sum(np.cos(np.pi * x_norm[:-1] * x_norm[1:] * (x_norm[:-1] + x_norm[1:] + x_norm[:-1]**3.2)) ** 4)
        
        # Additional term: asymmetric polynomial coupling with exponential decay
        f8 = np.sum(np.exp(-x_norm**2.2) * (x_norm**3.1 + 0.55 * x_norm**5.2) ** 2)
        
        # Slight modification: adjusted weights and exponents for better balance
        return f1 + 0.97 * f2 + 0.62 * f3 + 0.16 * f4 + 0.47 * f5 + 0.29 * f6 + 0.34 * f7 + 0.19 * f8