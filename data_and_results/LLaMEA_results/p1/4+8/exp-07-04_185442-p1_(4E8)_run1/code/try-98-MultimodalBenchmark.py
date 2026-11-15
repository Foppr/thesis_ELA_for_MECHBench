import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced exponential decay with multiple rates
        exp_decay = np.sum(np.exp(-0.3 * x_norm**2) * np.cos(3 * np.pi * x_norm)) + \
                    0.7 * np.sum(np.exp(-0.7 * x_norm**2) * np.sin(4 * np.pi * x_norm))
        
        # Increased sinusoidal frequency interactions
        trig_coupling = np.sum(np.sin(5 * x_norm) * np.cos(7 * x_norm)) + \
                        0.6 * np.sum(np.sin(9 * x_norm) * np.cos(11 * x_norm)) + \
                        0.3 * np.sum(np.sin(13 * x_norm) * np.cos(15 * x_norm))
        
        # Modified adaptive conditioning with exponential scaling
        conditioning = np.sum((x_norm**2) * np.exp(-0.2 * np.abs(x_norm))) + \
                       0.5 * np.sum(np.exp(-0.1 * x_norm**2) * x_norm**3)
        
        # Additional polynomial cross-terms with higher degree interactions
        cross_poly = np.sum((x_norm[0] * x_norm[1])**3) + \
                     0.4 * np.sum(x_norm**5 * np.sin(3 * np.pi * x_norm)) + \
                     0.2 * np.sum(x_norm**3 * np.cos(2 * np.pi * x_norm))
        
        # New structured noise component with periodic modulation
        noise = 0.03 * np.random.random() * np.sin(0.5 * np.sum(x_norm**2))
        
        # Combine all terms to create a highly complex multimodal landscape
        return exp_decay + trig_coupling + conditioning + cross_poly + noise