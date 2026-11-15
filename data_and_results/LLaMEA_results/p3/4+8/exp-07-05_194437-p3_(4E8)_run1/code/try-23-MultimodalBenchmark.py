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
        
        # Apply rotation to create interaction between dimensions
        x_rotated = self.rotation_matrix @ x
        
        # Base quadratic term (ellipsoid shape)
        result = np.sum(x_rotated**2)
        
        # Add saddle points using trigonometric functions with varying frequencies
        for i in range(self.dim):
            result += 15 * np.sin(0.5 * x_rotated[i]) * np.cos(0.9 * x_rotated[i]) + \
                      10 * np.sin(0.2 * x_rotated[i]) * np.cos(0.4 * x_rotated[i])
        
        # Add noise-like perturbations with non-linear components
        noise = 0.0
        for i in range(self.dim):
            noise += 2.5 * np.sin(0.15 * x_rotated[i]**2) * np.cos(0.25 * x_rotated[i]**3) + \
                     1.5 * np.sin(0.3 * x_rotated[i]) * np.cos(0.6 * x_rotated[i])
        
        result += noise
        
        # Add cross-dimension interactions with stronger coupling
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Increased interaction range
                result += 0.5 * x_rotated[i] * x_rotated[j] * np.sin(0.7 * (x_rotated[i] + x_rotated[j])) + \
                          0.2 * x_rotated[i] * x_rotated[j] * np.cos(0.3 * (x_rotated[i] - x_rotated[j]))
        
        # Add non-uniform scaling based on dimension index to increase conditioning
        scaling_factor = 1.0
        for i in range(self.dim):
            scaling_factor += 0.05 * np.sin(0.1 * i) * np.cos(0.2 * i)
        
        result *= scaling_factor
        
        # Add a global offset to avoid trivial solutions
        result += 0.1 * np.sum(np.abs(x)**1.5)
        
        return result