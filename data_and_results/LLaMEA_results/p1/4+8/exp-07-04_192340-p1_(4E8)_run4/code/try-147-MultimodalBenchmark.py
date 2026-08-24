import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute a rotation matrix with orthogonalization
        self.rotation = np.random.rand(dim, dim)
        self.rotation = np.dot(self.rotation, self.rotation.T)
        # Add a random shift to increase asymmetry
        self.shift = np.random.uniform(-1.0, 1.0, dim)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation and shift
        x_rot = np.dot(self.rotation, x) + self.shift
        
        # Initialize result
        result = 0.0
        
        # Add periodic cosine components with varying frequencies and amplitudes
        for i in range(self.dim):
            # Cosine-based multimodal term
            result += 3 * np.cos(x_rot[i] * (i + 1) * np.pi / 2) * np.cos(x_rot[i] * (i + 1) * np.pi / 4)
            # Saddle-point structure with quadratic and quartic terms
            result += 0.5 * x_rot[i] ** 2 - 0.1 * x_rot[i] ** 4
            # Gradient-adaptive penalty term
            grad_magnitude = np.abs(x_rot[i]) * (i + 1)
            penalty = 0.05 * grad_magnitude ** 2.5
            result += penalty
            # Cross-dimension interaction with a cosine-based coupling
            if i > 0:
                cross_term = np.cos(x_rot[i] * x_rot[i-1] * np.pi / 3) * (x_rot[i] ** 2 + x_rot[i-1] ** 2)
                result += cross_term * 0.02 * (i + 1)
        
        # Add a global barrier to keep solutions near the center
        barrier = 0.01 * np.sum(x_rot ** 4)
        result += barrier
        
        return result