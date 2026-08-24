import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate random rotation matrix for the ellipsoid
        self.rotation = np.random.rand(dim, dim)
        self.rotation, _ = np.linalg.qr(self.rotation)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation to create a non-separable function
        x_rotated = self.rotation @ x
        
        # Ellipsoid term with different weights for each dimension
        weights = np.arange(1, self.dim + 1)
        ellipsoid = np.sum(weights * x_rotated**2)
        
        # Add periodic noise to create local minima
        noise = 0.0
        for i in range(self.dim):
            noise += 0.3 * np.sin(2 * np.pi * x[i] / 1.5) * np.cos(2 * np.pi * x[i] / 0.7)
        
        # Add a small random component for additional challenge
        random_component = 0.05 * np.random.random()
        
        return ellipsoid + noise + random_component