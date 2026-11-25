import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Exponential decay base with adaptive scaling
        exp_base = np.exp(-0.5 * np.sum(x_normalized**2))
        
        # Trigonometric wave interference with multiple frequencies
        wave_interference = np.sum(np.sin(10 * np.pi * x_normalized) * np.cos(7 * np.pi * x_normalized))
        
        # Adaptive ridge structure with varying amplitude
        ridge_term = 0.5 * np.sum((x_normalized**2) * np.sin(5 * np.pi * x_normalized)**2)
        
        # Multi-scale sinusoidal modulation with fractal-like behavior
        fractal_modulation = np.sum(np.sin(15 * np.pi * x_normalized) * np.cos(12 * np.pi * x_normalized) * 
                                   np.exp(-0.3 * np.abs(x_normalized)))
        
        # Cross-dimensional coupling with exponential interaction
        cross_coupling = 0.3 * np.sum(np.exp(-0.5 * (x_normalized[:-1]**2 + x_normalized[1:]**2)) * 
                                    np.sin(3 * np.pi * (x_normalized[:-1] + x_normalized[1:])))
        
        # Adaptive conditioning factor based on dimensionality
        condition_factor = 1.0 + 0.15 * (self.dim - 1)
        
        # Polynomial interaction with high-degree terms
        poly_interaction = 0.02 * np.sum(x_normalized**8)
        
        # Novel basin-forming exponential potential
        basin_potential = 0.4 * np.prod(np.exp(-0.5 * (x_normalized**2)) * np.cos(3 * np.pi * x_normalized))
        
        # Combine all components with proper weighting
        return condition_factor * (exp_base + wave_interference + ridge_term + fractal_modulation + 
                                 cross_coupling + poly_interaction + basin_potential)