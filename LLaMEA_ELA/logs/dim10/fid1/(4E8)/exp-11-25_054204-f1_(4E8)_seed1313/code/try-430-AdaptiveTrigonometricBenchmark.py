import numpy as np

class AdaptiveTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute adaptive weights based on dimension
        self.weights = np.exp(-np.arange(1, dim + 1) * 0.5)
        self.freqs = 2.0 + np.sin(np.arange(1, dim + 1) * np.pi / (dim + 1))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # Exponential decay with trigonometric modulation
        f2 = np.sum(np.exp(-x**2 / 10.0) * np.sin(self.freqs * x))
        
        # Radial basis function with adaptive scaling
        r = np.sqrt(np.sum(x**2))
        f3 = np.sum(np.exp(-r**2 / (2.0 * self.dim)) * np.cos(r))
        
        # Cross-dimensional trigonometric coupling
        f4 = 0.0
        for i in range(self.dim - 1):
            f4 += np.sin(x[i]) * np.cos(x[i+1]) * (i + 1) / self.dim
        
        # Adaptive polynomial with exponential weights
        f5 = np.sum(self.weights * x**4 * np.sin(x))
        
        # Multi-scale harmonic components
        f6 = 0.0
        for k in range(1, min(6, self.dim + 1)):
            f6 += np.sin(k * x) * np.cos(k * x / 2.0)
        
        # Sigmoidal fitness modulation
        f7 = np.sum(1.0 / (1.0 + np.exp(-x)) * np.sin(x**2))
        
        # Dimensionality-dependent radial interaction
        f8 = np.sum(np.exp(-np.abs(x) / self.dim) * np.cos(self.freqs * x))
        
        # Fractal-like coupling with varying exponents
        f9 = 0.0
        for i in range(self.dim - 2):
            f9 += np.sin(x[i] * x[i+1]**1.5) * np.cos(x[i+2]**2)
        
        # Combined adaptive scaling factor
        scale = 1.0 + 0.5 * np.log(self.dim + 1)
        
        return scale * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9)