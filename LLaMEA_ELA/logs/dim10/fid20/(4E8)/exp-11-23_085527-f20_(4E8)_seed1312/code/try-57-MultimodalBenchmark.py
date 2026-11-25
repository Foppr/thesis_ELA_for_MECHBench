import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced polynomial shaping with higher degree terms
        poly_term = np.sum(0.8 * x_norm**6 + 0.4 * x_norm**5 + 0.2 * x_norm**4)
        
        # Increased frequency periodic components with sinusoidal and cosine products
        periodic_term = 15 * np.sum(np.sin(7 * np.pi * x_norm) * np.cos(4 * np.pi * x_norm))
        
        # Adaptive conditioning with exponential weighting for positive/negative values
        asym_term = np.sum(np.where(x_norm >= 0, 3 * np.exp(0.5 * x_norm), 0.3 * np.exp(-0.5 * x_norm)))
        
        # Enhanced cross-terms with logarithmic interaction to increase non-separability
        cross_term = 0.7 * np.sum(np.log(1 + np.abs(x_norm[:-1] * x_norm[1:])) - 1)
        
        # Global minimum at origin with additional scaling and sinusoidal penalty
        return 0.2 * poly_term + periodic_term + asym_term + cross_term