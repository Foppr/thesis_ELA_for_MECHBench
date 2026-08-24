import numpy as np

class FractalRuggedLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        quadratic = 0.5 * np.sum(x**2)
        
        # Multiple Gaussian peaks with varying heights and widths
        peaks = 0.0
        for i in range(1, 6):
            center = np.full(self.dim, i * 0.8)
            height = i * 0.5
            width = 0.3 + i * 0.1
            peaks += height * np.exp(-0.5 * np.sum(((x - center) / width)**2))
        
        # Sinusoidal modulation with varying frequencies
        sin_mod = 0.0
        for i in range(self.dim):
            sin_mod += np.sin(2 * np.pi * x[i]) * np.cos(3 * np.pi * x[i])
        
        # Fractal-like structure using recursive trigonometric functions
        fractal = 0.0
        for i in range(self.dim):
            fractal += np.sin(2 * np.pi * x[i] * (1 + 0.1 * np.sin(5 * np.pi * x[i])))
        
        # Cross-dimensional interaction with exponential decay
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interaction += np.sin(x[i] * x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Polynomial terms for higher-order nonlinearity
        poly_terms = 0.01 * np.sum(x**5) + 0.02 * np.sum(x**6)
        
        # Add a component with recursive fractal structure
        recursive = 0.0
        for i in range(self.dim):
            recursive += np.sin(10 * np.sin(10 * x[i]))
        
        # Combine all components
        return quadratic + peaks + 0.5 * sin_mod + 0.3 * fractal + 0.4 * cross_interaction + poly_terms + 0.2 * recursive