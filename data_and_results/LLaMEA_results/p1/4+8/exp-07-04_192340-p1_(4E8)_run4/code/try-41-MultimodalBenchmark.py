import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrix for added complexity
        self.rotation = np.random.rand(dim, dim) - 0.5
        self.rotation = np.dot(self.rotation, self.rotation.T)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation
        x_rot = np.dot(self.rotation, x)
        
        # Compute the multimodal function with periodic and ridge components
        result = 0.0
        for i in range(self.dim):
            # Quadratic term with scaling
            result += (x_rot[i] ** 2) * (i + 1)
            # Periodic term to create multiple local minima
            result += 5 * np.sin(x_rot[i] * (i + 1) * np.pi / 2)
            # Additional ridge term for sharp convergence challenges
            result += 2 * np.cos(x_rot[i] * (i + 1) * np.pi)
        
        # Add a global minimum at the origin with a small penalty term
        result += 0.01 * np.sum(x ** 4)
        
        return result