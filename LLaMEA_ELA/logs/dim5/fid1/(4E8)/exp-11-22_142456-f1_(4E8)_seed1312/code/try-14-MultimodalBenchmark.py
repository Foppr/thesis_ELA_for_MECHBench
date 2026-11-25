import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sphere function component
        sphere = np.sum(x**2)
        
        # Multimodal component with multiple local minima
        multimodal = 0
        for i in range(self.dim):
            multimodal += (x[i]**2 - 1)**2 + (x[i]**4 - 1)**2
        
        # Additional coupled oscillatory component
        oscillatory = np.sum(np.sin(3 * x) * np.cos(2 * x) * np.exp(-0.05 * x**2))
        
        # Cross-term coupling to increase complexity
        cross_term = np.sum(x[:-1] * x[1:] * np.sin(0.5 * x[:-1] + 0.3 * x[1:]))
        
        return sphere + 0.2 * multimodal + 0.02 * oscillatory + 0.01 * cross_term