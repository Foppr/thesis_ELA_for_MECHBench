import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced exponential decay with multiple rates
        exp_decay = np.sum(np.exp(-0.5 * x_norm**2) * np.cos(4 * np.pi * x_norm) * np.sin(2 * np.pi * x_norm))
        
        # Increased sinusoidal frequency interactions
        trig_coupling = np.sum(np.sin(5 * x_norm) * np.cos(7 * x_norm)) + \
                        0.7 * np.sum(np.sin(9 * x_norm) * np.cos(11 * x_norm)) + \
                        0.3 * np.sum(np.sin(13 * x_norm) * np.cos(15 * x_norm))
        
        # Adaptive conditioning with enhanced non-separability
        conditioning = np.sum((x_norm**2) * np.exp(-0.2 * np.abs(x_norm)) * np.sin(3 * x_norm))
        
        # Additional polynomial cross-terms with higher degrees
        cross_poly = np.sum((x_norm[0] * x_norm[1])**4) + \
                     0.5 * np.sum(x_norm**6 * np.sin(4 * np.pi * x_norm)) + \
                     0.2 * np.sum(x_norm**3 * np.cos(5 * np.pi * x_norm))
        
        # Structured noise with temporal correlation
        noise = 0.02 * np.random.random() + 0.01 * np.sin(0.5 * np.sum(x_norm))
        
        # Combine all terms to create a multimodal landscape
        return exp_decay + trig_coupling + conditioning + cross_poly + noise