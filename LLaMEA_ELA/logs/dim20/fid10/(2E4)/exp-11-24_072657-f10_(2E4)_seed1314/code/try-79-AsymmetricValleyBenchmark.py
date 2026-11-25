import numpy as np

class AsymmetricValleyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Periodic parabolic valleys with asymmetric curvature
        valley_terms = np.sum((x_norm**2 + 0.3 * np.sin(3 * np.pi * x_norm))**2)
        
        # Asymmetric cross-dimensional interactions
        asym_interaction = 0.0
        for i in range(self.dim - 1):
            asym_interaction += (x_norm[i] * x_norm[i+1] + 
                               0.5 * np.abs(x_norm[i] - x_norm[i+1])**1.5) * \
                              np.exp(-0.2 * (x_norm[i]**2 + x_norm[i+1]**2))
        
        # Adaptive conditioning based on dimensionality
        condition_factor = 1.0 + 0.4 * np.log(self.dim + 1)
        
        # Multi-scale periodic modulation with varying amplitudes
        periodic_terms = np.sum(np.sin(2 * np.pi * x_norm) * 
                               np.cos(4 * np.pi * x_norm) * 
                               np.exp(-0.1 * np.abs(x_norm)))
        
        # Asymmetric exponential decay with dimension-dependent scaling
        exp_decay = np.sum(np.exp(-0.5 * np.abs(x_norm)) * 
                          (x_norm**2 + 0.2 * np.abs(x_norm)**3))
        
        # Combined landscape with varying weights and conditioning
        result = condition_factor * (0.8 * valley_terms + 
                                   0.6 * asym_interaction + 
                                   0.4 * periodic_terms + 
                                   0.3 * exp_decay)
        
        # Add controlled noise for increased complexity
        noise = 0.001 * np.random.random()
        
        return result + noise