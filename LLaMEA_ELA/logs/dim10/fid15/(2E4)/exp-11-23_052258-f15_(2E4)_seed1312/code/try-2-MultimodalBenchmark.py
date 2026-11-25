import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Calculate the multimodal function
        # This combines a quadratic term with sinusoidal oscillations
        # to create multiple local minima around the global minimum at origin
        
        # Quadratic term (global minimum at origin)
        quadratic = np.sum(x**2)
        
        # Sinusoidal oscillations to create multiple local minima
        oscillation = 0.1 * np.sum(np.sin(5.0 * x) * np.cos(3.0 * x))
        
        # Additional multimodal component with varying frequencies
        multicomponent = 0.05 * np.sum(np.sin(10.0 * x**2) + np.cos(7.0 * x))
        
        return quadratic + oscillation + multicomponent