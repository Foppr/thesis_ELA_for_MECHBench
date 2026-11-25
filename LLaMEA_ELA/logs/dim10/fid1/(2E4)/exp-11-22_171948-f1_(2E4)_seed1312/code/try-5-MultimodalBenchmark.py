import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrix for added complexity
        np.random.seed(42)  # For reproducibility
        self.rotation_matrix = np.random.randn(dim, dim)
        self.rotation_matrix, _ = np.linalg.qr(self.rotation_matrix)
    
    def f(self, x):
        # Rotate the input vector
        x_rotated = self.rotation_matrix @ x
        
        # Standard ellipsoid term (quadratic)
        ellipsoid = np.sum(x_rotated**2)
        
        # Add periodic modulation to create multiple local minima
        period_modulation = np.sum(np.sin(3 * np.pi * x_rotated) * np.cos(2 * np.pi * x_rotated))
        
        # Add a Gaussian-like noise term with multiple peaks
        noise_term = np.sum(np.exp(-0.5 * (x_rotated / 1.0)**2) * np.cos(4 * np.pi * x_rotated))
        
        # Combine all terms with different weights
        result = ellipsoid + 0.5 * period_modulation + 0.1 * noise_term
        
        return result