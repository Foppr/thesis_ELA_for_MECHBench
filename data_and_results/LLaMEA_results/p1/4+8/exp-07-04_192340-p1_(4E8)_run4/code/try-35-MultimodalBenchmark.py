import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrix for added complexity
        self.rotation = np.random.rand(dim, dim) - 0.5
        self.rotation = np.dot(self.rotation, self.rotation.T)
        # Add chaotic component for enhanced complexity
        self.chaotic_params = np.random.rand(dim) * 2 + 1
        # Additional interaction terms between dimensions
        self.interaction_matrix = np.random.rand(dim, dim) * 0.5
        
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
            result += 2 * np.cos(x_rot[i] * (i + 1) * np.pi)
            # Chaotic component for enhanced landscape complexity
            result += 3 * np.sin(x_rot[i] * self.chaotic_params[i] * np.pi) * np.cos(x_rot[i] * self.chaotic_params[i] * np.pi / 3)
            # Saddle point enhancement
            result += 0.5 * np.sin(2 * x_rot[i]) * np.cos(2 * x_rot[i])
            # Interaction terms between dimensions
            for j in range(self.dim):
                if i != j:
                    result += 0.3 * self.interaction_matrix[i, j] * np.sin(x_rot[i]) * np.cos(x_rot[j])
        
        # Add a global minimum at the origin with a small penalty term
        result += 0.01 * np.sum(x ** 4)
        
        # Add variable conditioning to increase difficulty
        conditioning = np.array([1.0 + 0.5 * np.sin(i) for i in range(self.dim)])
        result *= np.prod(conditioning)
        
        # Add a highly nonlinear component to increase complexity
        nonlinear_term = np.sum(np.sin(x_rot ** 3)) * 0.1
        result += nonlinear_term
        
        return result