import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate random rotation matrix for added complexity
        self.rotation_matrix = np.random.randn(dim, dim)
        self.rotation_matrix, _ = np.linalg.qr(self.rotation_matrix)
        
    def f(self, x):
        # Apply rotation to input
        x_rotated = self.rotation_matrix @ x
        
        # Schwefel's function component: sum of -x*sin(sqrt(abs(x)))
        schwefel_term = np.sum(-x_rotated * np.sin(np.sqrt(np.abs(x_rotated))))
        
        # Add adaptive noise based on dimensionality
        noise = 0.1 * np.random.randn() * (1 + self.dim / 10.0)
        
        # Include saddle points with varying heights
        saddle_term = np.sum((x_rotated**2 - 100)**2) / 40000.0
        
        # Combine terms with different weights
        return 0.7 * schwefel_term + 0.2 * saddle_term + noise