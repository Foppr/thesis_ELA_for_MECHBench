import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Calculate the multimodal function
        # Combines quadratic terms with sinusoidal perturbations
        result = np.sum(x**2) + 0.1 * np.sum(np.sin(5 * x)) + 0.01 * np.sum(x**4)
        
        # Add a small noise term to make it more challenging
        result += 0.001 * np.random.random()
        
        return result