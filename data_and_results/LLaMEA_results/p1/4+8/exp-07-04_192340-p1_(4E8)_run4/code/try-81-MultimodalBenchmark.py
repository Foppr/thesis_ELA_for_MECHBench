import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrix for rotation-invariance
        self.rotation = np.random.rand(dim, dim)
        self.rotation = np.dot(self.rotation, self.rotation.T)
        # Normalize rotation matrix
        self.rotation = self.rotation / np.linalg.norm(self.rotation, axis=0)
        # Add a small random shift
        self.shift = np.random.uniform(-0.2, 0.2, dim)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation and shift
        x_rot = np.dot(self.rotation, x) + self.shift
        
        # Compute the multimodal function with exponential and trigonometric components
        result = 0.0
        for i in range(self.dim):
            # Quadratic term with varying coefficients
            result += 0.5 * (x_rot[i] ** 2) * (i + 1)
            # Exponential decay component with sinusoidal modulation
            exp_decay = np.exp(-0.1 * np.abs(x_rot[i]))
            sin_mod = np.sin(x_rot[i] * (i + 1) * np.pi / 4)
            result += exp_decay * sin_mod * (i + 1) * 0.3
            # Saddle point contribution
            saddle = np.sin(x_rot[i] * (i + 1) * np.pi / 2) * np.cos(x_rot[i] * (i + 1) * np.pi / 3)
            result += saddle * (i + 1) * 0.2
            # Logarithmic barrier to prevent divergence
            log_term = np.log(1 + np.abs(x_rot[i]) ** 2)
            result += log_term * (i + 1) * 0.1
            # Chaotic sine-wave interaction
            chaotic = np.sin(np.pi * np.sin(x_rot[i] * (i + 1)))
            result += chaotic * (i + 1) * 0.05
        
        # Add penalty for large values to encourage convergence
        result += 0.001 * np.sum(np.abs(x_rot) ** 3)
        
        return result