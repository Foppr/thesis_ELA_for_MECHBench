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
        sinusoidal = np.sum(np.sin(6 * np.pi * x_norm) ** 2) + 0.8 * np.sum(np.sin(10 * np.pi * x_norm) ** 2)
        
        # Increased cross-terms with higher frequency interactions
        cross_terms = 0.6 * np.sum(np.sin(4 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm)) + \
                      0.4 * np.sum(x_norm**3 * np.sin(5 * np.pi * x_norm))
        
        # Add adaptive conditioning to increase condition number with modified scaling
        condition_factor = np.sum((x_norm ** 3) * np.sin(3 * np.pi * x_norm))
        
        # Add a small noise term to create more complex landscape
        noise = 0.02 * np.random.random()
        
        # Combine terms to create multimodal landscape
        return quadratic + sinusoidal + cross_terms + condition_factor + noise