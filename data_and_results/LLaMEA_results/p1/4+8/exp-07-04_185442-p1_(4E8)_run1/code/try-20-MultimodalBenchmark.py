import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Quadratic base term
        quadratic = np.sum(x_norm**2)
        
        # Enhanced sinusoidal components with varying frequencies and phases
        sin1 = np.sum(np.sin(2 * np.pi * x_norm) ** 2)
        sin2 = np.sum(np.sin(5 * np.pi * x_norm) ** 2)
        sin3 = np.sum(np.sin(8 * np.pi * x_norm) ** 2)
        sin4 = np.sum(np.sin(10 * np.pi * x_norm) ** 2)
        
        # Cross-terms with different interaction patterns
        cross1 = 0.5 * np.sum(np.sin(3 * np.pi * x_norm) * np.cos(6 * np.pi * x_norm))
        cross2 = 0.3 * np.sum(np.sin(4 * np.pi * x_norm) * np.sin(9 * np.pi * x_norm))
        
        # Higher-order polynomial interactions
        poly_interaction = 0.2 * np.sum((x_norm**3) * np.sin(7 * np.pi * x_norm))
        
        # Structured noise with dimension dependency
        noise = 0.1 * np.sum(np.sin(15 * np.pi * x_norm) * np.cos(12 * np.pi * x_norm))
        
        # Combine all terms
        return quadratic + sin1 + sin2 + sin3 + sin4 + cross1 + cross2 + poly_interaction + noise