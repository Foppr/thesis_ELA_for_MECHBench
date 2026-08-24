import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponential decay terms with varying rates
        exp_decay = np.sum(np.exp(-0.5 * (x_norm ** 2)) * (1 + 0.3 * np.cos(3 * np.pi * x_norm)))
        
        # Trigonometric coupling terms with varying frequencies and amplitudes
        trig_coupling = (0.8 * np.sum(np.sin(2 * np.pi * x_norm) * np.cos(4 * np.pi * x_norm)) +
                        0.5 * np.sum(np.sin(6 * np.pi * x_norm) * np.cos(8 * np.pi * x_norm)) +
                        0.3 * np.sum(np.sin(10 * np.pi * x_norm) * np.cos(12 * np.pi * x_norm)))
        
        # Non-separable polynomial cross-terms
        poly_cross = 0.4 * np.sum((x_norm ** 2) * np.sin(5 * np.pi * x_norm)) + \
                    0.2 * np.sum(x_norm ** 3 * np.cos(7 * np.pi * x_norm))
        
        # Adaptive conditioning based on dimensionality
        conditioning = 0.1 * np.sum(np.abs(x_norm) ** (1.2 + 0.1 * self.dim))
        
        # Complex interaction between dimensions
        interaction = 0.3 * np.sum(np.sin(3 * np.pi * x_norm) * np.cos(5 * np.pi * x_norm) * 
                                  np.sin(7 * np.pi * x_norm) * np.cos(9 * np.pi * x_norm))
        
        # Global distortion with adjustable strength
        distortion = 0.05 * np.sum(np.abs(x_norm) ** 1.8)
        
        # Add small random noise for additional challenge
        noise = 0.01 * np.random.random()
        
        # Combine all components to form the final landscape
        return exp_decay + trig_coupling + poly_cross + conditioning + interaction + distortion + noise