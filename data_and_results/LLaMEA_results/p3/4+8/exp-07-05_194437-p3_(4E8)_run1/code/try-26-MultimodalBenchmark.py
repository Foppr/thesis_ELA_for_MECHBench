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
            multimodal += np.sin(2 * x[i]) * np.exp(-0.15 * (x[i] - 1)**2)
        
        # Additional interaction terms with higher frequency
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += 0.15 * np.sin(0.7 * (x[i] + x[j])) * np.exp(-0.03 * (x[i] - x[j])**2)
        
        # Cross-term interaction
        cross_term = 0
        for i in range(self.dim):
            cross_term += 0.05 * x[i]**3 * np.sin(0.3 * x[i])
        
        # Combine components
        return sphere + 12 * multimodal + 6 * interaction + 0.5 * cross_term