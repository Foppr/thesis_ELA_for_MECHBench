import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponential decay terms with varying rates
        exp_decay = np.sum(np.exp(-0.3 * x_norm**2) * np.cos(5 * np.pi * x_norm))
        
        # Trigonometric couplings with varying frequencies
        trig_coupling = np.sum(np.sin(6 * x_norm) * np.cos(8 * x_norm)) + \
                        0.6 * np.sum(np.sin(10 * x_norm) * np.cos(13 * x_norm))
        
        # Adaptive conditioning based on dimensionality
        conditioning = np.sum((x_norm**2) * np.exp(-0.15 * np.abs(x_norm)))
        
        # Non-separable cross-terms with polynomial interactions
        cross_poly = np.sum((x_norm[0] * x_norm[1])**5) + \
                     0.4 * np.sum(x_norm**5 * np.sin(3 * np.pi * x_norm))
        
        # Additional mixed nonlinear coupling terms
        mixed_coupling = 0.3 * np.sum(np.sin(2 * x_norm) * np.cos(3 * x_norm) * x_norm**3)
        
        # Add a small noise term to create more complex landscape
        noise = 0.015 * np.random.random()
        
        # Combine all terms to create a multimodal landscape
        return exp_decay + trig_coupling + conditioning + cross_poly + mixed_coupling + noise