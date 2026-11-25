import numpy as np

class RadialPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize radial basis function centers and widths
        self.rbf_centers = np.random.uniform(-4.0, 4.0, (dim, 7))  # More RBFs per dimension
        self.rbf_widths = np.random.uniform(0.3, 2.5, (dim, 7))
        # Initialize polynomial drift coefficients for each dimension (higher order)
        self.drift_coeffs = np.random.uniform(-1.5, 1.5, (dim, 6))  # Quintic drift per dimension
        # Initialize coupling weights between dimensions with trigonometric components
        self.coupling_weights = np.random.uniform(-0.8, 0.8, (dim, dim))
        self.coupling_trig_coeffs = np.random.uniform(-0.5, 0.5, (dim, dim))
        np.fill_diagonal(self.coupling_weights, 0)
        np.fill_diagonal(self.coupling_trig_coeffs, 0)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component
        rbf_sum = 0.0
        for i in range(self.dim):
            for j in range(7):  # More RBFs per dimension
                center = self.rbf_centers[i, j]
                width = self.rbf_widths[i, j]
                rbf_sum += np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Polynomial drift component (higher order)
        drift = 0.0
        for i in range(self.dim):
            x_i = x[i]
            poly_term = (self.drift_coeffs[i, 0] + 
                        self.drift_coeffs[i, 1] * x_i + 
                        self.drift_coeffs[i, 2] * x_i**2 + 
                        self.drift_coeffs[i, 3] * x_i**3 +
                        self.drift_coeffs[i, 4] * x_i**4 +
                        self.drift_coeffs[i, 5] * x_i**5)
            drift += poly_term
        
        # Coupling component with trigonometric interactions and adaptive scaling
        coupling = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    # Gradient-like interaction between dimensions
                    coupling += self.coupling_weights[i, j] * (x[i] - x[j])**2
                    # Trigonometric interaction component
                    coupling += self.coupling_trig_coeffs[i, j] * np.sin(0.5 * (x[i] - x[j]))
        
        # Adaptive scaling factor based on dimensionality
        adaptive_scale = 1.0 + 0.1 * np.log(self.dim + 1)
        
        # Combine components with different weights and adaptive scaling
        result = 2.0 * rbf_sum + 1.5 * drift + 1.2 * coupling * adaptive_scale
        
        return result