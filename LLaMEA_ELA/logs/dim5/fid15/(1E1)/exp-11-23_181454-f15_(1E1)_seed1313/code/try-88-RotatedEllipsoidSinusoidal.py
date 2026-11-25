import numpy as np

class RotatedEllipsoidSinusoidal:
    def __init__(self, dim):
        self.dim = dim
        # Generate random rotation matrix
        self.rotation_matrix = np.random.randn(dim, dim)
        self.rotation_matrix, _ = np.linalg.qr(self.rotation_matrix)
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
        
        # Apply rotation
        x_rotated = self.rotation_matrix @ x
        
        # Ellipsoid term (smooth and separable)
        ellipsoid = np.sum([(i+1) * x_rotated[i]**2 for i in range(self.dim)])
        
        # Sinusoidal perturbation to create complexity
        sinusoidal = 0.1 * np.sum(np.sin(5.0 * x))
        
        # Add a small quadratic term to make the function bounded
        quadratic = 0.01 * np.sum(x**2)
        
        return ellipsoid + sinusoidal + quadratic