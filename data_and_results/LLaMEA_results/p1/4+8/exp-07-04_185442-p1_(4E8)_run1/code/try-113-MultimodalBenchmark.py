import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponential decay terms with varying rates
        exp_decay = np.sum(np.exp(-0.4 * x_norm**2) * np.cos(6 * np.pi * x_norm))
        
        # Trigonometric couplings with varying frequencies
        trig_coupling = np.sum(np.sin(7 * x_norm) * np.cos(9 * x_norm)) + \
                        0.5 * np.sum(np.sin(11 * x_norm) * np.cos(14 * x_norm))
        
        # Adaptive conditioning based on dimensionality
        conditioning = np.sum((x_norm**2) * np.exp(-0.2 * np.abs(x_norm)))
        
        # Non-separable cross-terms with polynomial interactions
        cross_poly = np.sum((x_norm[0] * x_norm[1])**6) + \
                     0.3 * np.sum(x_norm**6 * np.sin(4 * np.pi * x_norm))
        
        # Additional mixed nonlinear coupling terms
        mixed_coupling = 0.25 * np.sum(np.sin(2.5 * x_norm) * np.cos(3.5 * x_norm) * x_norm**4)
        
        # Add a small noise term to create more complex landscape
        noise = 0.02 * np.random.random()
        
        # Combine all terms to create a multimodal landscape
        return exp_decay + trig_coupling + conditioning + cross_poly + mixed_coupling + noise