import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrix for added complexity
        self.rotation = np.random.rand(dim, dim) - 0.5
        self.rotation = np.dot(self.rotation, self.rotation.T)
        # Add conditioning parameters for variable difficulty
        self.conditioning = np.random.uniform(0.1, 10.0, dim)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation and conditioning
        x_rot = np.dot(self.rotation, x) * self.conditioning
        
        # Compute the multimodal function with enhanced complexity
        result = 0.0
        for i in range(self.dim):
            # Quadratic term with conditioning
            result += 0.5 * (x_rot[i] ** 2) * (i + 1)
            # Multiple periodic terms to create chaotic minima
            result += 3 * np.sin(x_rot[i] * (i + 1) * np.pi / 3) + \
                      2 * np.cos(x_rot[i] * (i + 1) * np.pi / 2) + \
                      1.5 * np.sin(x_rot[i] * (i + 1) * np.pi)
            # Sharp ridge terms to create saddle points
            result += 1.2 * np.abs(x_rot[i]) * np.sin(x_rot[i] * (i + 1) * np.pi / 4)
            # Additional chaotic component
            result += 0.8 * np.sin(x_rot[i] ** 3 * (i + 1))
        
        # Add global minimum with enhanced penalty
        result += 0.005 * np.sum(x ** 6)
        
        # Add a small noise term to increase landscape complexity
        result += 0.01 * np.random.rand()
        
        return result