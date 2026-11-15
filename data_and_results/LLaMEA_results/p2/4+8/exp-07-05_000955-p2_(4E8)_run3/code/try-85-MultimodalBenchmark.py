import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos expansion term with mixed monomials
        f1 = np.sum(x**2 + 0.5 * x**3 + 0.1 * x**4)
        
        # Radial basis function component with multi-scale Gaussian kernels
        f2 = np.sum(np.exp(-0.5 * np.sum((x[:, np.newaxis] - np.linspace(-5, 5, 10))**2, axis=0)))
        
        # Trigonometric coupling with varying frequencies and amplitudes
        f3 = np.sum(np.sin(2.0 * x) * np.cos(3.0 * x) * np.sin(5.0 * x))
        
        # Non-separable interaction term using nested sine functions
        f4 = np.sum(np.sin(np.sum(np.sin(x**2))) * np.cos(np.sum(np.cos(x**3))))
        
        # Multi-modal component with exponential decay and sinusoidal modulation
        f5 = np.sum(np.exp(-0.1 * np.sum(x**2)) * np.sin(10.0 * x) * np.cos(7.0 * x))
        
        # Cross-dimensional coupling with polynomial interaction
        f6 = np.sum((x[:-1] * x[1:] + 0.5 * x[:-1]**2 * x[1:]**2) * np.sin(4.0 * x[:-1]))
        
        # Adaptive scaling term with dynamic frequency modulation
        f7 = np.sum(np.sin(15.0 * x + np.sin(8.0 * x)) * np.cos(12.0 * x + np.sin(6.0 * x)))
        
        # High-order polynomial with chaotic modulation
        f8 = np.sum(x**7 * np.sin(3.0 * x) * np.cos(2.0 * x))
        
        # Saddle point enhancement through mixed trigonometric and polynomial terms
        f9 = np.sum(np.sin(x) * np.cos(2.0 * x) * (x**2 - 1.0))
        
        # Combined landscape with weighted contributions
        return 0.1 * f1 + 0.2 * f2 + 0.15 * f3 + 0.1 * f4 + 0.1 * f5 + 0.1 * f6 + 0.1 * f7 + 0.05 * f8 + 0.1 * f9