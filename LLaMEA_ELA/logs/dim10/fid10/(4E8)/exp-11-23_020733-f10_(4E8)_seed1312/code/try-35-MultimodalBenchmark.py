import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Polynomial basins with varying curvature
        poly_basin = np.sum(x_scaled**6 + 0.7 * x_scaled**4 + 0.3 * x_scaled**2)
        
        # Sinusoidal modulation creating multiple local optima
        sin_mod = np.sum(np.sin(10 * np.pi * x_scaled) * np.cos(7 * np.pi * x_scaled))
        
        # Chaotic saddle point with exponential repulsion
        chaotic_term = np.sum(np.exp(-x_scaled**2 / 0.2) * np.sin(3 * np.pi * x_scaled))
        
        # Cross-dimensional coupling with hyperbolic tangent interactions
        cross_coupling = np.sum(np.tanh(x_scaled[:-1] * x_scaled[1:]) * (x_scaled[:-1]**2 + x_scaled[1:]**2))
        
        # Quadratic barrier with sinusoidal perturbation
        barrier = np.sum(0.5 * x_scaled**2 + 0.2 * np.sin(4 * np.pi * x_scaled))
        
        # Multi-modal interaction term with varying frequencies
        multi_interaction = np.sum(np.sin(6 * np.pi * x_scaled[:-1]) * np.cos(5 * np.pi * x_scaled[1:]))
        
        # Shifted global minimum with chaotic perturbation
        shift = np.sum((x_scaled - 0.05 * np.sin(2 * np.pi * x_scaled))**2)
        
        # Combine all terms with different weights
        return 0.9 * poly_basin + 0.6 * sin_mod + 0.4 * chaotic_term + 0.3 * cross_coupling + 0.2 * barrier + 0.15 * multi_interaction + 0.1 * shift