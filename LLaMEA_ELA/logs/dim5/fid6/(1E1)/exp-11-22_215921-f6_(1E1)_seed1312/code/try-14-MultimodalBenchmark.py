import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate random rotation matrix for conditioning
        self.rotation_matrix = np.random.randn(dim, dim)
        self.rotation_matrix, _ = np.linalg.qr(self.rotation_matrix)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Apply rotation to create non-separability
        x_rotated = self.rotation_matrix @ x_norm
        
        # Ellipsoid term with varying condition numbers
        condition_numbers = np.logspace(0, 2, self.dim)
        ellipsoid = np.sum(condition_numbers * x_rotated**2)
        
        # Add saddle points using trigonometric functions
        saddle = 0.5 * np.sum(np.sin(3 * x_norm) * np.cos(2 * x_norm))
        
        # Introduce variable depth local minima with Gaussian bumps
        gaussian_bumps = 0.0
        for i in range(self.dim):
            center = 0.3 * np.sin(i * np.pi / self.dim)
            width = 0.5 + 0.5 * np.cos(i * np.pi / self.dim)
            gaussian_bumps += np.exp(-10 * (x_norm[i] - center)**2 / width**2)
        
        # Add coupling between dimensions with sinusoidal interaction
        coupling = 0.3 * np.sum(np.sin(4 * x_norm[:-1] + x_norm[1:]))
        
        # Dimension-dependent scaling factor
        scale_factor = 1.0 + 0.1 * np.log(self.dim + 1)
        
        return scale_factor * (ellipsoid + saddle + gaussian_bumps + coupling)