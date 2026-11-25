import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sphere function component
        sphere = np.sum(x**2)
        
        # Multimodal component with enhanced complexity
        multimodal = 0
        for i in range(self.dim):
            # Augmented trigonometric modulation with higher harmonics
            multimodal += (np.sin(7 * np.pi * x[i]) ** 8 + 
                          0.7 * np.cos(12 * np.pi * x[i]) ** 5 +
                          0.3 * np.sin(3 * np.pi * x[i]) ** 4)
            
        # Adaptive polynomial scaling based on dimensionality
        poly_scale = np.sum((x**4 + 0.5 * x**3 + 0.1 * x**2) * (1 + 0.1 * self.dim))
        
        # Hybrid Gaussian basin to create flat regions with sharp transitions
        gaussian_basin = np.sum(np.exp(-0.05 * (x**2)) * np.sin(3 * np.pi * x) ** 3)
        
        # Cross-dimensional interaction terms for increased complexity
        cross_terms = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_terms += 0.1 * np.sin(np.pi * (x[i] + x[j])) ** 2
        
        # Combined function with enhanced multimodality and complexity
        return sphere + 0.7 * multimodal + 0.2 * poly_scale + 0.15 * gaussian_basin + 0.05 * cross_terms