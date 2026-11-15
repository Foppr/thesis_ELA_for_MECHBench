import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Sum of squares term
        f1 = np.sum(x_norm**2)
        
        # Multiple high-frequency sinusoidal terms with varying amplitudes
        f2 = 0.8 * np.sum(np.cos(15 * np.pi * x_norm)) + 0.6 * np.sum(np.sin(20 * np.pi * x_norm))
        
        # High-order polynomial terms for increased curvature
        f3 = 0.1 * np.sum(x_norm**6) + 0.05 * np.sum(x_norm**8)
        
        # Cross-term interactions with non-linear coupling
        f4 = 0.2 * np.sum(x_norm[:-1]**2 * x_norm[1:]**2)
        
        # Quadratic interaction with shifted variables
        f5 = 0.1 * np.sum((x_norm[:-1] - 0.5 * x_norm[1:])**2)
        
        # Fifth power and absolute value terms for added complexity
        f6 = 0.03 * np.sum(np.abs(x_norm)**5) + 0.02 * np.sum(np.abs(x_norm)**7)
        
        # Additional sine and cosine terms with different frequencies
        f7 = 0.3 * np.sum(np.sin(12 * np.pi * x_norm) * np.cos(18 * np.pi * x_norm))
        
        # Exponential interaction term for enhanced conditioning
        f8 = 0.05 * np.sum(np.exp(2 * x_norm**2) - 1)
        
        # Additional quartic and sextic terms for multimodality
        f9 = 0.08 * np.sum(x_norm**4) + 0.04 * np.sum(x_norm**6)
        
        # Combined interaction term with multiple variables
        f10 = 0.15 * np.sum((x_norm[:-2] + x_norm[1:-1] - x_norm[2:])**2)
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10