import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrix for added complexity
        np.random.seed(42)  # For reproducibility
        self.rotation_matrix = np.random.randn(dim, dim)
        self.rotation_matrix, _ = np.linalg.qr(self.rotation_matrix)
        # Adaptive condition numbers for each dimension
        self.condition_numbers = np.random.uniform(1.0, 100.0, dim)
        # Harmonic interaction coefficients
        self.harmonic_coeffs = np.random.uniform(0.5, 2.0, dim)
        # RBF centers and widths
        self.centers = np.random.uniform(-5.0, 5.0, (10, dim))
        self.widths = np.random.uniform(0.5, 3.0, 10)
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation
        x_rotated = self.rotation_matrix @ x
        
        # Radial basis function component
        rbf_sum = 0.0
        for i in range(10):
            diff = x_rotated - self.centers[i]
            rbf_sum += np.exp(-np.sum((diff**2) / (2 * self.widths[i]**2)))
        
        # Adaptive condition number weighted quadratic term
        weighted_quad = np.sum((x_rotated**2) * self.condition_numbers)
        
        # Cross-dimensional harmonic interactions
        harmonic_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                harmonic_interaction += self.harmonic_coeffs[i] * self.harmonic_coeffs[j] * \
                                       np.sin(2.0 * x_rotated[i]) * np.cos(3.0 * x_rotated[j])
        
        # Add perturbed quartic term with chaotic modulation
        quartic_term = 0.05 * np.sum((x_rotated**4) * (1.0 + 0.3 * np.sin(7.0 * x_rotated)))
        
        # Combine all components
        f_val = rbf_sum + weighted_quad + harmonic_interaction + quartic_term
        
        # Add small constant to ensure positive fitness values
        f_val += 0.1
        
        return f_val