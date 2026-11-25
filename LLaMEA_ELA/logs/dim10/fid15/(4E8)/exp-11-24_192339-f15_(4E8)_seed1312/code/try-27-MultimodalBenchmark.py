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
            # Enhanced trigonometric modulation
            multimodal += np.sin(5 * np.pi * x[i]) ** 6 + 0.5 * np.cos(10 * np.pi * x[i]) ** 4
            
        # Exponential decay term to create flat regions
        exp_decay = np.sum(np.exp(-0.1 * np.abs(x)) * np.sin(2 * np.pi * x) ** 2)
        
        # Combined function with increased complexity
        return sphere + 0.5 * multimodal + 0.1 * exp_decay