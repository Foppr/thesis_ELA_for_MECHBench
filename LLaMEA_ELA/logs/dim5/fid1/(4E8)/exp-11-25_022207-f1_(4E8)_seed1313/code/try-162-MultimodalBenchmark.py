import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial fractal component with multiple scales
        r = np.sqrt(np.sum(x_norm**2))
        fractal_term = np.sin(10 * r) * np.cos(5 * r) * np.exp(-0.5 * r**2)
        
        # Sinusoidal coupling with varying frequencies
        coupling = 0.0
        for i in range(self.dim - 1):
            coupling += np.sin(3 * (x_norm[i] + x_norm[i+1])) * np.cos(2 * (x_norm[i] - x_norm[i+1]))
        
        # Multi-scale radial modulation
        radial_mod = np.sum((np.sin(8 * r) + np.cos(6 * r)) * np.exp(-0.3 * r**2))
        
        # Asymmetric polynomial interactions with exponential weighting
        poly_interaction = np.sum(x_norm**3 * (1 + 0.4 * np.sin(5 * x_norm)) * 
                                np.exp(-0.2 * np.abs(x_norm)))
        
        # Adaptive noise component that varies with position
        noise = np.sum(0.1 * np.sin(15 * x_norm) * np.cos(12 * x_norm) * 
                      (1 + 0.3 * np.sin(r)))
        
        # Saddle-point enhanced gradient field
        grad_field = np.sum((x_norm[:-1]**2 - x_norm[1:]**2)**3 * 
                          np.exp(-0.4 * np.abs(x_norm[:-1] - x_norm[1:])))
        
        # Combined fractal and coupling term with global scaling
        return 1.5 * (fractal_term + coupling + radial_mod + poly_interaction + 
                     noise + grad_field)