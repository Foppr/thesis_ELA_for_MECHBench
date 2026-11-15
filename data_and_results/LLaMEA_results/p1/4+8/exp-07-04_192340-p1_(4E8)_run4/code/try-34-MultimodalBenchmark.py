import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute a more complex rotation matrix with orthogonalization
        self.rotation = np.random.rand(dim, dim)
        self.rotation = np.linalg.qr(self.rotation)[0]
        # Add multiple chaotic parameters for enhanced complexity
        self.chaotic_params = np.random.rand(dim, 3) * 2 + 1
        # Add a scaling factor for each dimension to increase conditioning
        self.scaling = np.random.rand(dim) * 3 + 1
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation and scaling
        x_scaled = np.dot(self.rotation, x) * self.scaling
        
        # Compute the multimodal function with enhanced periodic and ridge components
        result = 0.0
        for i in range(self.dim):
            # Quadratic term with scaling and conditioning
            result += (x_scaled[i] ** 2) * (i + 1) * self.scaling[i]
            # Multiple periodic terms to create complex local minima
            result += 3 * np.sin(x_scaled[i] * (i + 1) * np.pi / 2)
            result += 2 * np.cos(x_scaled[i] * (i + 1) * np.pi)
            result += 1.5 * np.sin(x_scaled[i] * (i + 1) * np.pi * 2)
            # Chaotic component with multiple parameters
            result += 2.5 * np.sin(x_scaled[i] * self.chaotic_params[i, 0] * np.pi) * np.cos(x_scaled[i] * self.chaotic_params[i, 1] * np.pi / 3)
            # Additional ridge structure with variable sharpness
            result += 1.2 * np.cos(x_scaled[i] * self.chaotic_params[i, 2] * np.pi * 1.5)
            # Saddle point enhancement with interaction terms
            if i > 0:
                result += 0.8 * np.sin(2 * x_scaled[i]) * np.cos(2 * x_scaled[i-1])
            # Cross-dimensional interaction terms for increased complexity
            for j in range(i):
                result += 0.5 * np.sin(x_scaled[i] * x_scaled[j] * (i + j + 1))
        
        # Add a global minimum at the origin with a more complex penalty term
        result += 0.02 * np.sum(x ** 6)
        
        # Add variable conditioning with exponential scaling
        conditioning = np.array([1.0 + 0.8 * np.sin(i * 2) * np.cos(i * 3) for i in range(self.dim)])
        result *= np.prod(conditioning ** 2)
        
        return result