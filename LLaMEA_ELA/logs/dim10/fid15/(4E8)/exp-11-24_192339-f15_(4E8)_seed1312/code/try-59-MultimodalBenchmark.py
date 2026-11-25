import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sphere function component
        sphere = np.sum(x**2)
        
        # Chaotic multimodal component with sine modulations and Gaussian decay
        multimodal = 0
        for i in range(self.dim):
            freq1 = 3 * (i + 1) / self.dim
            freq2 = 1.5 * (i + 1) / self.dim
            multimodal += np.sin(freq1 * np.pi * x[i]) ** 6 + 0.4 * np.exp(-0.3 * (x[i] / 1.5)**2) * np.cos(freq2 * np.pi * x[i]) ** 4
        
        # Enhanced polynomial interaction terms with higher-order cross-terms
        polynomial = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                polynomial += 0.07 * (x[i] ** 3) * (x[j] ** 4)
        
        # Dynamic cross-dimensional coupling with chaotic interaction
        cross_dim = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_dim += np.sin(np.pi * x[i] * x[j]) * np.exp(-0.1 * (x[i] - x[j])**2)
        
        # Adaptive scaling based on dimensionality with chaotic factor
        scale_factor = 1.0 + 0.2 * np.log(self.dim + 1) + 0.05 * np.sin(self.dim * np.pi / 4)
        
        # Global shift to increase landscape complexity with chaotic component
        shift = 0.6 * np.sum(np.abs(x)) + 0.1 * np.sin(np.sum(x**2))
        
        # Combined function with improved fitness characteristics
        return sphere + scale_factor * (0.12 * multimodal + 0.03 * polynomial + 0.05 * cross_dim) + shift