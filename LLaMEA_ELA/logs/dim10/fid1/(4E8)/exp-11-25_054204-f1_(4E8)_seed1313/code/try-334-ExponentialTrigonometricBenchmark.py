import numpy as np

class ExponentialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute adaptive weights based on dimension with chaotic scaling
        self.weights = np.exp(-np.arange(dim) / (dim + 1)) * np.sin(np.arange(dim) * np.pi / (dim + 1))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base exponential decay term with chaotic modulation
        f1 = np.sum(np.exp(-x**2 / 8.0) * np.sin(x * np.pi / 4.0))
        
        # Trigonometric coupling with adaptive weights and fractal-like interaction
        f2 = 0.0
        for i in range(self.dim - 1):
            f2 += self.weights[i] * np.sin(x[i]) * np.cos(x[i+1]) * np.exp(-np.abs(x[i] - x[i+1]) / 3.0)
        f2 *= 0.6
        
        # Polynomial chaos with exponential scaling and chaotic exponent
        f3 = 0.4 * np.sum((x**5) * np.exp(-x**2 / 4.0) * np.cos(x))
        
        # Sine-cosine coupled harmonic terms with dynamic frequency
        f4 = 0.3 * np.sum(np.sin(x) * np.cos(3.0 * x) * np.exp(-np.abs(x) / 2.5))
        
        # Adaptive cubic polynomial with dynamic scaling and fractal modulation
        f5 = 0.25 * np.sum((x**3) * np.sin(x) * np.exp(-x**2 / 6.0) * np.cos(x**2))
        
        # Multi-scale oscillation with frequency modulation and chaotic coupling
        f6 = 0.2 * np.sum(np.sin(4.0 * x + np.cos(x)) * np.cos(3.0 * x) * np.exp(-np.abs(x) / 2.0))
        
        # Exponential decay with cross-dimensional interaction and fractal structure
        f7 = 0.15 * np.sum(np.exp(-np.abs(x) / 1.5) * np.sin(x**2) * np.cos(x))
        
        # Fractal-inspired coupling with recursive structure and chaotic scaling
        f8 = 0.12 * np.sum(np.sin(x * np.cos(x)) * np.cos(x * np.sin(x)) * np.exp(-x**2 / 10.0))
        
        # Hyperbolic tangent modulation with fractal frequency
        f9 = 0.15 * np.sum(np.tanh(x) * np.sin(2.0 * x) * np.cos(x**3))
        
        # Cross-dimensional interaction with inverse scaling and chaotic coupling
        cross_term = 0.0
        for i in range(self.dim - 1):
            cross_term += (1.0 / (1.0 + np.abs(x[i] - x[i+1]))) * np.sin(x[i] * x[i+1]) * np.cos(x[i] + x[i+1])
        f10 = 0.1 * cross_term
        
        # Fractal-based adaptive scaling factor with chaotic modulation
        scale_factor = 1.0 + 0.4 * np.log(self.dim + 1) * np.sin(np.pi * self.dim / (self.dim + 2))
        
        # Return final function value with combined terms
        return scale_factor * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10)