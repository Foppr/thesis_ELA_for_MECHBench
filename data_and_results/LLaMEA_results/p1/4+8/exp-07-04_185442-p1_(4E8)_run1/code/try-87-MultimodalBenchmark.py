import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced exponential decay with multiple rates and sinusoidal modulation
        exp_decay = np.sum(np.exp(-0.2 * x_norm**2) * np.cos(4 * np.pi * x_norm)) + \
                    0.6 * np.sum(np.exp(-0.5 * x_norm**2) * np.sin(5 * np.pi * x_norm))
        
        # Increased sinusoidal frequency interactions with higher harmonics
        trig_coupling = np.sum(np.sin(6 * x_norm) * np.cos(8 * x_norm)) + \
                        0.8 * np.sum(np.sin(10 * x_norm) * np.cos(12 * x_norm)) + \
                        0.4 * np.sum(np.sin(14 * x_norm) * np.cos(16 * x_norm))
        
        # Adaptive conditioning with exponential scaling and polynomial adjustments
        conditioning = np.sum((x_norm**2) * np.exp(-0.1 * np.abs(x_norm))) + \
                       0.4 * np.sum((x_norm**3) * np.exp(-0.05 * np.abs(x_norm))) + \
                       0.2 * np.sum(x_norm**4 * np.exp(-0.1 * np.abs(x_norm)))
        
        # Enhanced polynomial cross-terms with higher degrees and trigonometric modulation
        cross_poly = np.sum((x_norm[0] * x_norm[1])**4) + \
                     0.5 * np.sum(x_norm**5 * np.sin(4 * np.pi * x_norm)) + \
                     0.3 * np.sum(x_norm**6 * np.cos(3 * np.pi * x_norm)) + \
                     0.1 * np.sum(x_norm**7 * np.sin(2 * np.pi * x_norm))
        
        # Structured noise with spatial correlation and temporal component
        noise = 0.01 * np.random.random()
        spatial_noise = 0.005 * np.sum(np.sin(3 * np.pi * x_norm) * np.cos(3 * np.pi * x_norm))
        
        # Add a new term to increase complexity and challenge
        coupling_term = 0.3 * np.sum(np.sin(7 * x_norm) * np.cos(9 * x_norm) * np.exp(-0.3 * x_norm**2))
        
        # Combine all terms to create a multimodal landscape
        return exp_decay + trig_coupling + conditioning + cross_poly + noise + spatial_noise + coupling_term