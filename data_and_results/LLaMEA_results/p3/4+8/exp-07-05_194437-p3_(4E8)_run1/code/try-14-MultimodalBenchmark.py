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
            multimodal += np.sin(2 * x[i]) * np.exp(-0.2 * (x[i] - 1.5)**2)
        
        # Additional interaction terms with different coefficients
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += 0.15 * np.sin(0.7 * (x[i] + x[j])) * np.exp(-0.03 * (x[i] - x[j])**2)
        
        # Shifted and scaled sinusoidal terms for increased complexity
        shift_terms = 0
        for i in range(self.dim):
            shift_terms += 0.5 * np.sin(3 * (x[i] - 0.5)) * np.exp(-0.1 * (x[i] + 1)**2)
        
        # Combine components
        return sphere + 12 * multimodal + 6 * interaction + 2 * shift_terms