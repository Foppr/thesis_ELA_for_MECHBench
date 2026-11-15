import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x**2)
        
        # Add multiple local minima using sinusoidal terms
        f2 = 0.1 * np.sum(np.sin(5.0 * x))
        
        # Add a more complex multimodal component
        f3 = 0.05 * np.sum(np.sin(10.0 * x) * np.cos(3.0 * x))
        
        # Add a global minimum at origin with additional penalty terms
        f4 = 0.01 * np.sum(np.abs(x))
        
        return f1 + f2 + f3 + f4