import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Quadratic base term
        f1 = np.sum(x_norm**2)
        
        # Chaotic sinusoidal components with varying frequencies and amplitudes
        f2 = np.sum(np.sin(2 * np.pi * x_norm) ** 4) + 0.7 * np.sum(np.sin(5 * np.pi * x_norm) ** 3) + 0.3 * np.sum(np.sin(9 * np.pi * x_norm) ** 2)
        
        # High-frequency chaotic oscillation with exponential modulation
        f3 = np.sum(np.sin(15 * np.pi * x_norm) ** 2 * np.exp(-np.abs(x_norm))) + 0.5 * np.sum(np.cos(23 * np.pi * x_norm) ** 2)
        
        # Adaptive polynomial penalty with dynamic scaling based on dimensionality
        f4 = 0.15 * np.sum(np.abs(x_norm)**7) + 0.08 * np.sum(x_norm**5) + 0.03 * np.sum(np.abs(x_norm)**4)
        
        # Cross-dimensional coupling with non-linear interaction terms
        f5 = 0.02 * np.sum((x_norm[:-1] - x_norm[1:]) ** 4) + 0.01 * np.sum(np.sin(np.pi * (x_norm[:-1] + x_norm[1:])) ** 2)
        
        # Additional chaotic basin term with exponential decay
        f6 = 0.05 * np.sum(np.exp(-np.abs(x_norm)) * np.sin(13 * np.pi * x_norm) ** 2)
        
        return f1 + 0.3 * f2 + 0.2 * f3 + 0.03 * f4 + 0.01 * f5 + 0.02 * f6