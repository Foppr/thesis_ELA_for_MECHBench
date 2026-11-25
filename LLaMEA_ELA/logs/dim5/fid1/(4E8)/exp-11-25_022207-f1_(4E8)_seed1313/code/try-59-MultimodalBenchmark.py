import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Nested sinusoidal oscillations with adaptive amplitudes and modified frequencies
        nested_term = np.sum(np.sin(3 * np.pi * x_norm) * np.cos(5 * np.pi * x_norm) * (1 + 0.4 * np.sin(7 * np.pi * x_norm)))
        
        # Enhanced cubic spline-like interactions with higher-order polynomial weights
        cubic_term = np.sum(x_norm**4 * np.cos(2 * x_norm))
        
        # Perturbed central repulsive force field with altered decay rate
        center_distance = np.sqrt(np.sum(x_norm**2))
        repulsion_term = 1.0 / (1.0 + center_distance**3)
        
        # Increased cross-dimensional coupling with stronger interaction strengths
        cross_term = 0.3 * np.sum((x_norm[:-1] - x_norm[1:])**2 * np.exp(-0.3 * (x_norm[:-1] + x_norm[1:])**2))
        
        # Add a scaling factor to control overall landscape complexity
        return nested_term + cubic_term - repulsion_term + cross_term