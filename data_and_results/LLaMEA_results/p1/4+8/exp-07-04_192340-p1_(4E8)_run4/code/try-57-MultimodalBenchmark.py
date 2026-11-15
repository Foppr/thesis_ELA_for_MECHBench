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
        
        # Compute the multimodal function with enhanced periodic and ridge components
        result = 0.0
        for i in range(self.dim):
            # Quadratic term with variable conditioning
            result += (x_rot[i] ** 2) * (i + 1)
            # Enhanced periodic term with multiple frequencies
            result += 3 * np.sin(x_rot[i] * (i + 1) * np.pi / 2) + 2 * np.sin(x_rot[i] * (i + 1) * np.pi)
            # Sharp ridge term with exponential decay
            result += 1.5 * np.cos(x_rot[i] * (i + 1) * np.pi) * np.exp(-0.1 * abs(x_rot[i]))
            # Chaotic component for additional complexity
            result += 0.5 * np.sin(10 * x_rot[i]) * np.cos(5 * x_rot[i])
            # Additional interaction terms between dimensions
            if i > 0:
                result += 0.3 * x_rot[i-1] * x_rot[i] * np.sin(x_rot[i-1] + x_rot[i])
        
        # Add a global minimum at the origin with a small penalty term
        result += 0.005 * np.sum(x ** 4)
        
        # Add a chaotic scaling factor based on the sum of coordinates
        chaotic_factor = 1 + 0.1 * np.sin(np.sum(x) * np.pi / 5)
        result *= chaotic_factor
        
        return result