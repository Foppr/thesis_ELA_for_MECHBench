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
            freq1 = 4.0 * (i + 1) / self.dim
            freq2 = 2.0 * (i + 1) / self.dim
            multimodal += np.sin(freq1 * np.pi * x[i]) ** 5 + 0.2 * np.exp(-0.3 * (x[i] / 1.2)**2) * np.cos(freq2 * np.pi * x[i]) ** 4
        
        # Enhanced polynomial interaction terms with higher-order cross-terms
        polynomial = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                polynomial += 0.15 * (x[i] ** 2) * (x[j] ** 3) + 0.08 * (x[i] ** 3) * (x[j] ** 2)
        
        # Dynamic scaling based on dimensionality
        scale_factor = 1.0 + 0.5 * np.log(self.dim + 1)
        
        # Global shift to increase landscape complexity
        shift = 0.9 * np.sum(np.abs(x))
        
        # Add chaotic component for increased difficulty
        chaotic = 0.25 * np.sum(np.sin(3.0 * np.pi * x) ** 2)
        
        # Radial basis function component for additional multimodality
        rbf = 0
        for i in range(self.dim):
            rbf += 0.1 * np.exp(-0.4 * (x[i] - 1.0)**2) + 0.05 * np.exp(-0.6 * (x[i] + 1.0)**2)
        
        # Combined function with improved fitness characteristics
        return sphere + scale_factor * (0.25 * multimodal + 0.08 * polynomial) + shift + chaotic + rbf