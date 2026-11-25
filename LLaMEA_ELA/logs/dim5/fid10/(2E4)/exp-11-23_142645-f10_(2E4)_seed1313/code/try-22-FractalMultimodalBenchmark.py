import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos component with mixed degrees
        poly_chaos = np.sum(x**2 + 0.3 * x**3 + 0.05 * x**5)
        
        # Radial basis function with varying widths and centers
        rbfs = 0.0
        centers = np.linspace(-4, 4, min(10, self.dim))
        for i in range(min(10, self.dim)):
            center = centers[i] if i < len(centers) else 0.0
            width = 0.5 + 0.5 * np.sin(i)
            rbfs += np.exp(-width * (x - center)**2)
        
        # Fractal-like perturbation using recursive sine waves
        fractal = 0.0
        for i in range(1, 6):
            fractal += np.sin(3**i * x) / (3**i)
        
        # Mixed trigonometric terms with varying frequencies
        trig_terms = np.sum(np.sin(x) + 0.5 * np.cos(2 * x) + 0.3 * np.sin(4 * x))
        
        # Asymmetric penalty for large values
        penalty = np.sum((x**2 + 0.1 * x**4) * (x > 2) + (x**2 + 0.05 * x**4) * (x < -2))
        
        # Cross-dimensional interaction terms with exponential decay
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interaction += np.exp(-0.1 * abs(x[i] - x[j])) * (x[i]**2 + x[j]**2)
        
        return poly_chaos + rbfs + fractal + trig_terms + penalty + 0.1 * cross_interaction