import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Quadratic base term
        f1 = np.sum(x_norm**2)
        
        # High-frequency sine terms creating many local minima with varying amplitudes
        f2 = np.sum(np.sin(17 * np.pi * x_norm)**3)
        
        # Cosine product with varying frequencies and asymmetric shifts
        f3 = np.prod(np.cos(8 * x_norm + 0.6 * np.sin(4 * x_norm)))
        
        # Polynomial interaction term between adjacent dimensions with higher degree
        f4 = np.sum((x_norm[:-1] - x_norm[1:])**4)
        
        # Modified Rosenbrock-like term with cubic interactions
        f5 = np.sum((x_norm[:-1]**4 - x_norm[1:])**2)
        
        # Additional harmonic interaction with quintic terms and variable coupling
        f6 = np.sum(x_norm**6 * np.sin(8 * np.pi * x_norm))
        
        # Quintic polynomial interaction with altered coefficients and phase shifts
        f7 = np.sum((x_norm[:-1] ** 6 - x_norm[1:] ** 6) ** 2)
        
        # Cross-dimensional coupling with exponential decay
        f8 = np.sum(np.exp(-np.abs(x_norm[:-1] - x_norm[1:])) * (x_norm[:-1]**3 + x_norm[1:]**3))
        
        # Asymmetric cubic terms for additional challenge
        f9 = np.sum((x_norm[:-1] ** 4 - x_norm[1:] ** 5) ** 2)
        
        # Add small noise for additional challenge
        noise = 0.01 * np.random.random()
        
        return 0.35 * f1 + 1.6 * f2 + 0.45 * f3 + 0.75 * f4 + 1.1 * f5 + 0.55 * f6 + 0.35 * f7 + 0.65 * f8 + 0.45 * f9 + noise