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
            result += (x_rot[i] ** 2) * (i + 1) * 0.5
            # Sinusoidal components with varying frequencies and amplitudes
            result += 3 * np.sin(x_rot[i] * (i + 1) * np.pi / 3) * np.cos(x_rot[i] * (i + 1) * np.pi / 5)
            # Logarithmic barrier to prevent divergence
            log_term = np.log(1 + np.abs(x_rot[i]) ** 2)
            result += log_term * (i + 1) * 0.1
            # Additional chaotic component using a logistic map-like term
            chaotic = np.sin(np.pi * x_rot[i] * np.sin(x_rot[i]))
            result += chaotic * (i + 1) * 0.05
            # Introduce saddle points with higher-order polynomial terms
            result += 0.5 * (x_rot[i] ** 4) * np.cos(x_rot[i] * np.pi / 2) * (i + 1) * 0.01
        
        # Add a small penalty for large values to encourage convergence
        result += 0.001 * np.sum(np.abs(x_rot) ** 3)
        
        # Add a composite sinusoidal term to increase multimodality
        composite_sin = np.sum(np.sin(x_rot * np.pi / 2) * np.cos(x_rot * np.pi / 4))
        result += composite_sin * 0.2
        
        return result