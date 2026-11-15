import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x**2)
        
        # Add multiple local minima using sinusoidal terms with modified coefficients
        f2 = 0.15 * np.sum(np.sin(6.0 * x) * np.cos(2.0 * x))
        
        # Add a more complex multimodal component with interaction terms
        f3 = 0.08 * np.sum(np.sin(8.0 * x) + np.cos(4.0 * x) + x**3 * np.sin(2.0 * x))
        
        # Combine all components
        return f1 + f2 + f3