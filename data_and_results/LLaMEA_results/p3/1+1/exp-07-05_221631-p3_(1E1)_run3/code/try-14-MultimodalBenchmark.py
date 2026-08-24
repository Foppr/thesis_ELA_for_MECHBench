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
        # Gaussian centers and variances for RBF components
        self.centers = np.random.uniform(-5.0, 5.0, (10, dim))
        self.variances = np.random.uniform(0.5, 2.0, 10)
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation and scaling
        x_transformed = self.rotation_matrix @ x * self.scales
        
        # Base polynomial chaos term (sum of powers with alternating signs)
        f_val = np.sum(x_transformed**2) - 0.5 * np.sum(x_transformed**3) + 0.1 * np.sum(x_transformed**4)
        
        # Add Gaussian radial basis functions
        rbf_sum = 0.0
        for i in range(10):
            diff = x_transformed - self.centers[i]
            rbf_sum += np.exp(-np.sum(diff**2) / (2 * self.variances[i]**2))
        f_val += 2.0 * rbf_sum
        
        # Add cross-dimensional coupling with trigonometric terms
        coupling = 0.0
        for i in range(self.dim - 1):
            coupling += np.sin(2.0 * x_transformed[i]) * np.cos(3.0 * x_transformed[i+1]) + \
                       np.cos(4.0 * x_transformed[i]) * np.sin(5.0 * x_transformed[i+1])
        f_val += 0.5 * coupling
        
        # Add a quartic term for increased complexity
        f_val += 0.05 * np.sum(x_transformed**4)
        
        # Add stochastic noise with varying amplitude
        noise = np.random.normal(0, 0.1, self.dim)
        f_val += np.sum(noise * x_transformed)
        
        # Add a small constant to ensure positive fitness values
        f_val += 0.1
        
        return f_val