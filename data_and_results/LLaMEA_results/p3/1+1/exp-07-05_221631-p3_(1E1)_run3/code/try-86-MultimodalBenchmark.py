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
        # Parameters for the composite landscape
        self.poly_degree = 4
        self.oscillation_freq = 3.0
        self.symmetry_factor = 2.0
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Apply rotation and scaling
        x_transformed = self.rotation_matrix @ x * self.scales
        
        # Radial term with polynomial scaling
        r_squared = np.sum(x_transformed**2)
        radial_term = r_squared**self.poly_degree
        
        # Trigonometric oscillations with radial dependence
        oscillation_term = 0.0
        for i in range(self.dim):
            oscillation_term += np.sin(self.oscillation_freq * x_transformed[i]) * \
                               np.cos(self.symmetry_factor * x_transformed[i])
        
        # Cross-dimensional polynomial interactions
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction_term += (x_transformed[i] * x_transformed[j])**2 * \
                                   np.sin(0.5 * (x_transformed[i] + x_transformed[j]))
        
        # Add a radial modulation to create multiple valleys
        modulation = 1.0 + 0.5 * np.sin(2.0 * np.sqrt(r_squared))
        
        # Combine all terms
        f_val = radial_term + oscillation_term + interaction_term * modulation
        
        # Add a small constant to ensure positive fitness values
        f_val += 0.1
        
        return f_val