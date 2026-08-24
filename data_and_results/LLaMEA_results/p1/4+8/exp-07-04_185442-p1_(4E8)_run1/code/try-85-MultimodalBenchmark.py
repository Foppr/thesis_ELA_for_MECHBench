import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponential decay with multiple rates and trigonometric modulations
        exp_decay = np.sum(np.exp(-0.5 * x_norm**2) * np.cos(2 * np.pi * x_norm)) + \
                    0.3 * np.sum(np.exp(-0.8 * x_norm**2) * np.sin(5 * np.pi * x_norm))
        
        # High-frequency trigonometric couplings
        trig_coupling = np.sum(np.sin(10 * x_norm) * np.cos(8 * x_norm)) + \
                        0.6 * np.sum(np.sin(15 * x_norm) * np.cos(12 * x_norm)) + \
                        0.4 * np.sum(np.sin(20 * x_norm) * np.cos(18 * x_norm))
        
        # Adaptive conditioning with polynomial scaling
        conditioning = np.sum(x_norm**2 * np.exp(-0.3 * np.abs(x_norm))) + \
                       0.4 * np.sum(x_norm**4 * np.exp(-0.1 * np.abs(x_norm)))
        
        # Higher-order polynomial cross-terms with sinusoidal interactions
        cross_poly = np.sum((x_norm[0] * x_norm[1])**4) + \
                     0.3 * np.sum(x_norm**6 * np.sin(4 * np.pi * x_norm)) + \
                     0.1 * np.sum(x_norm**7 * np.cos(3 * np.pi * x_norm))
        
        # Structured noise with spatial correlation
        noise = 0.02 * np.random.random()
        spatial_noise = 0.01 * np.sum(np.sin(3 * np.pi * x_norm) * np.cos(3 * np.pi * x_norm))
        
        # Combine all terms to create a multimodal landscape
        return exp_decay + trig_coupling + conditioning + cross_poly + noise + spatial_noise