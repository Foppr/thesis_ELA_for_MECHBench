import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sphere function component
        sphere = np.sum(x**2)
        
        # Multimodal component with shifted local minima
        multimodal = 0
        for i in range(self.dim):
            shifted_x = x[i] - 1.5
            multimodal += (shifted_x**4 - 12 * shifted_x**2 + 3 * shifted_x)
        
        # Enhanced interaction term with higher frequency
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                distance = np.sqrt(x[i]**2 + x[j]**2)
                interaction += 0.2 * x[i] * x[j] * np.sin(3 * distance)
        
        # Add a cosine-based cross-term interaction
        cross_term = 0
        for i in range(self.dim):
            cross_term += np.cos(0.5 * x[i])**3
        
        # Combine components with modified weights
        return 0.1 * sphere + 1.5 * multimodal + 0.3 * interaction + 0.2 * cross_term + 15 * self.dim