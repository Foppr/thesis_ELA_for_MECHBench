import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Sum of quadratic terms with different scales
        quadratic = np.sum(x_norm**2)
        
        # Product of sinusoidal terms with higher frequency and amplitude
        sinusoidal = np.prod(np.sin(7 * np.pi * x_norm**2))
        
        # Add a more complex penalty term with radial dependence
        penalty = 0.15 * np.sum(x_norm**4) + 0.05 * np.sum(x_norm**6)
        
        # Add a secondary sinusoidal component to increase multimodality
        secondary_sine = 0.5 * np.sum(np.sin(3 * np.pi * x_norm))
        
        # Combine terms to create a challenging landscape
        return quadratic + 15 * sinusoidal + penalty + secondary_sine