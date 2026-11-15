import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Quadratic term for global attraction
        quadratic = np.sum(x_norm**2)
        
        # Enhanced sinusoidal terms with varying frequencies for increased multimodality
        sinusoidal = np.sum(np.sin(7 * np.pi * x_norm) + 0.5 * np.sin(13 * np.pi * x_norm))
        
        # Modified product term with higher frequency cosine components
        product = np.prod(np.cos(2.0 * np.pi * x_norm) * np.cos(0.3 * np.pi * x_norm))
        
        # Additional cross-term interaction to increase dimensionality challenge
        cross_term = 0.1 * np.sum(x_norm[:-1] * x_norm[1:])
        
        # Combine all terms with optimized weights
        return 0.15 * quadratic + 0.4 * sinusoidal + 0.35 * product + 0.1 * cross_term + 1.0