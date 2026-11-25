import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sphere function component
        sphere = np.sum(x**2)
        
        # Multimodal component with enhanced chaotic sine modulations and Gaussian decay
        multimodal = 0
        for i in range(self.dim):
            freq1 = 15 * (i + 1) / self.dim
            freq2 = 7.0 * (i + 1) / self.dim
            multimodal += np.sin(freq1 * np.pi * x[i]) ** 15 + 0.8 * np.exp(-0.3 * (x[i] / 1.5)**2) * np.cos(freq2 * np.pi * x[i]) ** 15
        
        # Enhanced polynomial interaction terms with higher-order cross-terms
        polynomial = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                polynomial += 0.3 * (x[i] ** 7) * (x[j] ** 9)
        
        # Quaternion-inspired cross-dimensional interactions with dynamic scaling
        quaternion = 0
        for i in range(0, self.dim, 2):
            if i + 1 < self.dim:
                quaternion += 0.5 * (x[i]**2 + x[i+1]**2) * np.sin(np.pi * (x[i] - x[i+1])) * np.cos(0.5 * np.pi * (x[i] + x[i+1]))
        
        # Adaptive scaling based on dimensionality with exponential growth
        scale_factor = 1.0 + 0.7 * np.log(self.dim + 1) + 0.1 * np.sqrt(self.dim)
        
        # Global shift to increase landscape complexity
        shift = 1.5 * np.sum(np.abs(x)) + 0.2 * np.sum(x**3)
        
        # Additional chaotic component for increased difficulty with dynamic frequency
        chaotic = 0
        for i in range(self.dim):
            chaotic += 0.5 * np.sin(20 * np.pi * x[i] + np.cos(10 * np.pi * x[i])) ** 3
        
        # Dynamic radial basis function component with varying centers and widths
        rbf = 0
        centers = np.linspace(-4.5, 4.5, min(9, self.dim))
        widths = np.linspace(0.8, 1.8, min(9, self.dim))
        for i in range(self.dim):
            center = centers[i % len(centers)]
            width = widths[i % len(widths)]
            rbf += 0.4 * np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Additional cross-dimensional coupling with hyperbolic tangent modulation
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += 0.25 * np.tanh(x[i]) * np.sin(np.pi * x[j]) * (x[i] - x[j])**2
        
        # Combined function with improved fitness characteristics and increased complexity
        return sphere + scale_factor * (0.35 * multimodal + 0.15 * polynomial + 0.2 * quaternion + 0.1 * coupling) + shift + chaotic + rbf