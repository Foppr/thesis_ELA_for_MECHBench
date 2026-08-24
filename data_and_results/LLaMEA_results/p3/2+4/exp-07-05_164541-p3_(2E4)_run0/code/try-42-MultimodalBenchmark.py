import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Recursive trigonometric composition creating fractal-like structure
        fractal_term = np.sum(np.sin(np.pi * np.sin(np.pi * np.sin(np.pi * x))) ** 2)
        
        # Controlled chaotic oscillations with varying frequencies and amplitudes
        chaotic_term = np.sum(np.exp(-0.1 * x**2) * np.sin(2 * np.pi * x) * np.cos(3 * np.pi * x) * np.sin(5 * np.pi * x))
        
        # Polynomial chaos with mixed even/odd degrees and cross-dimensional interactions
        poly_chaos = np.sum(0.1 * x**10 + 0.3 * x**8 - 0.5 * x**6 + 0.7 * x**4 - 0.9 * x**2 + 0.2 * x)
        
        # Cross-dimensional coupling with implicit gradient-like behavior
        grad_coupling = np.sum((x[:-1] - x[1:])**2 * np.cos(2 * np.pi * (x[:-1] + x[1:])) * np.sin(3 * np.pi * (x[:-1] - x[1:])))
        
        # Multi-scale sinusoidal modulation with frequency scaling
        multi_scale = np.sum(np.sin(10 * np.pi * x) * np.cos(15 * np.pi * x) * np.sin(20 * np.pi * x))
        
        # Implicit local minimum attraction terms
        attraction = np.sum(0.01 * (x**2 - 1)**2 * np.exp(-0.5 * x**2))
        
        # Combine all terms with optimized weights and add global offset
        return 0.3 * fractal_term + 0.25 * chaotic_term + 0.08 * poly_chaos + 0.15 * grad_coupling + 0.12 * multi_scale + 0.05 * attraction + 3.0