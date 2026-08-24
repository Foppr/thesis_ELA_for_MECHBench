import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial fractal component with self-similar patterns
        r = np.sqrt(np.sum(x**2))
        fractal_term = np.sin(10 * r) * np.cos(5 * r) * np.exp(-0.1 * r**2)
        
        # Discontinuous gradient transitions with step functions
        step_term = np.sum(np.floor(2 * np.sin(x)) * np.cos(3 * x) + np.ceil(1.5 * np.cos(x)) * np.sin(2 * x))
        
        # Multi-scale oscillatory patterns with varying frequencies
        scale_term = np.sum(np.sin(15 * x) * np.cos(12 * x) * np.sin(8 * x) * np.cos(6 * x))
        
        # Geometric symmetry breaking with polynomial distortions
        symm_term = np.sum((x**2 - 2 * x + 1)**3 + (x**3 - 3 * x**2 + 3 * x - 1)**2)
        
        # Cross-dimensional interaction with exponential coupling
        cross_term = np.sum(np.exp(-0.5 * (x[:-1] - x[1:])**2) * np.sin(4 * np.pi * (x[:-1] + x[1:])))
        
        # Discontinuous local minima with chaotic perturbations
        chaos_term = np.sum(np.sin(20 * x) * np.cos(18 * x) * np.tan(0.5 * x))
        
        # Combine all terms with adaptive weights
        return 0.3 * fractal_term + 0.25 * step_term + 0.15 * scale_term + 0.1 * symm_term + 0.1 * cross_term + 0.05 * chaos_term + 3.0