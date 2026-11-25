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
            freq1 = 8 * (i + 1) / self.dim
            freq2 = 4.0 * (i + 1) / self.dim
            multimodal += np.sin(freq1 * np.pi * x[i]) ** 10 + 0.8 * np.exp(-0.5 * (x[i] / 1.2)**2) * np.cos(freq2 * np.pi * x[i]) ** 8
        
        # Enhanced polynomial interaction terms with higher-order cross-terms
        polynomial = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                polynomial += 0.15 * (x[i] ** 5) * (x[j] ** 7)
        
        # Quaternion-inspired cross-dimensional interactions
        quaternion = 0
        for i in range(0, self.dim, 2):
            if i + 1 < self.dim:
                quaternion += 0.3 * (x[i]**2 + x[i+1]**2) * np.sin(np.pi * (x[i] - x[i+1]))
        
        # Adaptive scaling based on dimensionality
        scale_factor = 1.0 + 0.4 * np.log(self.dim + 1)
        
        # Global shift to increase landscape complexity
        shift = 1.1 * np.sum(np.abs(x))
        
        # Additional chaotic component for increased difficulty
        chaotic = 0
        for i in range(self.dim):
            chaotic += 0.3 * np.sin(12 * np.pi * x[i] + np.cos(6 * np.pi * x[i])) ** 2
        
        # Radial basis function component for enhanced multimodality
        rbf = 0
        centers = np.linspace(-5, 5, min(5, self.dim))
        for i in range(self.dim):
            center = centers[i % len(centers)]
            rbf += 0.25 * np.exp(-0.5 * ((x[i] - center) / 1.5)**2)
        
        # Combined function with improved fitness characteristics
        return sphere + scale_factor * (0.25 * multimodal + 0.08 * polynomial + 0.1 * quaternion) + shift + chaotic + rbf