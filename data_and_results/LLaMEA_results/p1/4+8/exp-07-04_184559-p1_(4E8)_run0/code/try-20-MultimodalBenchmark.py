import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrix for added complexity
        np.random.seed(42)  # For reproducibility
        self.rotation = np.random.randn(dim, dim)
        self.rotation, _ = np.linalg.qr(self.rotation)
    
    def f(self, x):
        # Rotate the input vector
        x_rot = self.rotation @ x
        
        # Base ellipsoid term with varying condition numbers
        f1 = np.sum((x_rot**2) * np.arange(1, self.dim + 1))
        
        # Add sharp ridges using absolute values with sinusoidal modulation
        f2 = np.sum(np.abs(x_rot) * np.sin(10 * np.pi * x_rot) * np.cos(5 * np.pi * x_rot))
        
        # Add chaotic noise component for increased multimodality
        noise = 0.2 * np.sin(np.sum(x_rot**2)) * np.random.rand()
        
        # Combine terms with different weights
        return f1 + 0.7 * f2 + noise