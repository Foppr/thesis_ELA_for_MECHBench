import numpy as np

class RotatedPeriodicElliptic:
    def __init__(self, dim):
        self.dim = dim
        # Generate random rotation matrix
        self.rotation_matrix = np.random.randn(dim, dim)
        self.rotation_matrix, _ = np.linalg.qr(self.rotation_matrix)
        
    def f(self, x):
        # Apply rotation
        x_rot = self.rotation_matrix @ x
        
        # Elliptic landscape with varying axis ratios
        condition_number = 100.0
        weights = np.logspace(0, np.log10(condition_number), self.dim)
        
        # Quadratic form with elliptic shape
        quadratic = np.sum(weights * x_rot**2)
        
        # Add periodic perturbations to create local optima
        periodic = 0.5 * np.sum(np.sin(3 * np.pi * x_rot) * np.cos(2 * np.pi * x_rot))
        
        # Add a small cubic term for additional complexity
        cubic = 0.01 * np.sum(x_rot**3)
        
        result = quadratic + periodic + cubic
        
        return result