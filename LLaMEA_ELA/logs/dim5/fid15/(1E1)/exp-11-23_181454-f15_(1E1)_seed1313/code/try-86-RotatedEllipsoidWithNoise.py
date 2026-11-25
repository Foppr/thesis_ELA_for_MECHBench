import numpy as np

class RotatedEllipsoidWithNoise:
    def __init__(self, dim):
        self.dim = dim
        # Generate random rotation matrix
        self.rotation_matrix = np.random.randn(dim, dim)
        self.rotation_matrix, _ = np.linalg.qr(self.rotation_matrix)
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
        
        # Rotate the input
        x_rotated = self.rotation_matrix @ x
        
        # Ellipsoid term with varying conditioning
        result = 0.0
        for i in range(self.dim):
            result += (10 ** (2 * i / (self.dim - 1))) * (x_rotated[i] ** 2)
        
        # Add periodic noise to create multiple local minima
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(5 * x[i]) * np.cos(3 * x[i])
        
        # Add a small quadratic term to make the function bounded
        quadratic_term = 0.01 * np.sum(x ** 2)
        
        return result + noise + quadratic_term