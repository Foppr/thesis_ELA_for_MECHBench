import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate random rotation matrix with orthogonalization
        self.rotation = np.random.rand(dim, dim)
        self.rotation, _ = np.linalg.qr(self.rotation)
        # Add a second rotation for more complex structure
        self.rotation2 = np.random.rand(dim, dim)
        self.rotation2, _ = np.linalg.qr(self.rotation2)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply double rotation to create a more complex non-separable function
        x_rotated = self.rotation @ x
        x_rotated = self.rotation2 @ x_rotated
        
        # Ellipsoid term with different weights for each dimension
        weights = np.arange(1, self.dim + 1)
        ellipsoid = np.sum(weights * x_rotated**2)
        
        # Add enhanced periodic noise with multiple frequencies
        noise = 0.0
        for i in range(self.dim):
            noise += 0.5 * np.sin(2 * np.pi * x[i] / 1.2) * np.cos(2 * np.pi * x[i] / 0.8) + \
                     0.3 * np.sin(3 * np.pi * x[i] / 1.0) * np.cos(3 * np.pi * x[i] / 0.5) + \
                     0.2 * np.sin(5 * np.pi * x[i] / 1.5) * np.cos(5 * np.pi * x[i] / 0.3)
        
        # Add a small random component for additional challenge
        random_component = 0.05 * np.random.random()
        
        # Add a saddle point component to increase complexity
        saddle = 0.0
        for i in range(0, self.dim, 2):
            if i + 1 < self.dim:
                saddle += 0.1 * (x[i]**2 - x[i+1]**2)
        
        return ellipsoid + noise + random_component + saddle