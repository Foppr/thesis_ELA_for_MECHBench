import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial base with mixed degrees for conditioning
        poly_base = np.sum(x_norm**4 + 0.5 * x_norm**3 + 0.2 * x_norm**2)
        
        # Asymmetric exponential terms to create skewed landscape
        exp_asym1 = np.sum(np.exp(2 * x_norm) - np.exp(-x_norm))
        exp_asym2 = np.sum(np.exp(-2 * x_norm) - np.exp(x_norm))
        
        # Trigonometric modulations with varying frequencies and amplitudes
        trig1 = np.sum(np.sin(3 * x_norm) * np.cos(5 * x_norm))
        trig2 = np.sum(np.sin(7 * x_norm) * np.cos(9 * x_norm))
        trig3 = np.sum(np.sin(4 * x_norm)**2 + np.cos(6 * x_norm)**2)
        
        # Radial component with adaptive scaling
        radial = np.sum((x_norm**2 + 0.1) * np.exp(-0.5 * x_norm**2))
        
        # Cross-term interactions with non-linear coupling
        cross_interaction = np.sum(x_norm * np.sin(8 * x_norm) * np.cos(3 * x_norm))
        
        # Adaptive scaling factor based on dimensionality
        scale_factor = 1.0 + 0.1 * np.log(self.dim + 1)
        
        # Combine all components with appropriate weights
        return scale_factor * (poly_base + 0.3 * exp_asym1 + 0.2 * exp_asym2 + 
                              0.25 * trig1 + 0.2 * trig2 + 0.15 * trig3 + 
                              0.1 * radial + 0.05 * cross_interaction)