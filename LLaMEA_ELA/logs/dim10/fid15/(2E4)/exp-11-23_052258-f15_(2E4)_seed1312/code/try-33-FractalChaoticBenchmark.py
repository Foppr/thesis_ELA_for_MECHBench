import numpy as np

class FractalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = np.sum(x**2) * 0.1
        
        # Nested sinusoidal modulations with varying frequencies and amplitudes
        f2 = 0.5 * np.sum(np.sin(2.0 * x) * np.sin(7.0 * x))
        
        # Fractal-like structure using recursive sine composition
        f3 = 0.3 * np.sum(np.sin(np.sin(3.0 * x)))
        
        # Multi-scale interaction terms creating self-similar patterns
        f4 = 0.2 * np.sum(np.sin(5.0 * x[:-1]) * np.cos(2.0 * x[1:]))
        
        # Non-smooth gradient transitions using absolute values and step functions
        f5 = 0.15 * np.sum(np.abs(x) ** 1.5)
        
        # Chaotic coupling between dimensions with exponential scaling
        f6 = 0.25 * np.sum(np.exp(-np.abs(x[:-2] - x[1:-1])) * x[2:]**2)
        
        # Combined fractal structure with varying scales
        f7 = 0.1 * np.sum(np.sin(4.0 * x) * np.cos(0.5 * x) * np.sin(0.1 * x))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7