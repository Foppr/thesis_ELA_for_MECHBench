import numpy as np

class RadialPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize radial basis function centers and widths with more variation
        self.rbf_centers = np.random.uniform(-4.5, 4.5, (dim, 7))  # 7 RBFs per dimension for higher complexity
        self.rbf_widths = np.random.uniform(0.3, 2.5, (dim, 7))
        # Initialize polynomial drift coefficients with higher order terms
        self.drift_coeffs = np.random.uniform(-1.5, 1.5, (dim, 6))  # Quintic drift per dimension
        # Initialize coupling weights with more complex structure
        self.coupling_weights = np.random.uniform(-0.8, 0.8, (dim, dim))
        np.fill_diagonal(self.coupling_weights, 0)
        # Add a global scaling factor for better control of landscape complexity
        self.global_scale = 2.0
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced radial basis function component with more complex interaction
        rbf_sum = 0.0
        for i in range(self.dim):
            for j in range(7):  # 7 RBFs per dimension
                center = self.rbf_centers[i, j]
                width = self.rbf_widths[i, j]
                # Add a multiplicative factor to increase sensitivity
                rbf_sum += np.exp(-0.5 * ((x[i] - center) / width)**2) * (1.0 + 0.2 * np.sin(x[i]))
        
        # Enhanced polynomial drift component with higher order terms
        drift = 0.0
        for i in range(self.dim):
            x_i = x[i]
            # Include more polynomial terms for complexity
            poly_term = (self.drift_coeffs[i, 0] + 
                        self.drift_coeffs[i, 1] * x_i + 
                        self.drift_coeffs[i, 2] * x_i**2 + 
                        self.drift_coeffs[i, 3] * x_i**3 +
                        self.drift_coeffs[i, 4] * x_i**4 +
                        self.drift_coeffs[i, 5] * x_i**5)
            drift += poly_term
        
        # Enhanced coupling component with adaptive interaction
        coupling = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    # Adaptive gradient-like interaction with non-linear coupling
                    diff = x[i] - x[j]
                    coupling += self.coupling_weights[i, j] * (diff**2 + 0.1 * diff**4)
        
        # Add a sine modulation to create more complex landscape features
        modulator = 1.0 + 0.3 * np.sin(np.sum(x)**2)
        
        # Combine components with different weights and global scaling
        result = self.global_scale * (1.2 * rbf_sum + 0.8 * drift + 0.6 * coupling) * modulator
        
        return result