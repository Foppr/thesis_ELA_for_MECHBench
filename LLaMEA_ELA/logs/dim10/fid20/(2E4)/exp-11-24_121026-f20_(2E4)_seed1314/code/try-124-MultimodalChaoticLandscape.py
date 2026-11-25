import numpy as np

class MultimodalChaoticLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Radial basis function component with chaotic frequency modulation
        rb_func = np.sum(np.exp(-np.sum((x_norm[:, np.newaxis] - np.linspace(-1, 1, self.dim))**2, axis=0)) * 
                        np.sin(10 * np.pi * x_norm)**2)
        
        # Sinusoidal oscillation with varying frequencies and chaotic coupling
        sin_term = np.sum(np.sin(15 * x_norm + np.sin(7 * x_norm))**4)
        
        # Exponential decay with radial dependence and chaotic modulation
        exp_decay = np.sum(np.exp(-0.5 * np.sum(x_norm**2)) * (1 + 0.3 * np.sin(12 * x_norm)))
        
        # Multimodal component with multiple peaks and chaotic amplitude scaling
        multimodal = np.sum((np.sin(8 * x_norm) + 0.5 * np.sin(16 * x_norm))**2 * 
                           (1 + 0.4 * np.cos(9 * x_norm)))
        
        # Cross-dimensional interaction with chaotic coupling weights
        cross_term = np.sum(x_norm[:-1] * x_norm[1:] * np.exp(-np.abs(x_norm[:-1] - x_norm[1:]) * 2))
        
        # Polynomial chaos component with exponential scaling
        poly_chaos = np.sum((x_norm**3 + 0.3 * x_norm**2 - 0.4 * x_norm)**2 * 
                           np.exp(-0.8 * np.abs(x_norm)))
        
        # Fractional power chaotic term
        frac_term = np.sum(np.abs(x_norm)**1.7 * np.sin(14 * x_norm)**3)
        
        # Boundary influence with logarithmic scaling
        boundary = np.sum(np.log(1 + 0.5 * np.abs(x_norm)) * np.exp(-0.3 * x_norm**2))
        
        # Combined chaotic interaction
        chaotic_interaction = np.sum(np.sin(20 * x_norm) * np.cos(13 * x_norm) * 
                                   (1 + 0.2 * np.sin(8 * x_norm)))
        
        return (0.5 * rb_func + 0.3 * sin_term + 0.4 * exp_decay + 0.25 * multimodal + 
                0.2 * cross_term + 0.35 * poly_chaos + 0.15 * frac_term + 0.1 * boundary + 
                0.18 * chaotic_interaction)