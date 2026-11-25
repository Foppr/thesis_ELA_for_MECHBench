import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Nested sinusoidal oscillations with adaptive amplitudes
        nested_term = np.sum(np.sin(2 * np.pi * x_norm) * np.cos(4 * np.pi * x_norm) * (1 + 0.3 * np.sin(6 * np.pi * x_norm)))
        
        # Cubic spline-like interactions with varying weights
        cubic_term = np.sum(x_norm**3 * np.cos(3 * x_norm))
        
        # Central repulsive force field to create multiple local minima
        center_distance = np.sqrt(np.sum(x_norm**2))
        repulsion_term = 1.0 / (1.0 + center_distance**2)
        
        # Cross-dimensional coupling with varying interaction strengths
        cross_term = 0.2 * np.sum((x_norm[:-1] - x_norm[1:])**2 * np.exp(-0.5 * (x_norm[:-1] + x_norm[1:])**2))
        
        # Add a scaling factor to control overall landscape complexity
        return nested_term + cubic_term - repulsion_term + cross_term