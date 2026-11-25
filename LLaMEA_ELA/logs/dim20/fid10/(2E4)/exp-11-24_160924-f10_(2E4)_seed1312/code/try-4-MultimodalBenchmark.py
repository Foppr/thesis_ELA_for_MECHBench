import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrix for conditioning
        self.rotation_matrix = np.random.rand(dim, dim)
        self.rotation_matrix, _ = np.linalg.qr(self.rotation_matrix)
    
    def f(self, x):
        # Rotate input vector
        x_rotated = self.rotation_matrix @ x
        
        # Elliptic term with varying condition numbers
        elliptic = 0.0
        for i in range(self.dim):
            elliptic += (10 ** (2 * i / (self.dim - 1))) * (x_rotated[i] ** 2)
        
        # Sinusoidal perturbation creating multiple local minima
        sinusoidal = 0.0
        for i in range(self.dim):
            sinusoidal += np.sin(3 * np.pi * x_rotated[i]) * np.cos(7 * np.pi * x_rotated[i])
        
        # Combine terms with different weights
        return 0.1 * elliptic + 0.05 * sinusoidal + 0.01 * np.sum(x ** 2)