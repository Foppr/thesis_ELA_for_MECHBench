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
        f2 = np.sum(np.sin(19 * np.pi * x_norm)**3)
        
        # Cosine product with varying frequencies and asymmetric shifts
        f3 = np.prod(np.cos(9 * x_norm + 0.7 * np.sin(5 * x_norm)))
        
        # Polynomial interaction term between adjacent dimensions with higher degree
        f4 = np.sum((x_norm[:-1] - x_norm[1:])**5)
        
        # Modified Rosenbrock-like term with cubic interactions
        f5 = np.sum((x_norm[:-1]**5 - x_norm[1:])**2)
        
        # Additional harmonic interaction with quintic terms and variable coupling
        f6 = np.sum(x_norm**7 * np.sin(9 * np.pi * x_norm))
        
        # Quintic polynomial interaction with altered coefficients and phase shifts
        f7 = np.sum((x_norm[:-1] ** 7 - x_norm[1:] ** 7) ** 2)
        
        # Cross-dimensional coupling with exponential decay
        f8 = np.sum(np.exp(-np.abs(x_norm[:-1] - x_norm[1:])) * (x_norm[:-1]**4 + x_norm[1:]**4))
        
        # Asymmetric cubic terms for additional challenge
        f9 = np.sum((x_norm[:-1] ** 5 - x_norm[1:] ** 6) ** 2)
        
        # Additional complex coupling with logarithmic scaling
        f10 = np.sum(np.log(np.abs(x_norm[:-1]) + 1) * np.sin(7 * x_norm[1:]))
        
        # Add small noise for additional challenge
        noise = 0.01 * np.random.random()
        
        return 0.4 * f1 + 1.7 * f2 + 0.5 * f3 + 0.8 * f4 + 1.2 * f5 + 0.6 * f6 + 0.4 * f7 + 0.7 * f8 + 0.5 * f9 + 0.3 * f10 + noise