import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic logistic map component for non-linearity and sensitivity
        logistic = np.sum(4 * x_norm * (1 - x_norm))
        
        # Multi-scale Gaussian peaks with varying amplitudes and widths
        peaks = 0
        scales = [0.5, 1.0, 2.0]
        for scale in scales:
            peaks += np.sum(np.exp(-scale * (x_norm**2).sum()) * 
                           np.cos(scale * np.pi * x_norm.sum()))
        
        # Non-separable polynomial interactions with asymmetric gradient
        poly_interaction = np.sum((x_norm[:-1]**2 + x_norm[1:]**2)**3 * 
                                np.exp(-0.5 * (x_norm[:-1] - x_norm[1:])**2) * 
                                np.sin(3 * np.pi * (x_norm[:-1] + x_norm[1:])))
        
        # Gradient-asymmetric corridor structure
        corridor = np.sum(np.exp(-0.3 * x_norm**2) * 
                         np.sin(4 * np.pi * x_norm) * 
                         np.cos(2 * np.pi * x_norm) * 
                         (1 + 0.5 * np.sin(6 * np.pi * x_norm)))
        
        # Perturbed repulsive force field
        repulsion = np.sum(np.exp(-2 * (x_norm**2).sum()) * 
                          np.sin(3 * np.pi * x_norm) * 
                          np.cos(5 * np.pi * x_norm.sum()) * 
                          np.tan(0.3 * x_norm))
        
        # Additional chaotic noise for robustness testing
        noise = 0.1 * np.random.normal(0, 1)
        
        return logistic + peaks + poly_interaction + corridor + repulsion + noise