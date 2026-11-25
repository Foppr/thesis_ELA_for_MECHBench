import numpy as np

class ChaoticTentFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Tent map component with chaotic dynamics
        tent_map = np.sum(1.0 - 2.0 * np.abs(x_norm - 0.5))
        
        # Fractal-like pattern using multiple sine waves with different frequencies
        fractal_pattern = 0.5 * np.sum(np.sin(10 * x_norm) + np.sin(20 * x_norm) + np.sin(30 * x_norm))
        
        # Dynamic interaction terms that depend on dimensionality
        dynamic_interaction = 0.3 * np.sum(x_norm[:-1] * x_norm[1:] * (1 + 0.1 * np.sin(self.dim * x_norm[:-1])))
        
        # Multi-scale harmonic components for varying optima sizes
        multi_scale = 0.2 * np.sum(np.sin(5 * x_norm) * np.cos(8 * x_norm) + 
                                  np.sin(15 * x_norm) * np.cos(25 * x_norm))
        
        # Asymmetric quadratic basin to introduce skewness
        asymmetric_quadratic = 0.1 * np.sum(np.where(x_norm >= 0, x_norm**2, 0.5 * x_norm**2))
        
        # Cross-dimensional coupling with exponential decay
        coupling = 0.15 * np.sum(np.exp(-np.abs(x_norm[:-1] - x_norm[1:])) * (x_norm[:-1]**2 + x_norm[1:]**2))
        
        # Add a chaotic noise term based on the input values
        chaos_noise = 0.05 * np.sum(np.sin(np.exp(x_norm)) * np.cos(np.exp(2 * x_norm)))
        
        # Fourth-order polynomial for increased nonlinearity and complexity
        fourth_order = 0.08 * np.sum(x_norm**4)
        
        return tent_map + fractal_pattern + dynamic_interaction + multi_scale + asymmetric_quadratic + coupling + chaos_noise + fourth_order