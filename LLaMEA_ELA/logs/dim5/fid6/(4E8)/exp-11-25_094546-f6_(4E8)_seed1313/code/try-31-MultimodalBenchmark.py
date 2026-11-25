import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial terms with varying degrees to create complex curvature
        f1 = np.sum(x_norm**4 + 0.5 * x_norm**3 + 0.2 * x_norm**2)
        
        # Trigonometric terms with multiple frequencies for fine-grained local optima
        f2 = np.sum(np.sin(2 * np.pi * x_norm) + 0.5 * np.sin(5 * np.pi * x_norm) + 0.3 * np.sin(8 * np.pi * x_norm))
        
        # Exponential terms to create steep gradients and challenging plateaus
        f3 = np.sum(np.exp(-x_norm**2) - 1.0)
        
        # Cross-terms to introduce dimension interaction effects
        f4 = np.sum(x_norm[:-1] * x_norm[1:] * np.sin(np.pi * x_norm[:-1]))
        
        # Combine all components with carefully chosen weights
        return 0.8 * f1 + 0.3 * f2 + 0.2 * f3 + 0.1 * f4