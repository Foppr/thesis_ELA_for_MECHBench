import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sphere function component
        sphere = np.sum(x**2)
        
        # Enhanced multimodal component with higher-order terms and varied frequencies
        multimodal = 0
        for i in range(self.dim):
            multimodal += (x[i]**4 - 8 * x[i]**2 + 20 * np.cos(1.5 * np.pi * x[i]) + 5 * np.sin(3 * np.pi * x[i]))
        
        # Combined function with adjusted weights to create a more challenging landscape
        return 0.05 * sphere + multimodal + 15 * self.dim