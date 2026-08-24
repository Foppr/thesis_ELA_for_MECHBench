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
        
        # Adaptive weighting based on dimensionality
        adaptive_weights = np.array([0.7, 0.4, 0.08, 0.3, 0.15, 0.2]) * (1 + 0.1 * np.log(self.dim + 1))
        
        # Combine all terms with optimized weights for better fitness
        return f1 + adaptive_weights[0] * f2 + adaptive_weights[1] * f3 + adaptive_weights[2] * f4 + adaptive_weights[3] * f5 + adaptive_weights[4] * f6 + adaptive_weights[5] * f7