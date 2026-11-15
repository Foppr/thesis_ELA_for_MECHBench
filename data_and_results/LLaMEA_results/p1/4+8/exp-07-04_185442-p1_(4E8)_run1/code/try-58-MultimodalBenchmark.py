import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Quadratic base with varying coefficients and adaptive conditioning
        quadratic = np.sum((x_norm ** 2) * (1 + 0.3 * np.sin(3 * np.pi * x_norm)) + 
                          0.2 * (x_norm ** 4) * np.cos(2 * np.pi * x_norm))
        
        # High-frequency sinusoidal components with varying amplitudes and phase shifts
        sinusoidal = (np.sum(np.sin(7 * np.pi * x_norm) ** 2) + 
                     0.6 * np.sum(np.sin(11 * np.pi * x_norm) ** 2) + 
                     0.4 * np.sum(np.sin(15 * np.pi * x_norm) ** 2) + 
                     0.2 * np.sum(np.sin(19 * np.pi * x_norm) ** 2))
        
        # Cross-terms with polynomial interactions and additional coupling
        cross_terms = 0.6 * np.sum((x_norm ** 3) * np.sin(5 * np.pi * x_norm)) + \
                     0.3 * np.sum(x_norm * np.cos(7 * np.pi * x_norm)) + \
                     0.1 * np.sum((x_norm ** 2) * np.sin(9 * np.pi * x_norm) * np.cos(4 * np.pi * x_norm))
        
        # Add a complex interaction term between dimensions with non-separable structure
        interaction = 0.5 * np.sum(np.sin(4 * np.pi * x_norm) * np.cos(6 * np.pi * x_norm) * 
                                  np.sin(8 * np.pi * x_norm) * np.cos(10 * np.pi * x_norm))
        
        # Add a global distortion term with adaptive scaling
        distortion = 0.15 * np.sum(np.abs(x_norm) ** 1.7) + \
                    0.05 * np.sum(np.abs(x_norm) ** 2.3)
        
        # Add a multi-modal noise component
        noise = 0.03 * np.random.random()
        
        # Combine all terms to create a highly complex landscape
        return quadratic + sinusoidal + cross_terms + interaction + distortion + noise