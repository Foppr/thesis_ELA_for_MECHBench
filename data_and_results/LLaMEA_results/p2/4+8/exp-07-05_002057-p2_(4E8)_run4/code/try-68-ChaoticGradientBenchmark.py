import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        self.attractors = np.random.uniform(-5.0, 5.0, (10, dim))
        self.weights = np.random.uniform(0.5, 3.0, 10)
        self.frequency_scale = np.random.uniform(1.0, 10.0, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Attractive potential from multiple chaotic centers
        potential = 0.0
        for i in range(10):
            center = self.attractors[i]
            weight = self.weights[i]
            distance = np.sum((x - center) ** 2)
            potential += weight * np.exp(-distance / (2 * 0.5 ** 2))
        
        # Chaotic gradient component with varying frequencies
        gradient_component = 0.0
        for i in range(self.dim):
            xi = x[i]
            freq = self.frequency_scale[i]
            gradient_component += (np.sin(freq * xi) * np.cos(freq * xi) * 
                                 np.sin(freq * xi + np.pi/4) * 
                                 np.cos(freq * xi + np.pi/3))
        
        # Saddle-point inducing term with cross-dimensional coupling
        saddle_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited cross-dimensionality
                saddle_term += (x[i] ** 2) * (x[j] ** 2) * np.sin(x[i] + x[j])
        
        # Dimensional conditioning with exponential scaling
        conditioning = 0.0
        for i in range(self.dim):
            conditioning += (i + 1) * np.exp(-x[i] ** 2 / (2 * (i + 1) ** 2))
        
        # Combine components with adaptive weights
        result = 0.4 * potential + 0.3 * gradient_component + 0.2 * saddle_term + 0.1 * conditioning
        
        return result