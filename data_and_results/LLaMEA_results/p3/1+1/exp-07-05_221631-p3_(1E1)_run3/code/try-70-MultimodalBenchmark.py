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
        # Parameters for radial basis functions
        self.num_centers = 10
        self.centers = np.random.uniform(-5.0, 5.0, (self.num_centers, dim))
        self.weights = np.random.uniform(0.5, 2.0, self.num_centers)
        # Interference parameters
        self.interference_strength = 1.5
        self.interference_frequency = 3.0
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation and scaling
        x_transformed = self.rotation_matrix @ x * self.scales
        
        # Radial basis function component
        f_val = 0.0
        for i in range(self.num_centers):
            center = self.centers[i]
            dist = np.sum((x_transformed - center)**2)
            f_val += self.weights[i] * np.exp(-0.5 * dist)
        
        # Add periodic interference terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Cross-dimensional interference with periodic modulation
                interference = self.interference_strength * np.sin(
                    self.interference_frequency * (x_transformed[i] + x_transformed[j])
                )
                f_val += interference * (x_transformed[i]**2 + x_transformed[j]**2)
        
        # Add a quartic perturbation with chaotic modulation
        f_val += 0.1 * np.sum((x_transformed**4) * (1.0 + 0.3 * np.sin(7.0 * x_transformed)))
        
        # Add a small constant to ensure positive fitness values
        f_val += 0.5
        
        return f_val