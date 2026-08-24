import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Quadratic base with varying coefficients
        quadratic = np.sum((x_norm ** 2) * (1 + 0.3 * np.sin(3 * np.pi * x_norm)))
        
        # High-frequency sinusoidal components with varying amplitudes
        sinusoidal = (np.sum(np.sin(7 * np.pi * x_norm) ** 2) + 
                     0.6 * np.sum(np.sin(11 * np.pi * x_norm) ** 2) + 
                     0.4 * np.sum(np.sin(15 * np.pi * x_norm) ** 2))
        
        # Cross-terms with polynomial interactions
        cross_terms = 0.6 * np.sum((x_norm ** 3) * np.sin(5 * np.pi * x_norm)) + \
                     0.3 * np.sum(x_norm * np.cos(7 * np.pi * x_norm))
        
        # Add a complex interaction term between dimensions
        interaction = 0.5 * np.sum(np.sin(4 * np.pi * x_norm) * np.cos(6 * np.pi * x_norm) * 
                                  np.sin(8 * np.pi * x_norm))
        
        # Add a global distortion term
        distortion = 0.15 * np.sum(np.abs(x_norm) ** 1.7)
        
        # Add a small random noise component
        noise = 0.015 * np.random.random()
        
        # Combine all terms to create a highly complex landscape
        return quadratic + sinusoidal + cross_terms + interaction + distortion + noise