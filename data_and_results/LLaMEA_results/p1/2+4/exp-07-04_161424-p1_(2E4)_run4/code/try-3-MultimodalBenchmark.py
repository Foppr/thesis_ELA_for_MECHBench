import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Sphere function component
        sphere = np.sum(x**2)
        
        # Multimodal component with multiple local minima
        multimodal = 0
        for i in range(self.dim):
            multimodal += np.sin(x[i]) * np.exp(-(x[i]**2) / 100)
        
        # Additional oscillatory component
        oscillatory = 0
        for i in range(self.dim):
            oscillatory += np.sin(10 * x[i]) * np.exp(-x[i]**2 / 50)
        
        # Combine components with different weights
        return sphere + 0.1 * multimodal + 0.05 * oscillatory