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
            multimodal += (x[i]**2 - 10 * np.cos(2 * np.pi * x[i]))
        
        # Combine components with different weights to create challenging landscape
        return sphere + 0.1 * multimodal + 10 * np.sum(np.sin(x)**2)