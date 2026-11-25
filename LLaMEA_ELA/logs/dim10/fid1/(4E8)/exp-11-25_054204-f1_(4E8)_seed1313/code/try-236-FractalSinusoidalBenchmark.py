import numpy as np

class FractalSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal scaling factors
        self.fractal_factors = np.power(0.5, np.arange(dim))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # Multi-scale sinusoidal modulation with fractal scaling
        f2 = 0.0
        for i in range(self.dim):
            scale = self.fractal_factors[i]
            freq = 2.0 * (i + 1) * scale
            f2 += np.sin(freq * x[i]) * np.cos(freq * x[i] / 2.0)
        
        # Polynomial chaos with fractal coupling
        f3 = 0.3 * np.sum((x**4) * np.sin(x))
        
        # Geometric interaction terms with multi-scale coupling
        f4 = 0.0
        for i in range(self.dim - 1):
            scale = self.fractal_factors[i] * self.fractal_factors[i+1]
            f4 += scale * (x[i]**2 + x[i+1]**2) * np.sin(x[i] * x[i+1])
        
        # Fractal-like cross-dimensional interactions
        f5 = 0.25 * np.sum(np.sin(x) * np.cos(3.0 * x) * np.exp(-np.abs(x) / 2.0))
        
        # Multi-scale harmonic components
        f6 = 0.0
        for i in range(self.dim):
            scale = self.fractal_factors[i]
            freq = 1.0 + 2.0 * scale
            f6 += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5) * np.exp(-x[i]**2 / 10.0)
        
        # Combined fractal polynomial chaos
        f7 = 0.15 * np.sum((x**6) * np.cos(x) * np.sin(x))
        
        # Additional multi-scale geometric coupling
        f8 = 0.0
        for i in range(self.dim - 2):
            scale = self.fractal_factors[i] * self.fractal_factors[i+1] * self.fractal_factors[i+2]
            f8 += scale * np.sin(x[i] * x[i+1] * x[i+2])
        
        # Sine-cosine hybrid with exponential decay
        f9 = 0.2 * np.sum(np.sin(x) * np.cos(2.0 * x) * np.exp(-x**2 / 5.0))
        
        # Fractal-based power scaling
        f10 = 0.1 * np.sum(np.power(np.abs(x), 1.5 + self.fractal_factors))
        
        # Multi-scale oscillatory component
        f11 = 0.0
        for i in range(self.dim):
            scale = self.fractal_factors[i]
            freq = 3.0 * (i + 1) * scale
            f11 += np.sin(freq * x[i]) * np.cos(freq * x[i] / 3.0)
        
        # Combined scaling factor based on fractal properties
        scale_factor = 1.0 + 0.5 * np.sum(self.fractal_factors)
        
        return scale_factor * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11)