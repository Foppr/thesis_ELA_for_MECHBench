import numpy as np

class AdaptiveMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute components for stability
        np.random.seed(42)
        self.spherical_centers = np.random.uniform(-5.0, 5.0, (10, dim))
        self.elliptic_weights = np.random.uniform(0.1, 10.0, 10)
        self.saddle_centers = np.random.uniform(-5.0, 5.0, (5, dim))
        self.noise_level = 0.01 * (1 + dim / 10.0)
        self.interaction_matrix = np.random.uniform(-0.5, 0.5, (dim, dim))
    
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Spherical component
        spherical = 0.0
        for i in range(10):
            center = self.spherical_centers[i]
            distance = np.sum((x - center) ** 2)
            spherical += np.exp(-distance / (2 * 0.5 ** 2))
        
        # Elliptic component with varying conditioning
        elliptic = 0.0
        for i in range(10):
            center = self.elliptic_weights[i] * (x - self.spherical_centers[i])
            distance = np.sum(center ** 2)
            elliptic += np.exp(-distance / (2 * 0.3 ** 2))
        
        # Saddle-shaped component
        saddle = 0.0
        for i in range(5):
            center = self.saddle_centers[i]
            dx = x - center
            # Saddle function: sum of squares minus sum of products
            saddle += np.sum(dx ** 2) - np.sum(dx * np.roll(dx, 1))
        
        # Dynamic interaction terms
        interaction = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    interaction += self.interaction_matrix[i, j] * x[i] * x[j]
        
        # Adaptive noise injection
        noise = np.random.normal(0, self.noise_level, self.dim)
        noise_term = np.sum(noise ** 2)
        
        # Combine all components
        result = 0.4 * spherical + 0.3 * elliptic + 0.2 * saddle + 0.05 * interaction + 0.05 * noise_term
        
        return result