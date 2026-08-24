import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Sphere function component
        sphere = np.sum(x**2)
        
        # Multimodal component with multiple local minima
        multimodal = 0
        for i in range(self.dim):
            multimodal += np.sin(5 * x[i]) * np.exp(-0.1 * (x[i] - 1)**2) + \
                         0.5 * np.sin(3 * x[i]) * np.exp(-0.05 * (x[i] + 2)**2)
        
        # Additional interaction terms with higher complexity
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += 0.1 * np.sin(2 * (x[i] + x[j])) * np.cos(0.5 * (x[i] - x[j]))
        
        # Polynomial interaction terms
        poly_interaction = 0
        for i in range(self.dim):
            poly_interaction += 0.05 * (x[i]**4 - 2*x[i]**2)
        
        # Combine components
        result = sphere + 3 * multimodal + 0.3 * interaction + 0.2 * poly_interaction
        
        # Add a small noise term to make it more challenging
        result += 0.005 * np.random.random()
        
        return result