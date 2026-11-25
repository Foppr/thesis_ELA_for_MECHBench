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
            # Enhanced trigonometric modulation with varying frequencies
            freq1 = 5 * (i + 1) / self.dim
            freq2 = 3 * (i + 1) / self.dim
            multimodal += np.sin(freq1 * np.pi * x[i]) ** 6 + 0.5 * np.sin(freq2 * np.pi * x[i]) ** 4
        
        # Polynomial interaction terms for increased complexity
        polynomial = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                polynomial += 0.1 * (x[i] ** 3) * (x[j] ** 2)
        
        # Adaptive scaling based on dimensionality
        scale_factor = 1.0 + 0.1 * np.log(self.dim + 1)
        
        # Combined function with improved fitness characteristics
        return sphere + scale_factor * (0.1 * multimodal + 0.01 * polynomial)