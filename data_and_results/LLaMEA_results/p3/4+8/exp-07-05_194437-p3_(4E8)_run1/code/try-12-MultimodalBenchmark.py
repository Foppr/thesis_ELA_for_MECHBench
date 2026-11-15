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
            multimodal += np.sin(3 * x[i]) * np.exp(-0.1 * (x[i] - 1)**2)
        
        # Additional interaction terms with higher frequency
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += 0.2 * np.sin(2 * (x[i] + x[j])) * np.exp(-0.03 * (x[i] - x[j])**2)
        
        # Cross-term interaction for increased complexity
        cross_term = 0
        for i in range(self.dim):
            cross_term += np.cos(2 * x[i]) * np.sin(0.5 * x[i]) * np.exp(-0.05 * x[i]**2)
        
        # Combine components with adjusted weights
        return sphere + 15 * multimodal + 8 * interaction + 3 * cross_term