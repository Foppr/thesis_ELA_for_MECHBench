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
            multimodal += np.sin(x[i]) * np.exp(-0.1 * (x[i] - 1)**2)
        
        # Additional interaction terms
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += 0.1 * np.sin(0.5 * (x[i] + x[j])) * np.exp(-0.05 * (x[i] - x[j])**2)
        
        # Combine components
        return sphere + 10 * multimodal + 5 * interaction