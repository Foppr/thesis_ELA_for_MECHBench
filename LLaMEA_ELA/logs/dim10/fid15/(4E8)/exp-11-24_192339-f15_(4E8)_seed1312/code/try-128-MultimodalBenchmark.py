import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrix for global conditioning
        np.random.seed(42)
        self.rotation_matrix = np.random.randn(dim, dim)
        self.rotation_matrix, _ = np.linalg.qr(self.rotation_matrix)
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Apply global rotation to introduce non-separability
        x_rotated = self.rotation_matrix @ x
        
        # Sinusoidal oscillation component with dynamic frequency
        sin_component = 0
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(0.3 * x[i])
            sin_component += np.sin(freq * x_rotated[i]) * np.cos(freq * x_rotated[i] / 2.0)
        
        # Radial basis function with adaptive width
        rbf_component = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x_rotated[i] - x_rotated[j])**2 + 0.1)
                width = 0.5 + 0.3 * np.abs(x[i]) * np.abs(x[j])
                rbf_component += np.exp(-dist**2 / (2 * width**2)) * np.sin(2 * dist)
        
        # Polynomial coupling with cross-dimensional interaction
        poly_component = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_component += (x_rotated[i]**2 + x_rotated[j]**2) * np.sin(0.5 * (x_rotated[i] + x_rotated[j]))
        
        # Adaptive conditioning based on dimension
        condition_factor = 1.0 + 0.5 * np.log(self.dim + 1)
        
        # Dynamic scaling with global shift
        global_shift = 0.2 * np.sum(np.abs(x))
        
        # Noise component
        noise = 0.05 * np.sum(np.sin(10 * x) ** 2)
        
        # Combine all components
        result = condition_factor * (0.3 * sin_component + 0.4 * rbf_component + 
                                    0.3 * poly_component) + global_shift + noise
        
        return result