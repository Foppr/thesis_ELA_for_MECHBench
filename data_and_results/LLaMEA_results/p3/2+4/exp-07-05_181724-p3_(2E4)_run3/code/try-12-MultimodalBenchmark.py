import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Quadratic base term
        quadratic = np.sum(x_norm**2)
        
        # Sinusoidal terms with varying frequencies and amplitudes
        sinusoidal1 = np.sum(np.sin(3 * np.pi * x_norm)**2)
        sinusoidal2 = np.sum(np.sin(7 * np.pi * x_norm)**2)
        
        # High-frequency component for increased complexity
        high_freq = np.sum(np.sin(15 * np.pi * x_norm)**2)
        
        # Polynomial terms with mixed degrees
        polynomial = np.sum(0.8 * x_norm**4 + 0.3 * x_norm**3 + 0.1 * x_norm**2)
        
        # Interaction terms between dimensions
        interaction = np.sum(x_norm[:-1] * x_norm[1:])
        
        # Cross-terms to create more complex landscape
        cross_terms = np.sum((x_norm**2) * np.sin(2 * np.pi * x_norm))
        
        # Add a small random noise for non-triviality
        noise = 0.01 * np.random.random()
        
        # Combine all components with carefully tuned weights
        return 0.5 * quadratic + 0.3 * sinusoidal1 + 0.2 * sinusoidal2 + 0.1 * high_freq + 0.15 * polynomial + 0.05 * interaction + 0.05 * cross_terms + noise