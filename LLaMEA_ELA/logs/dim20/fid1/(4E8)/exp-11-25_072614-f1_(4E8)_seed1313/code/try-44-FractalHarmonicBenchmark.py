import numpy as np

class FractalHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Multi-scale harmonic components with fractal-like structure
        harmonic = np.sum(np.sin(2**np.arange(1, self.dim + 1) * x)) + \
                   0.5 * np.sum(np.cos(3**np.arange(1, self.dim + 1) * x)) + \
                   0.3 * np.sum(np.sin(5**np.arange(1, self.dim + 1) * x))
        
        # Self-similar fractal structure using recursive scaling
        fractal = np.sum(np.sin(x / (1.0 + np.abs(x))) * np.cos(x / (1.0 + np.abs(x)**2))) + \
                  0.2 * np.sum(np.sin(x**2 / (1.0 + x**4)) * np.cos(x**3 / (1.0 + x**6)))
        
        # Adaptive conditioning based on coordinate magnitude
        condition = np.sum((1.0 + 0.1 * np.abs(x)) * x**2) + \
                    0.05 * np.sum((1.0 + 0.05 * np.abs(x)**2) * x**4)
        
        # Multi-scale polynomial with varying exponents
        poly = np.sum(x**3) + 0.7 * np.sum(x**5) + 0.1 * np.sum(x**7) + \
               0.05 * np.sum(x**9)
        
        # Combined function with global minimum at origin
        return harmonic + fractal + condition + poly + 0.001 * np.sum(x**10)