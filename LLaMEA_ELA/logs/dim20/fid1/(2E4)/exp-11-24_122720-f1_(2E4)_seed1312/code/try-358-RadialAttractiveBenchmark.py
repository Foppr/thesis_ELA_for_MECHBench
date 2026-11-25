import numpy as np

class RadialAttractiveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize radial basis function centers and widths
        self.rbf_centers = np.random.uniform(-4.0, 4.0, (10, dim))
        self.rbf_widths = np.random.uniform(0.5, 2.0, 10)
        # Initialize global minima positions
        self.minima = np.random.uniform(-4.0, 4.0, (5, dim))
        # Initialize noise parameters
        self.noise_level = np.random.uniform(0.1, 0.5)
        self.noise_decay = np.random.uniform(0.8, 1.0)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component
        rbf_sum = 0.0
        for i in range(10):
            center = self.rbf_centers[i]
            width = self.rbf_widths[i]
            distance = np.linalg.norm(x - center)
            rbf_sum += np.exp(-0.5 * (distance / width)**2)
        
        # Attractive force toward global minima
        attraction = 0.0
        for i in range(5):
            min_pos = self.minima[i]
            distance = np.linalg.norm(x - min_pos)
            # Strong attraction near minima, weaker further away
            attraction += 1.0 / (1.0 + distance**2)
        
        # Add adaptive noise that decreases with dimensionality
        noise = self.noise_level * self.noise_decay**(self.dim)
        noise_term = np.random.normal(0, noise)
        
        # Combine components
        result = rbf_sum + attraction + noise_term
        
        return result