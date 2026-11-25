import numpy as np

class ExponentialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute frequency components for trigonometric interactions
        self.frequencies = np.arange(1, dim + 1) * 0.5
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic base term
        f1 = np.sum(x**2)
        
        # Exponential decay with trigonometric modulation
        f2 = np.sum(np.exp(-0.1 * np.abs(x)) * np.cos(self.frequencies * x))
        
        # Saddle-point inducing term with polynomial and exponential interaction
        f3 = 0.5 * np.sum((x**4) * np.exp(-x**2 / 10.0))
        
        # Coupling between dimensions using sine and cosine products
        f4 = 0.3 * np.sum(np.sin(x[:-1]) * np.cos(x[1:]) * np.exp(-0.05 * (x[:-1]**2 + x[1:]**2)))
        
        # Multimodal component with Gaussian peaks and trigonometric modulation
        f5 = 0.4 * np.sum(np.exp(-0.5 * (x - 1.0)**2) * np.sin(3.0 * x))
        
        # Cross-dimensional exponential interaction
        f6 = 0.2 * np.sum(np.exp(-0.2 * np.abs(x[:-1] - x[1:])) * np.cos(2.0 * (x[:-1] + x[1:])))
        
        # High-order polynomial with sinusoidal perturbation
        f7 = 0.15 * np.sum((x**6) * np.sin(0.5 * x))
        
        # Asymmetric saddle structure
        f8 = 0.25 * np.sum(x**3 * np.exp(-x**2 / 8.0))
        
        # Fractal-like interaction using recursive frequency scaling
        f9 = 0.1 * np.sum(np.sin(self.frequencies * x) * np.cos(0.3 * x**2))
        
        # Dimensional scaling effect with exponential weights
        weights = np.exp(-np.arange(dim) / (dim + 1))
        f10 = 0.3 * np.sum(weights * np.abs(x)**1.5)
        
        # Combined function with adaptive scaling
        scale_factor = 1.0 + 0.2 * np.log(self.dim + 1)
        
        return scale_factor * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10)