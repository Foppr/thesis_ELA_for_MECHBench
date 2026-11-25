import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sphere function component
        sphere = np.sum(x**2)
        
        # Multimodal component with enhanced nonlinearity and interactions
        multimodal = 0
        for i in range(self.dim):
            multimodal += (x[i]**4 - 12 * x[i]**2 + 8 * x[i] * np.sin(3 * np.pi * x[i]) + 0.5 * x[i]**3)
        
        # Add interaction terms between dimensions
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += 0.1 * x[i] * x[j] * np.sin(np.pi * (x[i] + x[j]))
        
        # Combined function with different weights to create challenging landscape
        return 0.03 * sphere + multimodal + interaction + 20 * self.dim