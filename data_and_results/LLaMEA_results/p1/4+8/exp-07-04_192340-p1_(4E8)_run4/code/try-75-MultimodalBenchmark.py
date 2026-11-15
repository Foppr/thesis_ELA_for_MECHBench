import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic coefficients for varying curvature and rotation
        self.coeffs = np.random.rand(dim) * 3 + 1
        self.rotation_matrix = np.random.rand(dim, dim) * 2 - 1
        self.rotation_matrix = np.dot(self.rotation_matrix, self.rotation_matrix.T)
        self.saddle_points = np.random.rand(dim) * 10 - 5
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation to x
        x_rotated = np.dot(self.rotation_matrix, x)
        
        # Compute chaotic exponential terms with rotation
        result = 0.0
        for i in range(self.dim):
            # Exponential decay with chaotic coefficients
            result += self.coeffs[i] * np.exp(-0.5 * (x_rotated[i] - self.saddle_points[i])**2)
            # Saddle point contribution with varying curvature
            result += 0.5 * (x_rotated[i] - self.saddle_points[i])**2 * np.sin(x_rotated[i])
            # Chaotic gradient component
            result += 0.1 * np.sin(self.coeffs[i] * x_rotated[i]) * np.cos(x_rotated[i])
            # Logarithmic barrier term to prevent boundary escape
            result += 1.0 * np.log(1.0 + (x_rotated[i] - self.saddle_points[i])**2)
            
        # Add coupling terms between dimensions for increased complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.05 * np.sin(x_rotated[i] * x_rotated[j]) * (i + j)
                # Add composite sinusoidal components
                result += 0.02 * np.cos(x_rotated[i] * x_rotated[j]) * np.sin(x_rotated[i] + x_rotated[j])
                
        # Add global minimum at origin with penalty
        result += 0.001 * np.sum(x_rotated**6)
        
        # Add noise component to increase robustness testing
        noise = np.random.rand() * 0.01
        result += noise
        
        return result