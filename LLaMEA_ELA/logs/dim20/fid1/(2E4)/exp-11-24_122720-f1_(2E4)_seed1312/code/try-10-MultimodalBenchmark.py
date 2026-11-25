import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrix for added complexity
        self.rotation_matrix = np.random.rand(dim, dim) - 0.5
        self.rotation_matrix = np.dot(self.rotation_matrix, self.rotation_matrix.T)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation to create non-separable landscape
        x_rotated = np.dot(self.rotation_matrix, x)
        
        # Combine multiple periodic components with varying frequencies
        result = 0.0
        for i in range(self.dim):
            xi = x_rotated[i]
            # Multiple sinusoidal terms with different frequencies and amplitudes
            result += (xi**4 - 10 * xi**2 + 5 * np.sin(3 * xi) + 3 * np.cos(2 * xi))
        
        # Add a global scaling factor and offset to shift the landscape
        return 0.5 * result + 15 * self.dim