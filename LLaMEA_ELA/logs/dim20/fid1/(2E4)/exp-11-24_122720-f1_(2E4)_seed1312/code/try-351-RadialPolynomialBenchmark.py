import numpy as np

class RadialPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize radial basis function centers and widths
        self.rbf_centers = np.random.uniform(-4.0, 4.0, (dim, 5))  # 5 RBFs per dimension
        self.rbf_widths = np.random.uniform(0.5, 2.0, (dim, 5))
        # Initialize polynomial drift coefficients for each dimension
        self.drift_coeffs = np.random.uniform(-1.0, 1.0, (dim, 4))  # Cubic drift per dimension
        # Initialize coupling weights between dimensions
        self.coupling_weights = np.random.uniform(-0.5, 0.5, (dim, dim))
        np.fill_diagonal(self.coupling_weights, 0)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component
        rbf_sum = 0.0
        for i in range(self.dim):
            for j in range(5):  # 5 RBFs per dimension
                center = self.rbf_centers[i, j]
                width = self.rbf_widths[i, j]
                rbf_sum += np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Polynomial drift component
        drift = 0.0
        for i in range(self.dim):
            x_i = x[i]
            poly_term = (self.drift_coeffs[i, 0] + 
                        self.drift_coeffs[i, 1] * x_i + 
                        self.drift_coeffs[i, 2] * x_i**2 + 
                        self.drift_coeffs[i, 3] * x_i**3)
            drift += poly_term
        
        # Coupling component based on gradient-like interactions
        coupling = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    # Gradient-like interaction between dimensions
                    coupling += self.coupling_weights[i, j] * (x[i] - x[j])**2
        
        # Combine components with different weights
        result = 1.5 * rbf_sum + 1.0 * drift + 0.8 * coupling
        
        return result