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
            freq1 = 17 * (i + 1) / self.dim
            freq2 = 8.0 * (i + 1) / self.dim
            multimodal += np.sin(freq1 * np.pi * x[i]) ** 17 + 0.9 * np.exp(-0.35 * (x[i] / 1.6)**2) * np.cos(freq2 * np.pi * x[i]) ** 17
        
        # Enhanced polynomial interaction terms with higher-order cross-terms
        polynomial = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                polynomial += 0.4 * (x[i] ** 8) * (x[j] ** 10)
        
        # Quaternion-inspired cross-dimensional interactions with dynamic scaling
        quaternion = 0
        for i in range(0, self.dim, 2):
            if i + 1 < self.dim:
                quaternion += 0.6 * (x[i]**2 + x[i+1]**2) * np.sin(np.pi * (x[i] - x[i+1])) * np.cos(0.6 * np.pi * (x[i] + x[i+1]))
        
        # Adaptive scaling based on dimensionality with exponential growth
        scale_factor = 1.0 + 0.8 * np.log(self.dim + 1) + 0.12 * np.sqrt(self.dim)
        
        # Global shift to increase landscape complexity
        shift = 1.7 * np.sum(np.abs(x)) + 0.25 * np.sum(x**3)
        
        # Additional chaotic component for increased difficulty with dynamic frequency
        chaotic = 0
        for i in range(self.dim):
            chaotic += 0.6 * np.sin(22 * np.pi * x[i] + np.cos(11 * np.pi * x[i])) ** 4
        
        # Dynamic radial basis function component with varying centers and widths
        rbf = 0
        centers = np.linspace(-4.0, 4.0, min(8, self.dim))
        widths = np.linspace(0.9, 1.9, min(8, self.dim))
        for i in range(self.dim):
            center = centers[i % len(centers)]
            width = widths[i % len(widths)]
            rbf += 0.5 * np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Additional cross-dimensional coupling with hyperbolic tangent modulation
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += 0.3 * np.tanh(x[i]) * np.sin(np.pi * x[j]) * (x[i] - x[j])**2
        
        # Combined function with improved fitness characteristics and increased complexity
        return sphere + scale_factor * (0.4 * multimodal + 0.18 * polynomial + 0.22 * quaternion + 0.12 * coupling) + shift + chaotic + rbf