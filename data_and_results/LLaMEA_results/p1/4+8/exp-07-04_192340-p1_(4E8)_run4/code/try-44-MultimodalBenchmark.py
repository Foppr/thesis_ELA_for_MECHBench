import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrix for added complexity
        self.rotation = np.random.rand(dim, dim) - 0.5
        self.rotation = np.dot(self.rotation, self.rotation.T)
        # Add chaotic parameters
        self.chaotic_params = np.random.rand(dim) * 2 + 1
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation
        x_rot = np.dot(self.rotation, x)
        
        # Compute the multimodal function with chaotic and exponential components
        result = 0.0
        for i in range(self.dim):
            # Quadratic term with scaling
            result += (x_rot[i] ** 2) * (i + 1)
            # Chaotic exponential decay term
            result += 5 * np.exp(-self.chaotic_params[i] * np.abs(x_rot[i])) * np.sin(x_rot[i] * np.pi)
            # Saddle point component
            result += 2 * np.sin(x_rot[i] * 0.5 * np.pi) * np.cos(x_rot[i] * 0.3 * np.pi)
            # Additional interaction term between dimensions
            if i > 0:
                result += 0.3 * np.sin(x_rot[i] * x_rot[i-1] * (i + 1)) * np.exp(-0.1 * (x_rot[i] - x_rot[i-1])**2)
            # Exponential decay with periodic modulation
            result += 4 * np.exp(-0.5 * x_rot[i]**2) * np.cos(x_rot[i] * np.pi * 2)
        
        # Add a global minimum at the origin with a small penalty term
        result += 0.005 * np.sum(x ** 6)
        
        return result