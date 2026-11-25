import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced chaotic attractor with fractal modulation
        attractor_field = np.sum(np.sin(4 * np.pi * x_norm) * 
                                np.cos(6 * np.pi * x_norm) * 
                                np.exp(-0.3 * x_norm**2) * 
                                (1 + 0.4 * np.sin(8 * np.pi * x_norm)) * 
                                np.log(1 + 0.5 * np.abs(x_norm)))
        
        # Improved exponential coupling with directional bias
        coupling = np.sum(np.exp(-0.4 * np.abs(x_norm[:-1] - x_norm[1:])) * 
                         (x_norm[:-1]**2 + x_norm[1:]**2) * 
                         (1 + 0.3 * np.cos(5 * (x_norm[:-1] + x_norm[1:]))))
        
        # Enhanced saddle-point repulsion with multi-scale gradient variations
        saddle_repulsion = np.sum((x_norm[:-1]**2 - x_norm[1:]**2)**4 * 
                                np.exp(-0.3 * (x_norm[:-1] - x_norm[1:])**2) * 
                                (1 + 0.5 * np.sin(7 * (x_norm[:-1] - x_norm[1:]))))
        
        # Refined chaotic gradient modulation with higher frequency components
        chaotic_mod = np.sum(np.sin(3 * np.pi * x_norm) * 
                           np.cos(4 * np.pi * x_norm) * 
                           np.exp(-0.2 * np.abs(x_norm)) * 
                           (1 + 0.6 * np.sin(9 * np.pi * x_norm)))
        
        # Modified polynomial interaction with stronger non-separability
        poly_interaction = np.sum(x_norm**5 * (1 + 0.5 * np.sin(3 * x_norm)) * 
                                np.exp(-0.15 * x_norm**2) * 
                                (1 + 0.4 * np.cos(6 * x_norm)))
        
        # Additional perturbation with asymmetric harmonic components
        perturbation = 0.6 * np.sum(np.sin(10 * np.pi * x_norm) * 
                                  np.cos(12 * np.pi * x_norm) * 
                                  np.exp(-0.25 * x_norm**2))
        
        # Enhanced asymmetric quartic with modified exponential weighting
        asymmetric_quartic = np.sum(x_norm**4 * (1 + 0.7 * np.sin(4 * x_norm)) * 
                                  np.exp(-0.3 * np.abs(x_norm)) * 
                                  (1 + 0.2 * np.cos(5 * x_norm)))
        
        # Add global scaling factor for better conditioning
        return 0.8 * (attractor_field + coupling + saddle_repulsion + chaotic_mod + 
                     poly_interaction + perturbation + asymmetric_quartic)