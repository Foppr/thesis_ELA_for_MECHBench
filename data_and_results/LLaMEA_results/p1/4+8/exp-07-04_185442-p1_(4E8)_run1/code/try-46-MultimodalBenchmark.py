import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Sum of quadratic terms with different scales
        quadratic = np.sum(x_norm**2)
        
        # Enhanced sinusoidal terms with higher frequencies and interactions
        sinusoidal = np.sum(np.sin(5 * np.pi * x_norm) ** 2) + 0.7 * np.sum(np.sin(9 * np.pi * x_norm) ** 2)
        
        # Increased cross-terms with higher frequency interactions
        cross_terms = 0.5 * np.sum(np.sin(3 * np.pi * x_norm) * np.cos(6 * np.pi * x_norm)) + \
                      0.3 * np.sum(x_norm**3 * np.sin(4 * np.pi * x_norm))
        
        # Add adaptive conditioning to increase condition number
        condition_factor = np.sum((x_norm ** 4) * np.sin(2 * np.pi * x_norm))
        
        # Add a small noise term to create more complex landscape
        noise = 0.03 * np.random.random()
        
        # Combine terms to create multimodal landscape
        return quadratic + sinusoidal + cross_terms + condition_factor + noise