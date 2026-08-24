import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrix for added complexity
        np.random.seed(42)  # For reproducibility
        self.rotation_matrix = np.random.randn(dim, dim)
        self.rotation_matrix, _ = np.linalg.qr(self.rotation_matrix)
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation to create correlation between dimensions
        x_rotated = self.rotation_matrix @ x
        
        # Base quadratic term (ellipsoid)
        f_val = np.sum(x_rotated**2)
        
        # Add sinusoidal perturbations to create multiple local minima
        for i in range(self.dim):
            f_val += 0.5 * np.sin(0.5 * x_rotated[i]) * np.cos(0.3 * x_rotated[i])
            
        # Add interaction terms between dimensions
        for i in range(self.dim - 1):
            f_val += 0.1 * x_rotated[i] * x_rotated[i+1] * np.sin(0.2 * x_rotated[i])
            
        # Add a small quartic term for additional complexity
        f_val += 0.01 * np.sum(x_rotated**4)
        
        return f_val