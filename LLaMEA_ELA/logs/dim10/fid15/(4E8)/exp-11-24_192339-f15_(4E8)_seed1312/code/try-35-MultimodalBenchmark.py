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
            # Enhanced trigonometric modulation with shifted arguments
            multimodal += (np.sin(5 * np.pi * (x[i] + 0.5)) ** 6 + 
                          0.5 * np.cos(10 * np.pi * (x[i] - 0.3)) ** 4)
            
        # Cross-dimensional interaction term
        cross_interaction = 0
        for i in range(self.dim - 1):
            cross_interaction += (x[i] ** 2) * np.sin(3 * np.pi * x[i+1]) ** 2
            
        # Exponential decay term to create flat regions
        exp_decay = np.sum(np.exp(-0.15 * np.abs(x)) * np.sin(2 * np.pi * x) ** 2)
        
        # Combined function with increased complexity
        return sphere + 0.6 * multimodal + 0.15 * cross_interaction + 0.1 * exp_decay