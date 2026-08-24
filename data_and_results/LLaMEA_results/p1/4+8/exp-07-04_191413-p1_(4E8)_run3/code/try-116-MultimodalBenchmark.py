import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial terms with varying degrees
        poly_term = np.sum(x_norm**4 + 0.5 * x_norm**3 + 0.2 * x_norm**2)
        
        # Trigonometric components with multiple frequencies
        trig_term = np.sum(np.sin(2 * np.pi * x_norm) + 0.5 * np.sin(5 * np.pi * x_norm) + 0.3 * np.sin(8 * np.pi * x_norm))
        
        # Radial basis function component with adaptive width
        rbfs = np.sum(np.exp(-2 * np.sum((x_norm.reshape(1, -1) - np.arange(-1, 2).reshape(-1, 1))**2, axis=1)))
        
        # Cross-dimensional coupling with exponential decay
        cross_coupling = np.sum(np.exp(-0.5 * np.sum((x_norm[:-1] - x_norm[1:])**2)) * np.sin(3 * np.pi * x_norm[:-1]) * np.cos(3 * np.pi * x_norm[1:]))
        
        # Adaptive conditioning based on dimensionality
        conditioning = np.sum((1 + 0.1 * self.dim) * x_norm**2)
        
        # Chaotic modulation using logistic map-like behavior
        chaotic_mod = np.sum(np.sin(np.pi * x_norm * np.sin(10 * np.pi * x_norm)))
        
        # Combine all terms with appropriate weights
        return poly_term + 0.7 * trig_term + 0.3 * rbfs + 0.2 * cross_coupling + conditioning + 0.15 * chaotic_mod