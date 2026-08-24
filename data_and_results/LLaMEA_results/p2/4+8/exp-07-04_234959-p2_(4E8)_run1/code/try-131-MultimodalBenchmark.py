import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Global minimum at the center
        self.global_min = np.zeros(dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Logistic map based fractal component
        logistic_base = 4.0 * x * (1 - x / 5.0)
        fractal_term = np.sum(np.sin(logistic_base * np.pi) ** 2)
        
        # Trigonometric coupling with varying frequencies
        trig_coupling = np.sum(np.sin(2.0 * x) * np.cos(3.0 * x) + np.sin(0.5 * x) * np.cos(0.7 * x))
        
        # Polynomial chaos with exponential scaling
        poly_chaos = np.sum((x**4 - 10 * x**2 + 25) * np.exp(-0.1 * np.abs(x)))
        
        # Self-similar peak structure with multiple scales
        peak_structure = np.sum(np.exp(-0.5 * (x - 2.5)**2) + np.exp(-0.5 * (x + 2.5)**2))
        
        # Fractional Brownian motion inspired term
        fbm_like = np.sum(np.sin(x / 1.5) * np.cos(x / 2.0) * np.sin(x / 3.0))
        
        # Combined function with dynamic weights
        return 0.2 * fractal_term + 0.3 * trig_coupling + 0.25 * poly_chaos + 0.15 * peak_structure + 0.1 * fbm_like