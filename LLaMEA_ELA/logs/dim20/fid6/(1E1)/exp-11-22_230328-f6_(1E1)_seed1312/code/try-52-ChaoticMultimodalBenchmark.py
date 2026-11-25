import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial component with nested exponential decay and sinusoidal modulation
        r = np.sqrt(np.sum(x_norm**2))
        radial_term = np.exp(-r**4) * (1 + 0.5 * np.sin(10 * r) * np.cos(7 * r))
        
        # Enhanced trigonometric modulation with multiple frequencies and phase shifts
        trig_term = np.sum(np.cos(5 * np.pi * x_norm) * np.sin(6 * np.pi * x_norm) * 
                          np.cos(4 * np.pi * x_norm) * np.sin(3 * np.pi * x_norm))
        
        # Chaotic component with nested sine maps and dynamic coupling
        chaotic_term = 0.05 * np.sum(np.sin(7 * np.pi * x_norm) * np.cos(9 * np.pi * x_norm) * 
                                    (np.sin(4 * np.pi * x_norm) + 0.3 * np.cos(5 * np.pi * x_norm)) * 
                                    np.exp(-0.3 * r**2))
        
        # Cross-dimensional interaction with dynamic weights and higher-order coupling
        cross_term = 0.2 * np.sum(np.abs(x_norm[:-2] - x_norm[1:-1]) * 
                                np.abs(x_norm[1:-1] - x_norm[2:]) * 
                                np.exp(-0.4 * np.abs(x_norm[:-2] + x_norm[1:-1] + x_norm[2:])))
        
        # Dynamic scaling factor with multiple chaotic components
        scale_factor = 1.5 + 0.3 * np.sin(6 * r) * np.cos(8 * r) + 0.2 * np.sin(12 * r)
        
        # Add a non-separable component to increase interdependence
        non_sep = 0.1 * np.sum((x_norm[:-1] * x_norm[1:]) ** 3)
        
        return scale_factor * (radial_term + trig_term + chaotic_term + cross_term + non_sep)