import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial component with nested exponential decay and multiple sinusoidal modulations
        r = np.sqrt(np.sum(x_norm**2))
        radial_term = np.exp(-r**4) * (1 + 0.5 * np.sin(10 * r) + 0.3 * np.cos(15 * r))
        
        # Trigonometric modulation with multiple frequencies and interaction terms
        trig_term = np.sum(np.cos(4 * np.pi * x_norm) * np.sin(5 * np.pi * x_norm) * 
                          (1 + 0.2 * np.sin(7 * np.pi * x_norm)))
        
        # Chaotic component with nested sine maps and enhanced cross-dimensional interactions
        chaotic_term = 0.03 * np.sum(np.sin(7 * np.pi * x_norm) * np.cos(9 * np.pi * x_norm) * 
                                    (np.sin(4 * np.pi * x_norm) + 0.5 * np.cos(6 * np.pi * x_norm)))
        
        # Enhanced cross-dimensional interaction with polynomial coupling and dynamic weights
        cross_term = 0.2 * np.sum(np.abs(x_norm[:-1] - x_norm[1:]) * 
                                np.exp(-0.3 * (x_norm[:-1]**2 + x_norm[1:]**2)) * 
                                (1 + 0.1 * np.sin(5 * np.pi * (x_norm[:-1] + x_norm[1:]))))
        
        # Add a highly nonlinear scaling factor with multiple chaotic components
        scale_factor = 1.5 + 0.5 * np.sin(8 * r) * np.cos(6 * r) * np.sin(3 * r)
        
        # Add a global multimodal component with multiple peaks
        multi_peak = 0.1 * np.sum(np.sin(20 * np.pi * x_norm) * np.cos(15 * np.pi * x_norm))
        
        return scale_factor * (radial_term + trig_term + chaotic_term + cross_term + multi_peak)