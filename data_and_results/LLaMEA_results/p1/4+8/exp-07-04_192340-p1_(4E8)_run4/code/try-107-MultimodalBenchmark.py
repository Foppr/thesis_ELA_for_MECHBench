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
        
        # Compute the multimodal function with exponential decay and sinusoidal components
        result = 0.0
        for i in range(self.dim):
            # Quadratic term with varying coefficients
            result += (x_rot[i] ** 2) * (i + 1) * 0.1
            # Sinusoidal components with exponentially decaying amplitudes
            freq = (i + 1) * np.pi / 2
            amp = np.exp(-0.1 * i)
            result += amp * np.sin(freq * x_rot[i]) * np.cos(freq * x_rot[i] / 2)
            # Exponentially decaying barrier terms to encourage convergence
            barrier = np.exp(-0.5 * (x_rot[i] ** 2)) * (i + 1) * 0.2
            result += barrier
            # Saddle-point attractor terms to create complex landscape
            saddle = np.sin(x_rot[i] ** 2) * np.cos(x_rot[i]) * (i + 1) * 0.05
            result += saddle
        
        # Add a penalty for large values to encourage convergence
        result += 0.001 * np.sum(np.abs(x_rot) ** 4)
        
        return result