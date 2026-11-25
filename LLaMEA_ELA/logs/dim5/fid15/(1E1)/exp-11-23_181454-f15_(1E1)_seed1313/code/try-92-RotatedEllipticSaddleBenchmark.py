import numpy as np

class RotatedEllipticSaddleBenchmark:
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
        
        # Elliptic function component (primary minimization)
        result = 0.0
        for i in range(self.dim):
            result += 10**(2 * i / (self.dim - 1)) * x_rotated[i]**2
            
        # Add saddle points at regular intervals
        saddle_term = 0.0
        for i in range(self.dim):
            saddle_term += 5 * np.sin(2 * np.pi * x_rotated[i] / 5.0) * np.cos(2 * np.pi * x_rotated[i] / 5.0)
            
        # Add noise to make it more challenging
        noise = 0.1 * np.sum(np.random.randn(self.dim) * x)
        
        return result + saddle_term + noise