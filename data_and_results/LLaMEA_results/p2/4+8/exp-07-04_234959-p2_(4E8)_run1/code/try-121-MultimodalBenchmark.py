import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like self-similar structure with multiple scales
        f1 = np.sum(np.sin(10 * x) * np.cos(5 * x) * np.sin(x**2))
        
        # Logarithmic barrier terms creating narrow traps
        f2 = np.sum(np.log(1 + np.abs(x)) * np.exp(-0.5 * x**2))
        
        # Adaptive gradient modulation based on local curvature
        grad_mod = np.abs(np.cos(x)) + 0.5
        f3 = np.sum((x**3 - 3 * x) * grad_mod)
        
        # Multi-scale sinusoidal interference
        f4 = np.sum(np.sin(x) * np.sin(3 * x) * np.sin(9 * x))
        
        # Exponential decay with oscillatory perturbations
        f5 = np.sum(np.exp(-0.1 * x**2) * np.cos(2 * np.pi * x))
        
        # Self-similar fractal component with recursive structure
        f6 = np.sum(np.sin(np.pi * x) * np.cos(np.pi * x) * np.sin(2 * np.pi * x))
        
        # Combine with varying weights and chaotic scaling factors
        return 0.15 * f1 + 0.25 * f2 + 0.20 * f3 + 0.15 * f4 + 0.15 * f5 + 0.10 * f6