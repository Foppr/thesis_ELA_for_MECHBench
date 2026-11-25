import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Quadratic term with conditioning
        f1 = np.sum(x_norm**2)
        
        # High-frequency chaotic sinusoidal terms with varying amplitudes
        f2 = np.sum(np.sin(33 * np.pi * x_norm)**9 + 0.7 * np.sin(44 * np.pi * x_norm**2)**7)
        
        # Exponential barrier terms with asymmetric shape
        f3 = np.sum(np.exp(-x_norm**2) - 1.0 + 0.3 * np.exp(-(x_norm - 0.3)**2))
        
        # Mixed polynomial and trigonometric terms for additional complexity
        f4 = np.sum(x_norm**9 * np.cos(8 * np.pi * x_norm) + 0.5 * x_norm**4 * np.sin(15 * np.pi * x_norm))
        
        # Global repulsion term with non-uniform scaling
        f5 = 0.6 * np.sum(np.abs(x_norm)**0.3)
        
        # High-frequency cross-dimensional interaction terms
        f6 = 0.2 * np.sum(np.sin(39 * (x_norm[:-1] + x_norm[1:]))**6)
        
        # Nested sinusoidal shifts creating multiple layers of local minima
        f7 = 0.18 * np.sum(np.sin(25 * np.pi * (x_norm + 0.15))**4 + np.sin(31 * np.pi * (x_norm - 0.2))**4)
        
        # Additional chaotic term with non-linear transformation
        f8 = 0.1 * np.sum(np.sin(52 * x_norm**3) * np.cos(13 * x_norm) * np.exp(-x_norm**2))
        
        return f1 + 0.5 * f2 + 0.25 * f3 + 0.15 * f4 + 0.1 * f5 + 0.08 * f6 + 0.06 * f7 + 0.04 * f8