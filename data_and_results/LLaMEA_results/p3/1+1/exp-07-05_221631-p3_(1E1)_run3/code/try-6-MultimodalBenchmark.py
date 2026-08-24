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
            f_val += 0.3 * np.sin(0.7 * x_rotated[i]) * np.cos(0.4 * x_rotated[i])
            
        # Add interaction terms between dimensions with varying strengths
        for i in range(self.dim - 1):
            f_val += 0.15 * x_rotated[i] * x_rotated[i+1] * np.sin(0.3 * x_rotated[i] + 0.2 * x_rotated[i+1])
            
        # Add higher-order polynomial terms for increased complexity
        f_val += 0.02 * np.sum(np.abs(x_rotated)**3)
        
        # Add cross-terms with different frequencies for richer landscape
        for i in range(self.dim - 2):
            f_val += 0.08 * x_rotated[i] * x_rotated[i+1] * x_rotated[i+2] * np.cos(0.1 * x_rotated[i])
            
        return f_val