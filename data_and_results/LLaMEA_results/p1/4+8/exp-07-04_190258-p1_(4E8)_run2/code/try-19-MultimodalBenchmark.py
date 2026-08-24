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
            multimodal += np.sin(x[i]) * np.exp(-0.1 * (x[i] - 1)**2)
        
        # Additional quadratic terms to create more complex landscape
        quadratic = 0
        for i in range(self.dim):
            quadratic += 0.1 * (x[i] - 2)**2
        
        return sphere + multimodal + quadratic