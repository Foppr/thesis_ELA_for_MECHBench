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
            multimodal += np.sin(5 * x[i]) * np.exp(-0.05 * (x[i] - 1)**2)
        
        # Additional interaction terms with higher coupling
        interaction = 0
        for i in range(self.dim-1):
            interaction += 0.5 * (x[i]**2 + x[i+1]**2) * np.sin(0.5 * (x[i] - x[i+1]))
        
        # Cross-term interaction
        cross_term = 0
        for i in range(self.dim):
            cross_term += x[i] * np.sin(0.1 * x[i]**2)
        
        # Combine components with different weights
        return 0.5 * sphere + 3 * multimodal + interaction + 0.1 * cross_term