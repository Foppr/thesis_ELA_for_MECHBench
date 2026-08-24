import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Exponential decay terms with varying rates
        exp_decay = np.sum(np.exp(-x_norm**2) * np.sin(2 * np.pi * x_norm)**2)
        
        # Trigonometric couplings with multiple frequencies
        trig_coupling = np.sum(np.cos(3 * np.pi * x_norm) * np.sin(7 * np.pi * x_norm)) + \
                        0.5 * np.sum(np.sin(5 * np.pi * x_norm) * np.cos(9 * np.pi * x_norm))
        
        # Non-separable polynomial terms with cross-features
        poly_cross = np.sum((x_norm**2 + x_norm**3 + x_norm**4) * np.sin(4 * np.pi * x_norm))
        
        # Adaptive conditioning based on dimensionality
        condition_factor = np.sum((x_norm**2 + 0.1) * np.exp(-x_norm**2))
        
        # Add a complex interaction term to increase landscape ruggedness
        interaction = np.sum(np.sin(np.pi * x_norm) * np.cos(2 * np.pi * x_norm) * np.sin(3 * np.pi * x_norm))
        
        # Combine all terms to form the final landscape
        return exp_decay + trig_coupling + poly_cross + condition_factor + interaction