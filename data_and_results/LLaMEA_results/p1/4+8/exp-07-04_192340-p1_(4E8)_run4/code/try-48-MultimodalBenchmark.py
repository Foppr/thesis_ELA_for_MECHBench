import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrix for added complexity
        self.rotation = np.random.rand(dim, dim) - 0.5
        self.rotation = np.dot(self.rotation, self.rotation.T)
        # Add chaotic scaling factors for each dimension
        self.scaling = 1.0 + 2.0 * np.random.rand(dim)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation and scaling
        x_rot = np.dot(self.rotation, x) * self.scaling
        
        # Compute the multimodal function with enhanced chaotic components
        result = 0.0
        for i in range(self.dim):
            # Quadratic term with adaptive scaling
            result += (x_rot[i] ** 2) * (i + 1) * 0.5
            # Chaotic sine component with varying frequencies and amplitudes
            freq = (i + 1) * np.pi * (1.0 + 0.5 * np.sin(i))
            result += 8 * np.sin(x_rot[i] * freq) * np.cos(x_rot[i] * freq * 0.7)
            # Additional ridge term with exponential decay
            result += 2.5 * np.exp(-0.1 * np.abs(x_rot[i])) * np.sin(x_rot[i] * (i + 1) * np.pi * 1.5)
            # Cross-dimensional interaction with chaotic coupling
            if i > 0:
                coupling = 0.3 * np.sin(x_rot[i] * x_rot[i-1] * (i + 1) * 0.5)
                result += coupling * (i + 1)
            # Add a small chaotic perturbation to encourage global exploration
            result += 0.1 * np.sin(x_rot[i] * 10.0 * (i + 1))
        
        # Add a global minimum at the origin with a penalty term for large values
        result += 0.005 * np.sum(x ** 6)
        
        return result