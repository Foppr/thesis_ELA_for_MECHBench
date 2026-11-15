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
            # Exponential decay term to increase landscape complexity
            exp_decay = np.exp(-0.1 * np.abs(x_rot[i]))
            result += exp_decay * (i + 1) * 0.03
        
        # Add a dynamic penalty based on landscape curvature
        curvature_penalty = 0.0
        for i in range(self.dim):
            # Estimate local curvature using finite differences
            h = 1e-4
            second_diff = (np.sin(x_rot[i] + h) - 2 * np.sin(x_rot[i]) + np.sin(x_rot[i] - h)) / (h ** 2)
            curvature_penalty += np.abs(second_diff) * (i + 1) * 0.01
        
        result += curvature_penalty
        
        return result