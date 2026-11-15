import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrix for rotation-invariance
        self.rotation = np.random.rand(dim, dim) - 0.5
        self.rotation = np.dot(self.rotation, self.rotation.T)
        # Add a small random shift to make the function less symmetric
        self.shift = np.random.uniform(-0.5, 0.5, dim)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation and shift
        x_rot = np.dot(self.rotation, x) + self.shift
        
        # Compute the multimodal function with exponential decay and chaotic components
        result = 0.0
        for i in range(self.dim):
            # Quadratic term with varying coefficients
            result += (x_rot[i] ** 2) * (i + 1) * 0.1
            # Sinusoidal components with varying frequencies and amplitudes
            result += 2 * np.sin(x_rot[i] * (i + 1) * np.pi / 4) * np.cos(x_rot[i] * (i + 1) * np.pi / 6)
            # Exponential decay term to encourage convergence
            exp_term = np.exp(-0.1 * np.abs(x_rot[i]))
            result += exp_term * (i + 1) * 0.2
            # Chaotic component using a logistic map-like term for increased complexity
            logistic_map = 4.0 * np.mod(x_rot[i], 1.0) * (1.0 - np.mod(x_rot[i], 1.0))
            chaotic = np.sin(np.pi * logistic_map * x_rot[i])
            result += chaotic * (i + 1) * 0.08
        
        # Add a penalty for large values to encourage convergence
        result += 0.001 * np.sum(np.abs(x_rot) ** 4)
        
        return result