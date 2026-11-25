import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Periodic attractor landscape with chaotic modulation
        attractor_field = np.sum(np.sin(3 * np.pi * x_norm) * np.cos(5 * np.pi * x_norm) * 
                                np.exp(-0.5 * x_norm**2) * (1 + 0.3 * np.sin(7 * np.pi * x_norm)))
        
        # Exponentially weighted coupling with asymmetric repulsion
        coupling = np.sum(np.exp(-0.3 * np.abs(x_norm[:-1] - x_norm[1:])) * 
                         (x_norm[:-1]**3 + x_norm[1:]**3) * 
                         (1 + 0.2 * np.cos(4 * (x_norm[:-1] + x_norm[1:]))))
        
        # Saddle-point repulsion with fractal-like gradient variations
        saddle_repulsion = np.sum((x_norm[:-1]**2 - x_norm[1:]**2)**3 * 
                                np.exp(-0.2 * (x_norm[:-1] - x_norm[1:])**2) * 
                                (1 + 0.4 * np.sin(6 * (x_norm[:-1] - x_norm[1:]))))
        
        # Chaotic gradient modulation using logistic map
        chaotic_mod = np.sum(np.log(1 + np.abs(x_norm)) * 
                           np.sin(2 * np.pi * x_norm) * 
                           np.cos(3 * np.pi * x_norm) * 
                           (1 + 0.5 * np.sin(8 * np.pi * x_norm)))
        
        # High-order polynomial with non-separable interactions and noise
        poly_interaction = np.sum(x_norm**6 * (1 + 0.4 * np.sin(2 * x_norm)) * 
                                np.exp(-0.1 * x_norm**2) * 
                                (1 + 0.3 * np.cos(5 * x_norm)))
        
        # Additional chaotic perturbation term with multi-scale frequency components
        perturbation = 0.5 * np.sum(np.sin(9 * np.pi * x_norm) * 
                                  np.cos(11 * np.pi * x_norm) * 
                                  np.sin(13 * np.pi * x_norm) * 
                                  np.exp(-0.2 * x_norm**2))
        
        # Asymmetric quartic with exponential weighting
        asymmetric_quartic = np.sum(x_norm**4 * (1 + 0.6 * np.sin(3 * x_norm)) * 
                                  np.exp(-0.4 * np.abs(x_norm)))
        
        return attractor_field + coupling + saddle_repulsion + chaotic_mod + poly_interaction + perturbation + asymmetric_quartic