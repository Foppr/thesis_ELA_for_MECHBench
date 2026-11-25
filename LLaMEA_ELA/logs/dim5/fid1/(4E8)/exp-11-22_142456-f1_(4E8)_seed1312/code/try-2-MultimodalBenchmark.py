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
            multimodal += (x[i] - 1)**4 + (x[i] + 1)**4
        
        # Additional oscillatory component
        oscillatory = np.sum(np.sin(5 * x) * np.exp(-0.1 * x**2))
        
        return sphere + 0.1 * multimodal + 0.01 * oscillatory