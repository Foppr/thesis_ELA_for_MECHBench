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
        
        # Apply rotation to create a more complex landscape
        x_rotated = self.rotation_matrix @ x
        
        # Base ellipsoid function
        result = np.sum(x_rotated**2)
        
        # Add sinusoidal modulation to create multiple local minima
        modulation = np.sum(np.sin(3 * x_rotated) * np.cos(2 * x_rotated))
        
        # Add Gaussian noise to make it more challenging
        noise = np.random.normal(0, 0.01)
        
        # Combine all components
        result = result + 0.5 * modulation + noise
        
        return result