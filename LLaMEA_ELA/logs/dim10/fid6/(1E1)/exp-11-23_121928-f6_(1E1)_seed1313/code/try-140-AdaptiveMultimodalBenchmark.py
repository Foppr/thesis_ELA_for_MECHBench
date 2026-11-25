import numpy as np

class AdaptiveMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial base with varying degrees
        poly_term = np.sum((x_norm**3) + 0.5 * (x_norm**4) + 0.2 * (x_norm**5))
        
        # Trigonometric components with multiple frequencies
        trig_term = np.sum(np.sin(12 * x_norm) + np.cos(7 * x_norm) + np.sin(19 * x_norm**2) + np.cos(11 * x_norm**3))
        
        # Radial basis function component with adaptive width
        rbf_width = 0.5 + 0.5 * np.log(self.dim + 1)
        rbf_term = np.sum(np.exp(-rbf_width * np.sum((x_norm.reshape(-1, 1) - x_norm.reshape(1, -1))**2, axis=0)))
        
        # Asymmetrical scaling based on sign and magnitude
        asym_scale = np.sum(np.where(x_norm >= 0, x_norm**1.5, -0.7 * np.abs(x_norm)**1.3))
        
        # Adaptive conditioning based on dimensionality
        condition_factor = 1.0 + 0.3 * np.log(self.dim + 1) + 0.1 * np.std(x_norm)
        
        # Interaction term with exponential decay
        interaction = np.sum(np.exp(-np.abs(x_norm)) * np.sin(2 * np.pi * x_norm) * np.cos(3 * np.pi * x_norm))
        
        # Fractal-like self-similarity component
        fractal = np.sum(np.sin(np.pi * x_norm * np.sin(np.pi * x_norm))**2)
        
        # Combined function with weighted components
        return condition_factor * (0.4 * poly_term + 0.3 * trig_term - 0.15 * rbf_term + 0.1 * asym_scale + 0.05 * interaction + 0.03 * fractal) + 0.01 * np.sum(x_norm**6)