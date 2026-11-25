import numpy as np

class ExponentialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute adaptive weights based on dimension
        self.weights = np.exp(-np.arange(dim) / (dim + 1))
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base exponential decay term
        f1 = np.sum(np.exp(-x**2 / 8.0))
        
        # Trigonometric coupling with adaptive weights
        f2 = 0.0
        for i in range(self.dim - 1):
            f2 += self.weights[i] * np.sin(x[i]) * np.cos(x[i+1])
        f2 *= 0.6
        
        # Polynomial chaos with exponential scaling
        f3 = 0.4 * np.sum((x**4) * np.exp(-x**2 / 6.0))
        
        # Sine-cosine coupled harmonic terms
        f4 = 0.3 * np.sum(np.sin(x) * np.cos(2.0 * x) * np.exp(-np.abs(x) / 4.0))
        
        # Adaptive cubic polynomial with dynamic scaling
        f5 = 0.25 * np.sum((x**3) * np.sin(x) * np.exp(-x**2 / 10.0))
        
        # Multi-scale oscillation with frequency modulation
        f6 = 0.2 * np.sum(np.sin(4.0 * x + np.cos(x)) * np.cos(3.0 * x))
        
        # Exponential decay with cross-dimensional interaction
        f7 = 0.15 * np.sum(np.exp(-np.abs(x) / 3.0) * np.sin(x**2))
        
        # Fractal-inspired coupling with recursive structure
        f8 = 0.1 * np.sum(np.sin(x * np.cos(x)) * np.cos(x * np.sin(x)))
        
        # Hyperbolic tangent modulation
        f9 = 0.14 * np.sum(np.tanh(x) * np.sin(2.0 * x))
        
        # Cross-dimensional interaction with inverse scaling and modified coupling
        cross_term = 0.0
        for i in range(self.dim - 1):
            cross_term += (1.0 / (1.0 + 0.5 * np.abs(x[i] - x[i+1]))) * np.sin(1.5 * x[i] * x[i+1])
        f10 = 0.12 * cross_term
        
        # Combined adaptive scaling factor
        scale_factor = 1.0 + 0.4 * np.log(self.dim + 1)
        
        # Return final function value with combined terms
        return scale_factor * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10)