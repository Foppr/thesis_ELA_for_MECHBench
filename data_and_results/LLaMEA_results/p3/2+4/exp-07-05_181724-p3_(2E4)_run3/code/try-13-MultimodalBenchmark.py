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
        
        # Multiple sinusoidal components with different frequencies and amplitudes
        sin1 = np.sum(np.sin(2 * np.pi * x_norm)**2)
        sin2 = np.sum(np.sin(5 * np.pi * x_norm)**2)
        sin3 = np.sum(np.sin(10 * np.pi * x_norm)**2)
        
        # Polynomial terms with mixed degrees
        poly2 = np.sum(x_norm**4)
        poly3 = np.sum(0.3 * x_norm**3)
        poly4 = np.sum(0.1 * x_norm**2)
        
        # Interaction terms between dimensions
        interaction = np.sum(x_norm[:-1] * x_norm[1:])
        
        # Cross-terms to increase complexity
        cross_term = np.sum((x_norm**2) * np.sin(3 * np.pi * x_norm))
        
        # Add a small random noise for non-triviality
        noise = 0.01 * np.random.random()
        
        # Combine all terms with carefully chosen weights
        return 0.5 * quadratic + 0.3 * sin1 + 0.2 * sin2 + 0.1 * sin3 + 0.2 * poly2 + 0.1 * poly3 + 0.05 * poly4 + 0.1 * interaction + 0.05 * cross_term + noise