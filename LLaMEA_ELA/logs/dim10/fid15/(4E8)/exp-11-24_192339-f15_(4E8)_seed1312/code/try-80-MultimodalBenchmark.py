import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sphere function component
        sphere = np.sum(x**2)
        
        # Multimodal component with chaotic sine modulations and Gaussian decay
        multimodal = 0
        for i in range(self.dim):
            freq1 = 3.0 * (i + 1) / self.dim
            freq2 = 1.5 * (i + 1) / self.dim
            multimodal += np.sin(freq1 * np.pi * x[i]) ** 5 + 0.3 * np.exp(-0.5 * (x[i] / 1.5)**2) * np.cos(freq2 * np.pi * x[i]) ** 3
        
        # Enhanced polynomial interaction terms with higher-order cross-terms
        polynomial = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                polynomial += 0.1 * (x[i] ** 2) * (x[j] ** 4) + 0.05 * (x[i] ** 4) * (x[j] ** 2)
        
        # Dynamic scaling based on dimensionality
        scale_factor = 1.0 + 0.4 * np.log(self.dim + 1)
        
        # Global shift to increase landscape complexity
        shift = 0.8 * np.sum(np.abs(x))
        
        # Add chaotic component for increased difficulty
        chaotic = 0.2 * np.sum(np.sin(2.0 * np.pi * x) ** 2)
        
        # Adaptive curvature enhancement
        curvature = 0.1 * np.sum((x**3) * np.sin(0.5 * np.pi * x))
        
        # Cross-dimensional interaction enhancement
        cross_interaction = 0.05 * np.sum(np.abs(x[:-1] - x[1:]))
        
        # Combined function with improved fitness characteristics
        return sphere + scale_factor * (0.2 * multimodal + 0.05 * polynomial) + shift + chaotic + curvature + cross_interaction