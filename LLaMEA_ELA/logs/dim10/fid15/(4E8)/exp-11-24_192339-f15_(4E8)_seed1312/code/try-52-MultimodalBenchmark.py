import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sphere function component
        sphere = np.sum(x**2)
        
        # Multimodal component with enhanced cosine modulations and radial basis functions
        multimodal = 0
        for i in range(self.dim):
            freq1 = 6 * (i + 1) / self.dim
            freq2 = 3 * (i + 1) / self.dim
            multimodal += np.cos(freq1 * np.pi * x[i]) ** 8 + 0.5 * np.exp(-0.3 * (x[i] / 1.5)**2) * np.sin(freq2 * np.pi * x[i]) ** 6
        
        # Enhanced polynomial interaction terms with higher-order cross-terms and mixed powers
        polynomial = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                polynomial += 0.03 * (x[i] ** 5) * (x[j] ** 4) + 0.02 * (x[i] ** 3) * (x[j] ** 5)
        
        # Radial basis function component for additional multimodality
        rbf = 0
        centers = np.linspace(-5, 5, min(5, self.dim))
        for i in range(min(5, self.dim)):
            if i < len(centers):
                rbf += np.exp(-0.2 * np.sum((x - centers[i])**2))
        
        # Adaptive scaling based on dimensionality with dynamic factor
        scale_factor = 1.0 + 0.2 * np.log(self.dim + 1) + 0.05 * np.sin(self.dim * 0.5)
        
        # Dynamic global shift to increase landscape complexity
        shift = 0.3 * np.sum(np.abs(x)) + 0.1 * np.sum(x**3)
        
        # Combined function with improved fitness characteristics
        return sphere + scale_factor * (0.2 * multimodal + 0.015 * polynomial + 0.05 * rbf) + shift