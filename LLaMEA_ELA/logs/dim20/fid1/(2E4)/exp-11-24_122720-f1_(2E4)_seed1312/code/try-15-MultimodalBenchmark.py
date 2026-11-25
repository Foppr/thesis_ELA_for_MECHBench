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
            multimodal += (x[i]**4 - 10 * x[i]**2 + 5 * x[i] * np.sin(2 * np.pi * x[i]))
        
        # Combined function with different weights to create challenging landscape
        return 0.05 * sphere + multimodal + 15 * self.dim