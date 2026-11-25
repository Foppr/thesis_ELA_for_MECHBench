import numpy as np

class FractalSkewedBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Self-similar Gaussian peaks with fractal scaling
        f1 = np.sum(np.exp(-np.sum((x[:, None] - np.linspace(-5, 5, 20))**2, axis=0) / (2 * (0.5 + 0.5 * np.sin(self.dim)))) * 
                   np.exp(-0.5 * np.sum((x[:, None] - np.linspace(-5, 5, 20))**2, axis=0) / (2 * (1.0 + 0.3 * np.cos(self.dim)))))
        
        # Logarithmic barrier near boundaries
        f2 = np.sum(1.0 / (1.0 + np.log(1.0 + np.abs(x) / 5.0))**2)
        
        # Directional skewness with multi-scale sinusoidal modulation
        f3 = np.sum(np.sin(2 * np.pi * x) * np.cos(3 * np.pi * x) * 
                   np.exp(-0.1 * np.abs(x)) * (1 + 0.2 * np.sin(self.dim * x)))
        
        # Multi-modal structure with varying curvature
        f4 = np.sum((x**6 + 0.5 * x**4 + 0.2 * x**2 + 0.05) * 
                   np.exp(-0.05 * np.abs(x)) * np.cos(10 * x))
        
        # Cross-dimensional coupling with asymmetric interaction
        f5 = np.sum(np.sin(x[:-1] * x[1:]) * np.exp(-0.1 * (x[:-1]**2 + x[1:]**2)))
        
        # Fractal dimensionality scaling
        f6 = np.sum((np.abs(x) + 1)**(1.5 + 0.5 * np.sin(self.dim))) / self.dim
        
        # Combined with a smooth but non-convex base
        f7 = 0.5 * np.sum(np.sin(2 * x) + 0.3 * np.cos(3 * x)) / self.dim
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7