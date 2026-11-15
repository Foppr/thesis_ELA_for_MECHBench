import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute a rotation matrix
        self.rotation = np.random.rand(dim, dim)
        self.rotation = np.linalg.qr(self.rotation)[0]
        # Add a random shift
        self.shift = np.random.uniform(-2.0, 2.0, dim)
    
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
            # Polynomial term with varying degree
            result += (xi ** (i + 2)) * 0.1
            # Trigonometric components
            result += 2 * np.sin(xi * (i + 1)) * np.cos(xi * (i + 1) * 0.5)
            # Radial basis function component
            rbf = np.exp(-0.1 * xi ** 2) * np.sin(xi * np.pi)
            result += rbf * (i + 1) * 0.05
            # Cross-dimension interaction
            if i > 0:
                cross_term = np.sin(xi * x_rot[i-1] * 0.3) * np.exp(-0.01 * (xi - x_rot[i-1])**2)
                result += cross_term * (i + 1) * 0.02
        
        # Add a global shaping term to control the overall landscape
        result += 0.5 * np.sum(x_rot ** 4)
        
        # Add a penalty for being far from the origin to encourage convergence
        result += 0.01 * np.sum(x_rot ** 6)
        
        return result