import numpy as np

class MultimodalAttractionLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute attraction points for the landscape
        np.random.seed(42)
        self.attraction_points = np.random.uniform(-5.0, 5.0, (10, dim))
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component with varying widths
        rbf = 0
        for i in range(10):
            point = self.attraction_points[i]
            distance = np.sum((x - point)**2)
            rbf += np.exp(-distance / (2 * 0.5**2)) * np.sin(distance)
        
        # Gradient-based attraction field component
        attraction = 0
        for i in range(10):
            point = self.attraction_points[i]
            distance = np.sum((x - point)**2)
            # Add a repulsive component to create complex topology
            attraction += 1.0 / (1e-8 + distance) * np.cos(distance)
        
        # Add a polynomial term to increase complexity
        poly = 0.01 * np.sum(x**6) + 0.02 * np.sum(x**4) + 0.05 * np.sum(x**2)
        
        # Combine components with a dynamic scaling factor
        scaling = 1.0 + 0.3 * np.sin(0.3 * np.sum(x**2))
        
        return scaling * (rbf + attraction + poly)