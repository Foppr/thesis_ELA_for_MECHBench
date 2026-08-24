import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Quadratic base term for conditioning
        f1 = np.sum(x_norm**2)
        
        # Enhanced chaotic sine waves with variable frequencies and amplitudes
        f2 = np.sum(np.sin(30 * np.pi * x_norm + np.sin(15 * np.pi * x_norm)) ** 2)
        
        # Exponentially increasing frequency terms for complexity
        f3 = np.sum(np.sin(2**(np.arange(1, self.dim + 1) * 1.3) * np.pi * x_norm) ** 2)
        
        # Mixed polynomial terms for non-convexity and varied curvature
        f4 = np.sum(1.5 * x_norm**4 + 0.4 * x_norm**6 + 0.15 * x_norm**8)
        
        # Cross-terms with trigonometric coupling to increase dimensionality interaction
        f5 = np.sum(np.sin(x_norm[:-1] * x_norm[1:] * np.sin(x_norm[:-1] + x_norm[1:] * 0.6)) ** 2)
        
        # Additional chaotic interference patterns with higher-order terms
        f6 = np.sum(np.sin(7 * np.pi * x_norm * np.sin(6 * np.pi * x_norm)) ** 2)
        
        # Higher-order trigonometric coupling for increased complexity
        f7 = np.sum(np.sin(12 * np.pi * x_norm * np.sin(6 * np.pi * x_norm) * np.sin(3 * np.pi * x_norm)) ** 2)
        
        # Adaptive difficulty based on dimensionality with enhanced nonlinearity
        f8 = np.sum(np.sin(np.pi * x_norm * np.sin(5 * np.pi * x_norm) * np.sin(6 * np.pi * x_norm)) ** 2)
        
        # Additional cross-dimensional interaction terms
        f9 = np.sum(np.cos(x_norm[:-1] * x_norm[1:] * np.cos(x_norm[:-1] + x_norm[1:] * 0.8)) ** 2)
        
        # Combine all terms with varying weights
        return f1 + 0.85 * f2 + 0.55 * f3 + 0.18 * f4 + 0.35 * f5 + 0.28 * f6 + 0.32 * f7 + 0.22 * f8 + 0.18 * f9