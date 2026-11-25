import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sphere function component
        sphere = np.sum(x**2)
        
        # Multimodal component with modified trigonometric terms and cross-terms
        multimodal = 0
        for i in range(self.dim):
            multimodal += np.sin(7 * np.pi * x[i]) ** 4
        
        # Add interactive cross-terms for increased complexity
        cross_terms = 0
        for i in range(self.dim - 1):
            cross_terms += (x[i] - x[i+1])**2 * np.sin(3 * np.pi * (x[i] + x[i+1]))
        
        # Combined function with adjusted weights
        return sphere + 0.15 * multimodal + 0.05 * cross_terms