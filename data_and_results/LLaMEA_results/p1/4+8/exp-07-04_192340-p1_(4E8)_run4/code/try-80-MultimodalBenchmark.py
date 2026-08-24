import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic rotation matrix
        self.rotation_matrix = np.random.rand(dim, dim) * 2 - 1
        self.rotation_matrix = np.dot(self.rotation_matrix, self.rotation_matrix.T)
        # Logarithmic barrier coefficients
        self.barrier_coeffs = np.random.rand(dim) * 0.5 + 0.5
        # Sinusoidal interaction coefficients
        self.sin_coeffs = np.random.rand(dim) * 2 + 1
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation
        x_rot = np.dot(self.rotation_matrix, x)
        
        # Polynomial chaos terms with logarithmic barriers
        result = 0.0
        for i in range(self.dim):
            # Polynomial chaos component
            result += x_rot[i]**4 + x_rot[i]**3 - 2*x_rot[i]**2
            # Logarithmic barrier
            barrier = -np.log(25.0 - x_rot[i]**2) if 25.0 - x_rot[i]**2 > 0 else 1000.0
            result += self.barrier_coeffs[i] * barrier
            # Composite sinusoidal interaction
            result += self.sin_coeffs[i] * np.sin(0.5 * x_rot[i]) * np.cos(0.3 * x_rot[i])
            
        # Add coupling terms between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(x_rot[i] * x_rot[j]) * np.cos(x_rot[i] + x_rot[j])
                result += 0.1 * coupling * (i + j)
                
        # Add global minimum penalty
        result += 0.01 * np.sum(x**8)
        
        return result