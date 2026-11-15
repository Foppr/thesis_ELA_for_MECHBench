import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Quadratic base with varying coefficients
        quadratic = np.sum((x_norm ** 2) * (1 + 0.5 * np.sin(2 * np.pi * x_norm)))
        
        # High-frequency sinusoidal components with varying amplitudes
        sinusoidal = (np.sum(np.sin(5 * np.pi * x_norm) ** 2) + 
                     0.7 * np.sum(np.sin(9 * np.pi * x_norm) ** 2) + 
                     0.3 * np.sum(np.sin(13 * np.pi * x_norm) ** 2))
        
        # Cross-terms with polynomial interactions
        cross_terms = 0.5 * np.sum((x_norm ** 3) * np.sin(4 * np.pi * x_norm)) + \
                     0.2 * np.sum(x_norm * np.cos(6 * np.pi * x_norm))
        
        # Add a complex interaction term between dimensions
        interaction = 0.4 * np.sum(np.sin(3 * np.pi * x_norm) * np.cos(5 * np.pi * x_norm) * 
                                  np.sin(7 * np.pi * x_norm))
        
        # Add a global distortion term
        distortion = 0.1 * np.sum(np.abs(x_norm) ** 1.5)
        
        # Add a small random noise component
        noise = 0.02 * np.random.random()
        
        # Combine all terms to create a highly complex landscape
        return quadratic + sinusoidal + cross_terms + interaction + distortion + noise