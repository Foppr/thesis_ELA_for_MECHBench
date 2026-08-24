import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced exponential decay with multiple rates
        exp_decay = np.sum(np.exp(-0.3 * x_norm**2) * np.cos(3 * np.pi * x_norm)) + \
                    0.5 * np.sum(np.exp(-0.7 * x_norm**2) * np.sin(4 * np.pi * x_norm))
        
        # Increased sinusoidal frequency interactions
        trig_coupling = np.sum(np.sin(5 * x_norm) * np.cos(7 * x_norm)) + \
                        0.7 * np.sum(np.sin(9 * x_norm) * np.cos(11 * x_norm)) + \
                        0.3 * np.sum(np.sin(13 * x_norm) * np.cos(15 * x_norm))
        
        # Adaptive conditioning with exponential scaling
        conditioning = np.sum((x_norm**2) * np.exp(-0.2 * np.abs(x_norm))) + \
                       0.5 * np.sum((x_norm**3) * np.exp(-0.1 * np.abs(x_norm)))
        
        # Enhanced polynomial cross-terms with higher degrees
        cross_poly = np.sum((x_norm[0] * x_norm[1])**3) + \
                     0.4 * np.sum(x_norm**5 * np.sin(3 * np.pi * x_norm)) + \
                     0.2 * np.sum(x_norm**6 * np.cos(2 * np.pi * x_norm))
        
        # Structured noise with spatial correlation
        noise = 0.01 * np.random.random()
        spatial_noise = 0.005 * np.sum(np.sin(2 * np.pi * x_norm) * np.cos(2 * np.pi * x_norm))
        
        # Combine all terms to create a multimodal landscape
        return exp_decay + trig_coupling + conditioning + cross_poly + noise + spatial_noise