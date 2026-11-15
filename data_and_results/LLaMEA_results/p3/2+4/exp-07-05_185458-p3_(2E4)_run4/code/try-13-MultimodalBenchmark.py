import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial component with exponential decay
        r = np.sqrt(np.sum(x_norm**2))
        radial = np.exp(-r**2) * np.sin(5 * r)
        
        # Multi-modal sinusoidal components with varying frequencies
        sin_terms = np.sum(np.sin(10 * x_norm) * np.cos(7 * x_norm) * np.exp(-0.5 * x_norm**2))
        
        # Polynomial interaction terms with exponential weighting
        poly_interaction = np.sum(np.exp(-0.1 * np.abs(x_norm)) * (x_norm[:-1]**3 + x_norm[1:]**3))
        
        # Frequency-modulated component
        freq_mod = np.sum(np.sin(15 * x_norm * np.exp(-0.2 * r)) * np.cos(8 * x_norm * np.exp(-0.3 * r)))
        
        # Combine all terms with carefully chosen weights
        return 0.3 * radial + 0.4 * sin_terms + 0.2 * poly_interaction + 0.1 * freq_mod