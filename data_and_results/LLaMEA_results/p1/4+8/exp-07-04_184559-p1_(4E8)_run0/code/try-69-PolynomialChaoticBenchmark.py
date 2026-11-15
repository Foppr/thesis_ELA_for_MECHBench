import numpy as np

class PolynomialChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute polynomial chaos coefficients for different degrees
        self.poly_coeffs = np.random.randn(dim, 5)
        # Generate random rotation matrices for each dimension
        self.rotations = [np.random.randn(dim, dim) for _ in range(3)]
        # Normalize rotation matrices
        for i in range(len(self.rotations)):
            self.rotations[i] = self.rotations[i] @ self.rotations[i].T
            self.rotations[i] = self.rotations[i] / np.linalg.norm(self.rotations[i], axis=0)
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial chaos expansion component
        poly_term = 0.0
        for i in range(self.dim):
            for j in range(5):
                poly_term += self.poly_coeffs[i, j] * np.power(x_norm[i], j)
        
        # Radial basis function with adaptive conditioning
        rbf_term = 0.0
        centers = np.random.randn(10, self.dim)
        for i in range(10):
            diff = x_norm - centers[i]
            # Adaptive conditioning based on distance
            sigma = 0.5 + 0.5 * np.exp(-np.sum(diff**2) / 2)
            rbf_term += np.exp(-np.sum(diff**2) / (2 * sigma**2))
        
        # Global rotation term creating deceptive landscape
        rot_term = 0.0
        for i, rotation in enumerate(self.rotations):
            rotated_x = rotation @ x_norm
            rot_term += np.sum(np.sin(rotated_x) * np.cos(rotated_x)) * (i + 1)
        
        # Cross-dimensional interaction term
        interaction_term = 0.0
        for i in range(self.dim - 1):
            interaction_term += np.sin(x_norm[i] * x_norm[i+1]) * np.exp(-0.5 * (x_norm[i] - x_norm[i+1])**2)
        
        # Combine all components with varying weights
        return 1.2 * poly_term + 0.8 * rbf_term + 1.5 * rot_term + 0.6 * interaction_term