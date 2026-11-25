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
        
        # Rotate the input vector
        x_rotated = self.rotation_matrix @ x
        
        # Ellipsoid term with varying condition numbers
        ellipsoid_term = np.sum([(i + 1) * (x_rotated[i] ** 2) for i in range(self.dim)])
        
        # Add periodic noise to create many local optima
        noise_term = 0.5 * np.sum(np.sin(5 * x) * np.cos(3 * x))
        
        # Add a small quadratic penalty to keep solution within bounds
        bound_penalty = 0.1 * np.sum(np.maximum(0, np.abs(x) - 5.0) ** 2)
        
        return ellipsoid_term + noise_term + bound_penalty