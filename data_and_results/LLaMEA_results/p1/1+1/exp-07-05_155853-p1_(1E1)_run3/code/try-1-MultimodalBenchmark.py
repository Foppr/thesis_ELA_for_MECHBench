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
            multimodal += np.sin(x[i]) * np.exp(-(x[i]**2)/10.0)
        
        # Additional quadratic terms to create a more complex landscape
        quadratic = 0.1 * np.sum((x - 1.0)**2)
        
        # Combine components to create a challenging optimization landscape
        return sphere + multimodal + quadratic