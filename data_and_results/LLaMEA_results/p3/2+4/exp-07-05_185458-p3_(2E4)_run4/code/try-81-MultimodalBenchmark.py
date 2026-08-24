import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Quadratic base term for conditioning
        f1 = np.sum(x_norm**2)
        
        # Enhanced chaotic sine waves with higher frequency modulation and amplitude scaling
        f2 = np.sum((1.5 * np.sin(25 * np.pi * x_norm + np.sin(12 * np.pi * x_norm))) ** 2)
        
        # Exponentially increasing frequency terms with added phase shifts and modified exponents
        f3 = np.sum(np.sin(2**(np.arange(1, self.dim + 1) + 0.7) * np.pi * x_norm + np.sin(4 * np.pi * x_norm)) ** 2)
        
        # Mixed polynomial terms with higher exponents and additional nonlinear interactions
        f4 = np.sum(x_norm**6 + 0.4 * x_norm**8 + 0.3 * x_norm**10 + 0.15 * x_norm**12)
        
        # Stronger cross-terms with trigonometric coupling and additional interaction patterns
        f5 = np.sum(np.cos(x_norm[:-1] * x_norm[1:] * np.cos(x_norm[:-1] + x_norm[1:] + x_norm[:-1]**2.7)) ** 2)
        
        # Additional chaotic interference patterns with modified weights and nonlinear coupling
        f6 = np.sum(np.sin(8 * np.pi * x_norm * np.sin(4.5 * np.pi * x_norm) * np.cos(2.3 * np.pi * x_norm)) ** 2)
        
        # New term: higher-order cross-dimensional coupling with chaotic modulation and increased complexity
        f7 = np.sum(np.cos(np.pi * x_norm[:-1] * x_norm[1:] * (x_norm[:-1] + x_norm[1:] + x_norm[:-1]**3.5)) ** 4)
        
        # Additional term: asymmetric polynomial coupling with exponential decay and modified exponents
        f8 = np.sum(np.exp(-x_norm**2.5) * (x_norm**3.5 + 0.6 * x_norm**5.5) ** 2)
        
        # New term: increased chaotic modulation with polynomial interaction and cross-coupling
        f9 = np.sum(np.sin(3.2 * np.pi * x_norm * np.sin(5.8 * np.pi * x_norm) * np.cos(1.9 * np.pi * x_norm)) ** 3)
        
        # Slight modification: increased weight on chaotic interference and adjusted polynomial exponents
        return f1 + 1.02 * f2 + 0.68 * f3 + 0.18 * f4 + 0.52 * f5 + 0.32 * f6 + 0.38 * f7 + 0.21 * f8 + 0.25 * f9