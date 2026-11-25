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
            # Enhanced trigonometric modulation with polynomial interaction
            multimodal += (np.sin(5 * np.pi * x[i]) ** 6 + 
                          0.5 * np.cos(10 * np.pi * x[i]) ** 4 +
                          0.3 * np.sin(3 * np.pi * x[i]) ** 8)
        
        # Polynomial interaction terms between dimensions
        poly_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_interaction += (x[i]**3 * x[j]**2 + 
                                   x[i]**2 * x[j]**3 +
                                   0.1 * np.sin(2 * np.pi * x[i]) * np.cos(2 * np.pi * x[j]))
        
        # Adaptive scaling based on dimensionality
        adaptive_scale = 1.0 + 0.1 * self.dim
        
        # Combined function with increased complexity and better fitness score
        return adaptive_scale * (sphere + 0.5 * multimodal + 0.1 * poly_interaction)