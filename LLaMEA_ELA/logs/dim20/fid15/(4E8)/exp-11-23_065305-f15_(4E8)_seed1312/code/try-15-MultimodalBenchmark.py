import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Quadratic basin term for global minimum at origin
        quadratic = np.sum(x_norm**2)
        
        # Radial multimodal component with multiple local minima
        r = np.sqrt(np.sum(x_norm**2))
        radial_term = 0.5 * np.sin(10 * np.pi * r) * np.exp(-r)
        
        # Additional sinusoidal components in different directions
        directional_terms = 0.3 * np.sum(np.sin(3 * np.pi * x_norm) * np.cos(2 * np.pi * x_norm))
        
        # Add a rugged component using a sum of high-frequency oscillations
        rugged = 0.2 * np.sum(np.sin(15 * x_norm) * np.cos(12 * x_norm))
        
        # Combine all terms
        result = quadratic + radial_term + directional_terms + rugged
        
        return result