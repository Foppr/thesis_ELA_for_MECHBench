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
        
        # Additional oscillatory component with higher frequency and different weighting
        oscillatory = 0
        for i in range(self.dim):
            oscillatory += np.sin(15 * x[i]) * np.exp(-x[i]**2 / 30)
        
        # Shifted local minima component
        shifted = 0
        for i in range(self.dim):
            shifted += np.sin(x[i] - 1.0) * np.exp(-(x[i] - 1.0)**2 / 50)
        
        # Combine components with different weights
        return sphere + 0.15 * multimodal + 0.1 * oscillatory + 0.05 * shifted