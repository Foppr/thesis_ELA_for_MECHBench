import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced chaotic attractor with fractal modulation and higher frequency components
        attractor_field = np.sum(np.sin(5 * np.pi * x_norm) * 
                                np.cos(7 * np.pi * x_norm) * 
                                np.exp(-0.4 * x_norm**2) * 
                                (1 + 0.5 * np.sin(9 * np.pi * x_norm)) * 
                                np.log(1 + 0.6 * np.abs(x_norm)))
        
        # Improved exponential coupling with directional bias and increased non-separability
        coupling = np.sum(np.exp(-0.5 * np.abs(x_norm[:-1] - x_norm[1:])) * 
                         (x_norm[:-1]**2 + x_norm[1:]**2) * 
                         (1 + 0.4 * np.cos(6 * (x_norm[:-1] + x_norm[1:]))))
        
        # Enhanced saddle-point repulsion with multi-scale gradient variations and stronger forcing
        saddle_repulsion = np.sum((x_norm[:-1]**2 - x_norm[1:]**2)**5 * 
                                np.exp(-0.4 * (x_norm[:-1] - x_norm[1:])**2) * 
                                (1 + 0.6 * np.sin(8 * (x_norm[:-1] - x_norm[1:]))))
        
        # Refined chaotic gradient modulation with higher frequency components and stronger chaos
        chaotic_mod = np.sum(np.sin(4 * np.pi * x_norm) * 
                           np.cos(5 * np.pi * x_norm) * 
                           np.exp(-0.3 * np.abs(x_norm)) * 
                           (1 + 0.7 * np.sin(10 * np.pi * x_norm)))
        
        # Modified polynomial interaction with stronger non-separability and higher degree terms
        poly_interaction = np.sum(x_norm**6 * (1 + 0.6 * np.sin(4 * x_norm)) * 
                                np.exp(-0.2 * x_norm**2) * 
                                (1 + 0.5 * np.cos(7 * x_norm)))
        
        # Additional perturbation with asymmetric harmonic components and increased amplitude
        perturbation = 0.8 * np.sum(np.sin(12 * np.pi * x_norm) * 
                                  np.cos(14 * np.pi * x_norm) * 
                                  np.exp(-0.3 * x_norm**2))
        
        # Enhanced asymmetric quartic with modified exponential weighting and higher order terms
        asymmetric_quartic = np.sum(x_norm**5 * (1 + 0.8 * np.sin(5 * x_norm)) * 
                                  np.exp(-0.4 * np.abs(x_norm)) * 
                                  (1 + 0.3 * np.cos(6 * x_norm)))
        
        # Add global scaling factor for better conditioning and increased difficulty
        return 1.2 * (attractor_field + coupling + saddle_repulsion + chaotic_mod + 
                     poly_interaction + perturbation + asymmetric_quartic)