import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrix for added complexity
        self.rotation = np.random.rand(dim, dim) - 0.5
        self.rotation = np.dot(self.rotation, self.rotation.T)
        # Add some scaling to make the landscape more challenging
        self.scales = np.random.uniform(0.5, 2.0, dim)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation and scaling
        x_rot = np.dot(self.rotation, x) * self.scales
        
        # Compute the multimodal function with chaotic and barrier components
        result = 0.0
        for i in range(self.dim):
            # Quadratic term with scaling
            result += (x_rot[i] ** 2) * (i + 1)
            # Logarithmic barrier to prevent escaping from local regions
            result += 10 * np.log(1 + np.abs(x_rot[i]))
            # Gaussian hill structure to create multiple local minima
            result += 3 * np.exp(-0.5 * (x_rot[i] - 2 * np.sin(i)) ** 2)
            # Chaotic sine component to increase complexity
            result += 2 * np.sin(x_rot[i] * np.exp(i))
        
        # Add a global minimum at the origin with a small penalty term
        result += 0.01 * np.sum(x ** 4)
        
        return result