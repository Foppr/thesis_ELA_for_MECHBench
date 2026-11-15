import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Intensified exponential decay with multiple rates and dynamic modulation
        exp_decay = np.sum(np.exp(-0.5 * x_norm**2) * np.cos(5 * np.pi * x_norm)) + \
                    0.7 * np.sum(np.exp(-0.9 * x_norm**2) * np.sin(6 * np.pi * x_norm)) + \
                    0.3 * np.sum(np.exp(-0.4 * x_norm**2) * np.cos(8 * np.pi * x_norm))
        
        # Augmented sinusoidal frequency interactions with higher harmonics
        trig_coupling = np.sum(np.sin(7 * x_norm) * np.cos(9 * x_norm)) + \
                        0.8 * np.sum(np.sin(11 * x_norm) * np.cos(13 * x_norm)) + \
                        0.5 * np.sum(np.sin(15 * x_norm) * np.cos(17 * x_norm)) + \
                        0.2 * np.sum(np.sin(19 * x_norm) * np.cos(21 * x_norm))
        
        # Dynamic conditioning with adaptive scaling and non-linear transformations
        conditioning = np.sum((x_norm**2) * np.exp(-0.3 * np.abs(x_norm))) + \
                       0.6 * np.sum((x_norm**3) * np.exp(-0.2 * np.abs(x_norm))) + \
                       0.4 * np.sum((x_norm**4) * np.exp(-0.1 * np.abs(x_norm)))
        
        # Augmented polynomial cross-terms with higher degrees and mixed interactions
        cross_poly = np.sum((x_norm[0] * x_norm[1])**4) + \
                     0.5 * np.sum(x_norm**6 * np.sin(4 * np.pi * x_norm)) + \
                     0.3 * np.sum(x_norm**7 * np.cos(3 * np.pi * x_norm)) + \
                     0.1 * np.sum(x_norm**8 * np.sin(5 * np.pi * x_norm))
        
        # Layered noise with temporal and spatial correlation
        noise = 0.02 * np.random.random()
        spatial_noise = 0.01 * np.sum(np.sin(3 * np.pi * x_norm) * np.cos(3 * np.pi * x_norm)) + \
                        0.005 * np.sum(np.sin(4 * np.pi * x_norm) * np.cos(4 * np.pi * x_norm))
        
        # Combine all terms to create a highly multimodal landscape
        return exp_decay + trig_coupling + conditioning + cross_poly + noise + spatial_noise