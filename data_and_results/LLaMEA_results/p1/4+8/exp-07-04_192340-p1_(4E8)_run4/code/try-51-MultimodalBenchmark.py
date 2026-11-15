import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrix for added complexity
        self.rotation = np.random.rand(dim, dim) - 0.5
        self.rotation = np.dot(self.rotation, self.rotation.T)
        # Add chaotic scaling factors
        self.scaling = np.random.rand(dim) * 10 + 1
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation and scaling
        x_rot = np.dot(self.rotation, x)
        x_scaled = x_rot * self.scaling
        
        # Compute the multimodal function with enhanced periodic and ridge components
        result = 0.0
        for i in range(self.dim):
            # Quadratic term with scaling and chaotic modification
            result += (x_scaled[i] ** 2) * (i + 1) * np.sin(x_scaled[i] * 0.5)
            # Enhanced periodic term with multiple frequencies
            result += 7 * np.sin(x_scaled[i] * (i + 1) * np.pi / 2) * np.cos(x_scaled[i] * (i + 1) * np.pi / 4)
            # Additional ridge term with chaotic modulation
            result += 3 * np.cos(x_scaled[i] * (i + 1) * np.pi) * np.sin(x_scaled[i] * 0.3)
            # Chaotic local minimum term
            result += 1.5 * np.sin(x_scaled[i] ** 3 * 0.1) * np.exp(-0.1 * abs(x_scaled[i]))
            # Saddle point contribution
            result += 0.5 * np.sin(x_scaled[i] * 2 * np.pi) * np.cos(x_scaled[i] * 2 * np.pi)
        
        # Add a global minimum at the origin with a complex penalty term
        result += 0.005 * np.sum(x ** 6) + 0.02 * np.sum(np.abs(x) ** 1.5)
        
        return result