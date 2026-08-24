import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x**2)
        
        # Add multiple local minima using sinusoidal terms with modified frequencies
        f2 = 0.15 * np.sum(np.sin(6.0 * x) * np.cos(2.0 * x))
        
        # Add a more complex multimodal component with cubic terms
        f3 = 0.08 * np.sum(x**3 * np.sin(4.0 * x))
        
        # Add exponential penalty terms for better conditioning
        f4 = 0.02 * np.sum(np.exp(0.5 * np.abs(x)) - 1.0)
        
        # Add a global minimum at origin with additional penalty terms
        f5 = 0.01 * np.sum(np.abs(x))
        
        return f1 + f2 + f3 + f4 + f5