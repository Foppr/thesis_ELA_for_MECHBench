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
        f2 = np.sum(np.sin(15 * np.pi * x_norm)**3)
        
        # Cosine product with varying frequencies and asymmetric shifts
        f3 = np.prod(np.cos(7 * x_norm + 0.5 * np.sin(3 * x_norm)))
        
        # Polynomial interaction term between adjacent dimensions with higher degree
        f4 = np.sum((x_norm[:-1] - x_norm[1:])**3)
        
        # Modified Rosenbrock-like term with cubic interactions
        f5 = np.sum((x_norm[:-1]**3 - x_norm[1:])**2)
        
        # Additional harmonic interaction with quintic terms and variable coupling
        f6 = np.sum(x_norm**5 * np.sin(7 * np.pi * x_norm))
        
        # Quintic polynomial interaction with altered coefficients and phase shifts
        f7 = np.sum((x_norm[:-1] ** 5 - x_norm[1:] ** 5) ** 2)
        
        # Cross-dimensional coupling with exponential decay
        f8 = np.sum(np.exp(-np.abs(x_norm[:-1] - x_norm[1:])) * (x_norm[:-1]**2 + x_norm[1:]**2))
        
        # Asymmetric cubic terms for additional challenge
        f9 = np.sum((x_norm[:-1] ** 3 - x_norm[1:] ** 4) ** 2)
        
        # Add small noise for additional challenge
        noise = 0.01 * np.random.random()
        
        return 0.3 * f1 + 1.5 * f2 + 0.4 * f3 + 0.7 * f4 + 1.0 * f5 + 0.5 * f6 + 0.3 * f7 + 0.6 * f8 + 0.4 * f9 + noise