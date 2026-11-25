import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrix for added complexity
        self.rotation_matrix = np.random.rand(dim, dim) - 0.5
        self.rotation_matrix = np.dot(self.rotation_matrix, self.rotation_matrix.T)
        np.fill_diagonal(self.rotation_matrix, 1.0)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation to create non-separable landscape
        x_rotated = np.dot(self.rotation_matrix, x)
        
        # Elliptic function with varying condition numbers
        result = 0.0
        for i in range(self.dim):
            # Varying coefficients to create conditioning differences
            coeff = 10**(2 * i / (self.dim - 1)) if self.dim > 1 else 1.0
            result += coeff * x_rotated[i]**2
            
        # Add sinusoidal modulation to create multiple local minima
        for i in range(self.dim):
            result += 0.5 * np.sin(3 * x_rotated[i])**2 + 0.3 * np.cos(2 * x_rotated[i])
            
        # Add noise term to make the landscape stochastic
        noise = np.random.normal(0, 0.1)
        result += noise
        
        return result