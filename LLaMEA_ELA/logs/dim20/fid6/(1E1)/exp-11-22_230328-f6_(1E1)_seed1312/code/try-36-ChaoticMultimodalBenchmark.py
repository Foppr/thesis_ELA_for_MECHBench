import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial component with exponential decay and fractal-like perturbations
        r = np.sqrt(np.sum(x_norm**2))
        radial_term = np.exp(-r**2) * (1 + 0.3 * np.sin(15 * r) * np.cos(7 * r))
        
        # Trigonometric modulation with varying frequencies and amplitudes
        trig_term = np.sum(np.cos(3 * np.pi * x_norm) * np.sin(5 * np.pi * x_norm) * 
                          (1 + 0.2 * np.sin(8 * np.pi * x_norm)))
        
        # Chaotic component with higher frequency interactions and sine-cosine coupling
        chaotic_term = 0.02 * np.sum(np.sin(8 * np.pi * x_norm) * np.cos(9 * np.pi * x_norm) * 
                                    (np.sin(3 * np.pi * x_norm) + 0.4 * np.cos(4 * np.pi * x_norm)))
        
        # Cross-dimensional interaction with dynamic weights and non-linear coupling
        cross_term = 0.15 * np.sum(np.abs(x_norm[:-1] - x_norm[1:]) * 
                                 np.exp(-np.abs(x_norm[:-1] + x_norm[1:])) * 
                                 (1 + 0.1 * np.sin(6 * r)))
        
        # Add fractal-like irregularity using multiple sine waves with different periods
        fractal_irregularity = 0.05 * np.sum(np.sin(20 * np.pi * x_norm) * 
                                           np.cos(12 * np.pi * x_norm) * 
                                           np.sin(18 * np.pi * x_norm))
        
        # Dynamic scaling factor based on position and dimensionality
        scale_factor = 1.5 + 0.4 * np.sin(3 * r) * np.cos(2 * self.dim) * np.sin(0.5 * r)
        
        return scale_factor * (radial_term + trig_term + chaotic_term + cross_term + fractal_irregularity)