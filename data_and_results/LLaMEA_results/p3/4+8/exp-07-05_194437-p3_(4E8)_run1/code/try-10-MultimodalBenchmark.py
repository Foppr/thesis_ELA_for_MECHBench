import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate random rotation matrix
        self.rotation = np.random.randn(dim, dim)
        self.rotation, _ = np.linalg.qr(self.rotation)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation
        x_rot = self.rotation @ x
        
        # Base quadratic term (ellipsoid)
        result = np.sum(x_rot**2)
        
        # Add periodic components with varying frequencies
        for i in range(self.dim):
            result += 5 * np.sin(2 * np.pi * x_rot[i] / 2.0) * np.cos(3 * np.pi * x_rot[i] / 3.0)
        
        # Add noise component
        result += 0.1 * np.sum(np.random.randn(self.dim) * x_rot)
        
        # Add cross-dimensional interaction terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.3 * np.sin(x_rot[i] + x_rot[j]) * np.cos(x_rot[i] - x_rot[j])
        
        # Add a global scaling factor to make it more challenging
        result *= (1.0 + 0.1 * np.sum(np.abs(x_rot)))
        
        return result