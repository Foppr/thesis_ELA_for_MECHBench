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
            freq1 = 10 * (i + 1) / self.dim
            freq2 = 5.0 * (i + 1) / self.dim
            multimodal += np.sin(freq1 * np.pi * x[i]) ** 12 + 0.9 * np.exp(-0.5 * (x[i] / 1.1)**2) * np.cos(freq2 * np.pi * x[i]) ** 10
        
        # Enhanced polynomial interaction terms with higher-order cross-terms
        polynomial = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                polynomial += 0.2 * (x[i] ** 6) * (x[j] ** 8)
        
        # Quaternion-inspired cross-dimensional interactions
        quaternion = 0
        for i in range(0, self.dim, 2):
            if i + 1 < self.dim:
                quaternion += 0.4 * (x[i]**2 + x[i+1]**2) * np.sin(np.pi * (x[i] - x[i+1]))
        
        # Adaptive scaling based on dimensionality
        scale_factor = 1.0 + 0.5 * np.log(self.dim + 1)
        
        # Global shift to increase landscape complexity
        shift = 1.2 * np.sum(np.abs(x))
        
        # Additional chaotic component for increased difficulty
        chaotic = 0
        for i in range(self.dim):
            chaotic += 0.4 * np.sin(15 * np.pi * x[i] + np.cos(7 * np.pi * x[i])) ** 2
        
        # Radial basis function component for enhanced multimodality
        rbf = 0
        centers = np.linspace(-5, 5, min(6, self.dim))
        for i in range(self.dim):
            center = centers[i % len(centers)]
            rbf += 0.3 * np.exp(-0.5 * ((x[i] - center) / 1.4)**2)
        
        # Combined function with improved fitness characteristics
        return sphere + scale_factor * (0.3 * multimodal + 0.1 * polynomial + 0.15 * quaternion) + shift + chaotic + rbf