import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrix for rotation-invariance
        self.rotation = np.random.rand(dim, dim) - 0.5
        self.rotation = np.dot(self.rotation, self.rotation.T)
        # Add a small random shift to make the function less symmetric
        self.shift = np.random.uniform(-0.5, 0.5, dim)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation and shift
        x_rot = np.dot(self.rotation, x) + self.shift
        
        # Initialize result
        result = 0.0
        
        # Polynomial and trigonometric components
        for i in range(self.dim):
            xi = x_rot[i]
            # Polynomial term with increasing degree
            result += (xi ** (i + 2)) * 0.1
            # Trigonometric components with varying frequencies
            result += 2 * np.sin(xi * (i + 1)) * np.cos(xi * (i + 1) * 0.5)
            # Asymmetric logarithmic barrier (stronger penalty for positive values)
            if xi > 0:
                result += np.log(1 + xi ** 2) * 0.2
            else:
                result += np.log(1 - xi ** 2) * 0.1
            # Exponential decay component with dynamic scaling
            scale = 1.0 / (1.0 + np.abs(xi))
            result += np.exp(-scale * xi ** 2) * np.sin(xi) * 0.05
        
        # Dynamic scaling based on input magnitude
        magnitude = np.linalg.norm(x_rot)
        dynamic_scale = 1.0 + 0.5 * np.sin(magnitude)
        result *= dynamic_scale
        
        # Add a global penalty term for large values
        penalty = 0.01 * np.sum(np.abs(x_rot) ** 4)
        result += penalty
        
        return result