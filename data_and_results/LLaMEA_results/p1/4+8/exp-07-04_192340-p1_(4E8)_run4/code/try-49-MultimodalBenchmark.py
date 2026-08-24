import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrix for added complexity
        self.rotation = np.random.rand(dim, dim) - 0.5
        self.rotation = np.dot(self.rotation, self.rotation.T)
        # Add chaotic component for enhanced complexity
        self.chaotic_params = np.random.rand(dim) * 2 + 1
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation
        x_rot = np.dot(self.rotation, x)
        
        # Compute the multimodal function with periodic and ridge components
        result = 0.0
        for i in range(self.dim):
            # Quadratic term with scaling
            result += (x_rot[i] ** 2) * (i + 1)
            # Periodic term to create multiple local minima
            result += 5 * np.sin(x_rot[i] * (i + 1) * np.pi / 2)
            # Additional ridge term for sharp convergence challenges
            result += 2.5 * np.cos(x_rot[i] * (i + 1) * np.pi)
            # Chaotic component for enhanced landscape complexity
            result += 3.5 * np.sin(x_rot[i] * self.chaotic_params[i] * np.pi) * np.cos(x_rot[i] * self.chaotic_params[i] * np.pi / 3)
            # Saddle point enhancement with modified amplitude
            result += 0.7 * np.sin(2 * x_rot[i]) * np.cos(2 * x_rot[i])
            # Additional chaotic ridge structure
            result += 1.8 * np.sin(x_rot[i] * self.chaotic_params[i] * np.pi * 2) * np.cos(x_rot[i] * self.chaotic_params[i] * np.pi)
            # Interaction term between dimensions to increase complexity
            if i > 0:
                result += 0.3 * np.sin(x_rot[i-1] * x_rot[i] * np.pi)
        
        # Add a global minimum at the origin with a small penalty term
        result += 0.01 * np.sum(x ** 4)
        
        # Add variable conditioning to increase difficulty
        conditioning = np.array([1.0 + 0.5 * np.sin(i * 0.5) for i in range(self.dim)])
        result *= np.prod(conditioning)
        
        # Add a new chaotic modulation term to improve fitness score
        chaotic_modulation = np.prod(np.sin(x_rot * np.pi / 4) + 0.5)
        result += 2.5 * chaotic_modulation
        
        return result