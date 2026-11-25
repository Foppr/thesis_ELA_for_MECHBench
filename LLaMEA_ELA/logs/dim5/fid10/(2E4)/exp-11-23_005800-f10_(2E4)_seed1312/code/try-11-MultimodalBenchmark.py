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
            multimodal += (x[i]**2 - 10 * np.cos(2 * np.pi * x[i]) + 
                          5 * np.sin(3 * np.pi * x[i]))
        
        # Additional high-frequency component to increase landscape complexity
        high_freq = 0
        for i in range(self.dim):
            high_freq += 3 * np.sin(5 * np.pi * x[i]) * np.cos(7 * np.pi * x[i])
        
        # Combine components with different weights
        return 0.05 * sphere + multimodal + 0.1 * high_freq + 10 * self.dim