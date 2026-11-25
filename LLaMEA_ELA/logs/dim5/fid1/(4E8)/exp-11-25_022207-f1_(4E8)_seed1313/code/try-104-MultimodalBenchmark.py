import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Fractal basin structure with chaotic mappings
        fractal_term = np.sum(np.sin(3 * np.pi * x_norm) * 
                             np.cos(2.7 * np.pi * x_norm) * 
                             np.exp(-0.1 * np.abs(x_norm)) * 
                             (1 + 0.2 * np.sin(5 * np.pi * x_norm)))
        
        # Non-smooth gradient transitions with sharp valleys
        sharp_valleys = np.sum(np.abs(x_norm)**1.7 * 
                              np.cos(4 * np.pi * x_norm) * 
                              np.exp(-0.05 * x_norm**2))
        
        # Embedded periodic attractors with varying frequencies
        attractor_term = np.sum(np.sin(6 * x_norm) * 
                               np.cos(3 * x_norm) * 
                               (1 + 0.1 * np.sin(2 * x_norm)) * 
                               np.exp(-0.15 * np.abs(x_norm)))
        
        # Multi-scale oscillatory behavior with amplitude modulation
        scale_osc = np.sum(np.sin(2.5 * x_norm) * 
                          np.cos(3.5 * x_norm) * 
                          (1 + 0.3 * np.cos(4 * x_norm)) * 
                          np.exp(-0.2 * x_norm**2))
        
        # Asymmetric saddle points with directional bias
        saddle_points = np.sum((x_norm**2 - 0.5 * x_norm) * 
                              np.sin(3 * x_norm) * 
                              np.exp(-0.1 * x_norm**2))
        
        # Global conditioning through higher-order polynomial interactions
        global_cond = 0.1 * np.sum(x_norm**6 + 0.3 * x_norm**4)
        
        # Combine all terms with non-linear coupling
        return fractal_term + sharp_valleys - attractor_term + scale_osc + saddle_points + global_cond