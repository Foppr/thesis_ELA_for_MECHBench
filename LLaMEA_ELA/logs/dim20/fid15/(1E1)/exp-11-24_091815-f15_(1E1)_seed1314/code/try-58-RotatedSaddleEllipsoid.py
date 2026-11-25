import numpy as np

class RotatedSaddleEllipsoid:
    def __init__(self, dim):
        self.dim = dim
        # Generate random rotation matrix for conditioning
        self.rotation = np.random.randn(dim, dim)
        self.rotation, _ = np.linalg.qr(self.rotation)
        # Varying conditioning factors per dimension
        self.conditioning = np.logspace(0, 2, dim)
        
    def f(self, x):
        # Apply rotation and conditioning
        x_rot = self.rotation @ (x / 5.0)  # Normalize to [-1, 1]
        x_rot_cond = x_rot * np.sqrt(self.conditioning)
        
        # Quadratic ellipsoid term
        ellipsoid = np.sum(x_rot_cond**2)
        
        # Embedded saddle points using high-frequency sinusoids
        saddle = np.sum(np.sin(10 * np.pi * x_rot)**2 * (x_rot**2))
        
        # Additional non-convexity with polynomial terms
        poly_term = np.sum((x_rot**4) * np.cos(3 * np.pi * x_rot))
        
        # Cross-dimensional interaction via weighted sum of products
        cross = 0.1 * np.sum(x_rot[:-1] * x_rot[1:] * self.conditioning[:-1])
        
        return ellipsoid + saddle + poly_term + cross