import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x**2)
        
        # Add multiple local minima using sinusoidal terms with modified frequencies and phase shifts
        f2 = 0.2 * np.sum(np.sin(5.0 * x + 1.0) * np.cos(3.0 * x - 0.5))
        
        # Add a more complex multimodal component with cubic terms and additional exponential interactions
        f3 = 0.1 * np.sum(x**3 * np.sin(5.0 * x) * np.exp(-0.1 * np.abs(x)))
        
        # Add exponential penalty terms for better conditioning with modified base
        f4 = 0.03 * np.sum(np.exp(0.6 * np.abs(x)) - 1.0)
        
        # Add a global minimum at origin with additional penalty terms and shifted components
        f5 = 0.015 * np.sum(np.abs(x - 0.5) + np.abs(x + 0.5))
        
        return f1 + f2 + f3 + f4 + f5