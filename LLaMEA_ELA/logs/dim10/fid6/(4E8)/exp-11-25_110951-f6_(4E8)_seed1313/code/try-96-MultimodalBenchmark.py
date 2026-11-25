import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Enhanced sinusoidal oscillatory component with multiple frequencies
        sin_component = np.sum(np.sin(12 * np.pi * x_normalized) * np.cos(6 * np.pi * x_normalized) + 
                              0.5 * np.sin(20 * np.pi * x_normalized) * np.cos(10 * np.pi * x_normalized))
        
        # Modified polynomial conditioning with higher-order terms
        poly_conditioning = np.sum((x_normalized ** 6) * (1 + 0.3 * np.sin(5 * np.pi * x_normalized)) + 
                                  0.2 * (x_normalized ** 3) * np.cos(2 * np.pi * x_normalized))
        
        # Enhanced radial basin term with multi-scale exponential decay
        r = np.sqrt(np.sum(x_normalized**2))
        basin_term = -np.exp(-r**3) * np.sin(7 * np.pi * r) * np.cos(3 * np.pi * r)
        
        # Advanced cross-dimensional interaction with higher-order coupling
        cross_interaction = 0.7 * np.sum(
            np.sin(5 * np.pi * x_normalized[:-1]) * 
            np.cos(5 * np.pi * x_normalized[1:]) * 
            (1 + 0.3 * np.sin(3 * np.pi * r)) * 
            np.cos(2 * np.pi * x_normalized[:-1] * x_normalized[1:])
        )
        
        # Stronger chaotic perturbation using nested trigonometric functions with fractal scaling
        chaos_perturbation = 0.5 * np.sum(
            np.sin(15 * np.pi * x_normalized) * 
            np.cos(12 * np.pi * x_normalized) * 
            np.sin(8 * np.pi * r) * 
            (1 + 0.4 * np.sin(4 * np.pi * r))
        )
        
        # Additional multi-scale modulation with dimensionality-dependent factors
        scale_factor = 1.5 + 0.3 * (self.dim - 1) + 0.1 * np.sin(self.dim * 0.5)
        
        # Add a global minimum attractor with adjustable strength
        global_attractor = 0.2 * np.exp(-r**2) * np.sin(10 * np.pi * r)
        
        # Combine all components with appropriate weighting
        return scale_factor * (sin_component + poly_conditioning + basin_term + cross_interaction + chaos_perturbation + global_attractor)