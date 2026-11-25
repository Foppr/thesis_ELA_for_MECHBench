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
            # High-frequency sinusoidal oscillations
            multimodal += np.sin(10 * np.pi * x[i]) ** 8
            # Additional Gaussian peaks for complexity
            multimodal += 0.5 * np.exp(-0.5 * ((x[i] - 2.0) / 0.5)**2)
            multimodal += 0.3 * np.exp(-0.5 * ((x[i] + 3.0) / 0.3)**2)
        
        # Add a more complex interaction term between dimensions
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += 0.1 * np.sin(3 * np.pi * x[i]) * np.cos(2 * np.pi * x[j])
        
        # Combined function with enhanced multimodality
        return sphere + 0.5 * multimodal + 0.2 * interaction