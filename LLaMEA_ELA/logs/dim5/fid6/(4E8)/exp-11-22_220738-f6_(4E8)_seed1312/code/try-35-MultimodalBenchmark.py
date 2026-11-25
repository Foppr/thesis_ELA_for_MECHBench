import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Quadratic term for central attraction
        f1 = np.sum(x_norm**2)
        
        # High-frequency sinusoidal terms with chaotic modulation
        f2 = np.sum(np.sin(20 * np.pi * x_norm * (1 + 0.5 * np.sin(5 * x_norm)))**2)
        
        # Polynomial terms with different degrees and asymmetric coefficients
        f3 = np.sum(x_norm**4 + 0.5 * x_norm**6 + 0.2 * x_norm**8)
        
        # Exponential decay with cosine modulation and cross-dimensional coupling
        f4 = np.sum(np.exp(-x_norm**2) * np.cos(6 * np.pi * x_norm) * np.prod(x_norm[:, np.newaxis] - x_norm[np.newaxis, :], axis=1))
        
        # Additional sinusoidal term with varying phase and chaotic frequency
        f5 = np.sum(np.sin(10 * np.pi * x_norm * (1 + 0.3 * np.cos(7 * x_norm))) * np.cos(5 * np.pi * x_norm))
        
        # Cross-dimensional interaction terms for increased complexity
        f6 = np.sum(np.sin(x_norm[:-1] - x_norm[1:])**2)
        
        # Combine all terms with carefully chosen weights and chaotic scaling
        return 0.3 * f1 + 0.5 * f2 + 0.1 * f3 + 0.05 * f4 + 0.03 * f5 + 0.02 * f6 + 5 * np.sum(np.sin(x_norm)) + 3 * np.sum(np.cos(x_norm))