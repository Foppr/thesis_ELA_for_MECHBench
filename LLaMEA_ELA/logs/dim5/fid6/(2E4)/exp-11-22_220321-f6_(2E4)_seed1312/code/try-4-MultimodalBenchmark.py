import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Base quadratic term
        base_term = np.sum(x_normalized**2)
        
        # Multiple sinusoidal modulation terms with varying frequencies
        freq1 = 2 * np.pi
        freq2 = 5 * np.pi
        freq3 = 7 * np.pi
        
        sin_term = (np.sum(np.sin(freq1 * x_normalized)**2) + 
                   0.5 * np.sum(np.sin(freq2 * x_normalized)**2) + 
                   0.3 * np.sum(np.sin(freq3 * x_normalized)**2))
        
        # Additional polynomial penalty terms for increased complexity
        poly_term = 0.1 * np.sum(x_normalized**4) + 0.05 * np.sum(x_normalized**6)
        
        # Cross-terms to increase conditioning difficulty
        cross_term = 0.2 * np.sum(x_normalized[:-1] * x_normalized[1:])
        
        return base_term + sin_term + poly_term - cross_term