import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sphere function component
        sphere = np.sum(x**2)
        
        # Multimodal component with enhanced oscillations and shifted global minimum
        multimodal = 0
        for i in range(self.dim):
            # Add sine-based oscillation with varying frequencies
            multimodal += (x[i]**2 - 10 * np.cos(2 * np.pi * x[i]) - 
                          5 * np.sin(3 * np.pi * x[i]) + 
                          2 * np.cos(5 * np.pi * x[i]))
        
        # Add a shift to the global minimum to increase difficulty
        shift = 0.5 * np.sum((x - 1.0)**2)
        
        # Combine components with different weights
        return 0.05 * sphere + multimodal + shift + 15 * self.dim