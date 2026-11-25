import numpy as np

class RotatedPeriodicEllipsoid:
    def __init__(self, dim):
        self.dim = dim
        # Generate random rotation matrix for dimensionality
        self.rotation_matrix = np.random.randn(dim, dim)
        self.rotation_matrix, _ = np.linalg.qr(self.rotation_matrix)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation
        x_rotated = self.rotation_matrix @ x
        
        # Base rotated ellipsoid term
        f = np.sum((x_rotated**2) * np.arange(1, self.dim + 1))
        
        # Add periodic components with varying frequencies and amplitudes
        for i in range(self.dim):
            f += 0.5 * np.sin(2 * np.pi * x[i] / 3.0) * np.cos(np.pi * x[i] / 2.0)
            
        # Add saddle point interactions between pairs of dimensions
        for i in range(0, self.dim - 1, 2):
            j = i + 1
            f += 0.3 * (x[i]**2 - x[j]**2) * np.sin(0.5 * x[i] * x[j])
            
        # Add coupling terms with exponential decay
        for i in range(self.dim):
            f += 0.2 * np.exp(-0.1 * np.abs(x[i])) * np.cos(3 * x[i])
            
        # Add cubic and quartic cross-terms
        for i in range(self.dim):
            f += 0.1 * x[i]**3 + 0.05 * x[i]**4
            
        # Add global periodic modulation
        f += 0.4 * np.sin(0.2 * np.sum(x**2))
        
        return f