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
        # Global modulation parameters
        self.global_freq = 3.0
        self.global_amp = 2.0
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation and scaling
        x_transformed = self.rotation_matrix @ x * self.scales
        
        # Base quadratic term (ellipsoid)
        f_val = np.sum(x_transformed**2)
        
        # Add exponential decay terms with sinusoidal modulation
        for i in range(self.dim):
            f_val += 3.0 * np.exp(-0.5 * x_transformed[i]**2) * np.sin(self.global_freq * x_transformed[i])
            
        # Add trigonometric coupling between dimensions
        for i in range(self.dim - 1):
            f_val += 1.5 * np.sin(x_transformed[i]) * np.cos(x_transformed[i+1]) * \
                     np.exp(-0.1 * (x_transformed[i] - x_transformed[i+1])**2)
            
        # Add global sinusoidal modulation with varying amplitude
        f_val += self.global_amp * np.sin(np.sum(x_transformed) / self.dim)
        
        # Add higher-order polynomial terms with chaotic perturbations
        f_val += 0.1 * np.sum(x_transformed**6 * (1.0 + 0.3 * np.sin(7.0 * x_transformed)))
        
        # Add cross-dimensional interaction with exponential decay
        for i in range(self.dim - 2):
            f_val += 0.5 * np.exp(-0.5 * (x_transformed[i] + x_transformed[i+1])**2) * \
                     np.sin(2.0 * x_transformed[i+2])
            
        # Add small constant to ensure positive fitness values
        f_val += 0.5
        
        return f_val