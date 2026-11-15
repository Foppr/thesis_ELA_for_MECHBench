import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrix for added complexity
        self.rotation = np.random.rand(dim, dim) - 0.5
        self.rotation = np.dot(self.rotation, self.rotation.T)
        # Add conditioning parameters
        self.conditioning = np.linspace(1, 10, dim)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation and conditioning
        x_rot = np.dot(self.rotation, x) * self.conditioning
        
        # Compute the multimodal function with enhanced complexity
        result = 0.0
        for i in range(self.dim):
            # Quadratic term with variable conditioning
            result += 0.5 * (x_rot[i] ** 2) * (i + 1)
            # Enhanced periodic term with varying frequencies
            freq = (i + 1) * np.pi * (1 + 0.5 * np.sin(i))
            result += 5 * np.sin(x_rot[i] * freq)
            result += 3 * np.cos(x_rot[i] * freq * 1.5)
            # Additional ridge term with logarithmic scaling
            if x_rot[i] != 0:
                result += 2 * np.log(np.abs(x_rot[i]) + 1) * np.sin(x_rot[i] * (i + 1) * np.pi / 2)
            # Interaction term between adjacent dimensions with variable coupling
            if i > 0:
                coupling = 0.3 * (i + 1) * np.cos(x_rot[i] * x_rot[i-1])
                result += coupling
            # Cross-dimensional interaction term
            if i > 1:
                result += 0.2 * x_rot[i] * x_rot[i-1] * x_rot[i-2] * (i + 1)
            # Nonlinear scaling with fourth power
            result += 0.01 * (x_rot[i] ** 4)
            # Saddle point enhancement
            result += 0.1 * (x_rot[i] ** 6) * np.cos(x_rot[i] * (i + 1) * np.pi / 3)
        
        # Add global minimum penalty term
        result += 0.005 * np.sum(x ** 6)
        
        return result