import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrix for added complexity
        self.rotation = np.random.rand(dim, dim) - 0.5
        self.rotation = np.dot(self.rotation, self.rotation.T)
        # Add a small random shift to make the function less symmetric
        self.shift = np.random.uniform(-0.5, 0.5, dim)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation and shift
        x_rot = np.dot(self.rotation, x) + self.shift
        
        # Compute the multimodal function with chaotic and barrier components
        result = 0.0
        for i in range(self.dim):
            # Quadratic term with varying coefficients
            result += (x_rot[i] ** 2) * (i + 1) * 0.3
            # Sinusoidal components with varying frequencies and amplitudes
            result += 2.5 * np.sin(x_rot[i] * (i + 1) * np.pi / 2.5) * np.cos(x_rot[i] * (i + 1) * np.pi / 4.5)
            # Enhanced logarithmic barrier to prevent divergence
            log_term = np.log(1 + np.abs(x_rot[i]) ** 2.5)
            result += log_term * (i + 1) * 0.15
            # Additional chaotic component using a logistic map-like term
            chaotic = np.sin(np.pi * x_rot[i] * np.sin(x_rot[i] * 0.5))
            result += chaotic * (i + 1) * 0.08
        
        # Add a small penalty for large values to encourage convergence
        result += 0.0015 * np.sum(np.abs(x_rot) ** 3.5)
        
        return result