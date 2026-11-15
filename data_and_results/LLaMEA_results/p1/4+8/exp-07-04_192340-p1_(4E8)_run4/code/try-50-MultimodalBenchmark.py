import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrix for added complexity
        self.rotation = np.random.rand(dim, dim) - 0.5
        self.rotation = np.dot(self.rotation, self.rotation.T)
        # Add conditioning factors
        self.conditioning = np.linspace(1, 10, dim)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation and conditioning
        x_rot = np.dot(self.rotation, x) * self.conditioning
        
        # Compute the multimodal function with enhanced periodic and ridge components
        result = 0.0
        for i in range(self.dim):
            # Quadratic term with conditioning
            result += (x_rot[i] ** 2) * (i + 1) * 0.5
            # Enhanced periodic term with multiple frequencies
            result += 3 * np.sin(x_rot[i] * (i + 1) * np.pi / 2) + 2 * np.sin(x_rot[i] * (i + 1) * np.pi)
            # Additional ridge term with chaotic behavior
            result += 1.5 * np.cos(x_rot[i] * (i + 1) * np.pi) + 0.5 * np.cos(x_rot[i] * (i + 1) * 2 * np.pi)
            # Chaotic component for increased complexity
            result += 0.3 * np.sin(x_rot[i] ** 3 * (i + 1))
        
        # Add a global minimum at the origin with a penalty term
        result += 0.005 * np.sum(x ** 4)
        
        # Add interaction terms between variables for increased complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.1 * np.sin(x_rot[i] * x_rot[j] * (i + j + 1))
        
        return result