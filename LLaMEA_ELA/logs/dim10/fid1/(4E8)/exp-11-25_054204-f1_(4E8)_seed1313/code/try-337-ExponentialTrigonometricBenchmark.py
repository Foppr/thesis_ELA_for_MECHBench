import numpy as np

class ExponentialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute adaptive weights based on dimension with fractal scaling
        self.weights = np.exp(-np.arange(dim) / (dim + 1)) * np.sin(np.pi * np.arange(dim) / (dim + 1))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base exponential decay term with dynamic scaling
        f1 = np.sum(np.exp(-x**2 / (5.0 + 0.5 * np.sin(0.3 * self.dim))))
        
        # Trigonometric coupling with adaptive weights and chaotic modulation
        f2 = 0.0
        for i in range(self.dim - 1):
            f2 += self.weights[i] * np.sin(x[i]) * np.cos(x[i+1]) * np.exp(-np.abs(x[i] - x[i+1]) / 3.0)
        f2 *= 0.5
        
        # Polynomial chaos with exponential scaling and fractal modulation
        f3 = 0.3 * np.sum((x**4) * np.exp(-x**2 / (4.0 + 0.2 * np.cos(0.5 * self.dim))))
        
        # Sine-cosine coupled harmonic terms with dynamic frequency
        f4 = 0.25 * np.sum(np.sin(x) * np.cos(2.0 * x) * np.exp(-np.abs(x) / (2.5 + 0.1 * np.sin(0.4 * self.dim))))
        
        # Adaptive cubic polynomial with dynamic scaling and chaotic coupling
        f5 = 0.2 * np.sum((x**3) * np.sin(x) * np.exp(-x**2 / (6.0 + 0.3 * np.cos(0.6 * self.dim))))
        
        # Multi-scale oscillation with frequency modulation and fractal structure
        f6 = 0.15 * np.sum(np.sin(3.0 * x + np.cos(x)) * np.cos(2.0 * x) * np.exp(-np.abs(x) / (3.0 + 0.2 * np.sin(0.7 * self.dim))))
        
        # Exponential decay with cross-dimensional interaction and chaotic coupling
        f7 = 0.1 * np.sum(np.exp(-np.abs(x) / 2.0) * np.sin(x**2) * np.cos(0.5 * x))
        
        # Fractal-inspired coupling with recursive structure and dynamic scaling
        f8 = 0.08 * np.sum(np.sin(x * np.cos(x)) * np.cos(x * np.sin(x)) * np.exp(-np.abs(x) / (4.0 + 0.1 * np.sin(0.8 * self.dim))))
        
        # Hyperbolic tangent modulation with chaotic frequency
        f9 = 0.12 * np.sum(np.tanh(x) * np.sin(1.5 * x) * np.cos(0.3 * x))
        
        # Cross-dimensional interaction with inverse scaling and fractal coupling
        cross_term = 0.0
        for i in range(self.dim - 1):
            cross_term += (1.0 / (1.0 + np.abs(x[i] - x[i+1]))) * np.sin(x[i] * x[i+1]) * np.exp(-np.abs(x[i] + x[i+1]) / 4.0)
        f10 = 0.09 * cross_term
        
        # Combined adaptive scaling factor with chaotic modulation
        scale_factor = 1.0 + 0.3 * np.log(self.dim + 1) + 0.1 * np.sin(0.2 * self.dim)
        
        # Return final function value with combined terms
        return scale_factor * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10)