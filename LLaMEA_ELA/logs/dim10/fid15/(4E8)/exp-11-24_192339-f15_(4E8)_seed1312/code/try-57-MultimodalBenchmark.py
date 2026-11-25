import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sphere function component
        sphere = np.sum(x**2)
        
        # Multimodal component with sine modulations and Gaussian decay
        multimodal = 0
        for i in range(self.dim):
            freq1 = 4 * (i + 1) / self.dim
            freq2 = 2.0 * (i + 1) / self.dim
            multimodal += np.sin(freq1 * np.pi * x[i]) ** 6 + 0.5 * np.exp(-0.4 * (x[i] / 1.2)**2) * np.cos(freq2 * np.pi * x[i]) ** 4
        
        # Enhanced polynomial interaction terms with higher-order cross-terms
        polynomial = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                polynomial += 0.08 * (x[i] ** 3) * (x[j] ** 5)
        
        # Adaptive scaling based on dimensionality
        scale_factor = 1.0 + 0.3 * np.log(self.dim + 1)
        
        # Global shift to increase landscape complexity
        shift = 0.7 * np.sum(np.abs(x))
        
        # Combined function with improved fitness characteristics
        return sphere + scale_factor * (0.15 * multimodal + 0.04 * polynomial) + shift