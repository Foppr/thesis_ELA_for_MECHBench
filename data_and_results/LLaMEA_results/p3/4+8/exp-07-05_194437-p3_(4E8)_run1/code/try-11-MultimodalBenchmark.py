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
        
        # Add saddle points using trigonometric functions
        for i in range(self.dim):
            result += 20 * np.sin(0.3 * x_rotated[i]) * np.cos(0.7 * x_rotated[i])
        
        # Add noise-like perturbations
        noise = 0.0
        for i in range(self.dim):
            noise += 3 * np.sin(0.1 * x_rotated[i]**2) * np.cos(0.2 * x_rotated[i]**3)
        
        result += noise
        
        # Add cross-dimension interactions with varying strengths
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited interaction
                result += 0.3 * x_rotated[i] * x_rotated[j] * np.sin(0.5 * (x_rotated[i] + x_rotated[j]))
        
        # Add a global scaling factor to control function difficulty
        result *= 1.0 + 0.1 * np.sum(np.abs(x))
        
        return result