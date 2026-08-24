import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrix for rotation-invariance
        self.rotation = np.random.rand(dim, dim) - 0.5
        self.rotation = np.dot(self.rotation, self.rotation.T)
        # Add a small random shift to make the function less symmetric
        self.shift = np.random.uniform(-0.5, 0.5, dim)
        # Adaptive scaling factor to control landscape ruggedness
        self.scaling = np.random.uniform(0.5, 2.0, dim)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation and shift
        x_rot = np.dot(self.rotation, x) + self.shift
        
        # Compute the multimodal function with periodic and saddle components
        result = 0.0
        for i in range(self.dim):
            # Quadratic term with adaptive scaling
            result += 0.5 * self.scaling[i] * (x_rot[i] ** 2)
            # Periodic cosine components to create multimodality
            result += 3 * np.cos(self.scaling[i] * x_rot[i] * np.pi / 2) * np.cos(x_rot[i] * np.pi)
            # Saddle point contribution to increase optimization difficulty
            result += 2 * np.sin(x_rot[i] * np.pi / 4) * np.sin(x_rot[i] * np.pi / 2)
            # Additional harmonic term to increase complexity
            result += 1.5 * np.cos(x_rot[i] * np.pi * (i + 1)) * np.sin(x_rot[i] * np.pi * (i + 1) / 3)
            # Exponential barrier near boundaries to prevent divergence
            barrier = np.exp(-0.5 * (np.abs(x_rot[i]) - 4.5) ** 2)
            result += barrier * (i + 1) * 0.1
            # Add a small noise-like component for robustness testing
            noise = 0.05 * np.sin(x_rot[i] * np.pi * (i + 1) * 3)
            result += noise
        
        # Add a penalty term for large values to encourage convergence
        result += 0.001 * np.sum(np.abs(x_rot) ** 3)
        
        return result