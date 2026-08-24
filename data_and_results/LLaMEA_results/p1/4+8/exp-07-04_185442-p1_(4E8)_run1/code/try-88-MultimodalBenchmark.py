import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponential decay terms with varying rates
        exp_decay = np.sum(np.exp(-0.3 * x_norm**2) * np.cos(3 * np.pi * x_norm))
        
        # Trigonometric couplings with varying frequencies
        trig_coupling = np.sum(np.sin(4 * x_norm) * np.cos(6 * x_norm)) + \
                        0.6 * np.sum(np.sin(8 * x_norm) * np.cos(10 * x_norm))
        
        # Adaptive conditioning based on dimensionality
        conditioning = np.sum((x_norm**2) * np.exp(-0.15 * np.abs(x_norm)))
        
        # Non-separable cross-terms with polynomial interactions
        cross_poly = np.sum((x_norm[0] * x_norm[1])**3) + \
                     0.4 * np.sum(x_norm**5 * np.sin(3 * np.pi * x_norm))
        
        # Add a small noise term to create more complex landscape
        noise = 0.015 * np.random.random()
        
        # Combine all terms to create a multimodal landscape
        return exp_decay + trig_coupling + conditioning + cross_poly + noise