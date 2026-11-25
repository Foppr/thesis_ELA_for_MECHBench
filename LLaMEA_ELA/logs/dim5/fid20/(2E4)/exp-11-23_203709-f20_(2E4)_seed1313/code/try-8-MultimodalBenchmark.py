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
            multimodal += (x[i]**4 - 10 * x[i]**2 + 5 * x[i])
        
        # Add a more complex interaction term between dimensions
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += 0.1 * x[i] * x[j] * np.sin(np.sqrt(x[i]**2 + x[j]**2))
        
        # Combine components with different weights
        return 0.05 * sphere + multimodal + 0.5 * interaction + 10 * self.dim