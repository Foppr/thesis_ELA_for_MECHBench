import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrix for added complexity
        np.random.seed(42)  # For reproducibility
        self.rotation_matrix = np.random.randn(dim, dim)
        self.rotation_matrix, _ = np.linalg.qr(self.rotation_matrix)
        # Additional random scaling for each dimension
        self.scales = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation and scaling
        x_transformed = self.rotation_matrix @ x * self.scales
        
        # Base quadratic term (ellipsoid)
        f_val = np.sum(x_transformed**2)
        
        # Add highly oscillatory sinusoidal perturbations
        for i in range(self.dim):
            f_val += 2.0 * np.sin(3.0 * x_transformed[i]) * np.cos(2.0 * x_transformed[i]) + \
                     1.5 * np.sin(5.0 * x_transformed[i]) * np.cos(4.0 * x_transformed[i])
            
        # Add complex interaction terms between dimensions
        for i in range(self.dim - 2):
            f_val += 0.3 * x_transformed[i] * x_transformed[i+1] * x_transformed[i+2] * \
                     (np.sin(0.5 * x_transformed[i]) + np.cos(0.7 * x_transformed[i+1]))
            
        # Add a quartic and quintic term for additional complexity
        f_val += 0.02 * np.sum(x_transformed**4) + 0.005 * np.sum(x_transformed**5)
        
        # Add stochastic noise to increase ruggedness
        noise = np.random.normal(0, 0.1, self.dim)
        f_val += np.sum(noise * x_transformed)
        
        return f_val