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
            # Enhanced periodic term with exponential modulation
            result += 7 * np.sin(x_rot[i] * (i + 1) * np.pi / 1.5) * np.exp(-0.1 * abs(x_rot[i]))
            # Additional ridge term for sharp convergence challenges
            result += 3 * np.cos(x_rot[i] * (i + 1) * np.pi * 1.2)
            # Interaction term between dimensions
            if i > 0:
                result += 0.5 * x_rot[i] * x_rot[i-1] * (i + 1)
        
        # Add global cross-term interaction between all dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.3 * x_rot[i] * x_rot[j] * np.sin(np.pi * (i + j) / self.dim)
        
        # Add a global minimum at the origin with a small penalty term
        result += 0.01 * np.sum(x ** 4)
        
        return result