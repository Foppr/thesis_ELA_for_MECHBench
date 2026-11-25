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
            # Enhanced trigonometric modulation with polynomial interactions
            multimodal += (np.sin(5 * np.pi * x[i]) ** 6 + 
                          0.5 * np.cos(10 * np.pi * x[i]) ** 4 + 
                          0.3 * np.sin(3 * np.pi * x[i]) ** 8)
        
        # Cross-terms to increase interaction between dimensions
        cross_terms = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_terms += 0.1 * np.sin(np.pi * (x[i] + x[j])) ** 2
        
        # Exponential decay term to create flat regions
        exp_decay = np.sum(np.exp(-0.1 * np.abs(x)) * np.sin(2 * np.pi * x) ** 2)
        
        # Polynomial interaction term for increased complexity
        poly_interaction = np.sum((x**3 + 0.5 * x**2 - 0.3 * x)**2)
        
        # Combined function with increased complexity
        return sphere + 0.5 * multimodal + 0.1 * exp_decay + 0.2 * cross_terms + 0.05 * poly_interaction