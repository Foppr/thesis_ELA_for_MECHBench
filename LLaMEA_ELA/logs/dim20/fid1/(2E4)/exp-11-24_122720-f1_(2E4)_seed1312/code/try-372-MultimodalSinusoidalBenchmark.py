import numpy as np

class MultimodalSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize radial basis function centers and widths
        self.rbf_centers = np.random.uniform(-4.0, 4.0, (10, dim))
        self.rbf_widths = np.random.uniform(0.5, 2.0, (10,))
        # Initialize sinusoidal parameters
        self.sin_freq = np.random.uniform(1.0, 5.0, dim)
        self.sin_amp = np.random.uniform(0.5, 2.0, dim)
        # Initialize polynomial coefficients for coupling
        self.poly_coeffs = np.random.normal(0.0, 1.0, (dim, 4))
        # Initialize interaction matrix
        self.interaction_matrix = np.random.uniform(-1.0, 1.0, (dim, dim))
        np.fill_diagonal(self.interaction_matrix, 0)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component
        rbf_sum = 0
        for i in range(10):
            rbf_term = 0
            for j in range(self.dim):
                diff = x[j] - self.rbf_centers[i, j]
                rbf_term += diff**2
            rbf_sum += np.exp(-0.5 * rbf_term / (self.rbf_widths[i]**2))
        
        # Sinusoidal component
        sin_sum = 0
        for i in range(self.dim):
            sin_sum += self.sin_amp[i] * np.sin(self.sin_freq[i] * x[i])
        
        # Polynomial coupling component
        poly_sum = 0
        for i in range(self.dim):
            x_i = x[i]
            poly_term = (self.poly_coeffs[i, 0] + 
                        self.poly_coeffs[i, 1] * x_i + 
                        self.poly_coeffs[i, 2] * x_i**2 + 
                        self.poly_coeffs[i, 3] * x_i**3)
            poly_sum += poly_term
        
        # Cross-dimension interaction with sinusoidal coupling
        interaction = 0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    interaction += self.interaction_matrix[i, j] * np.sin(x[i]) * x[j]**2
        
        # Combine all components
        result = (1.5 * rbf_sum + 
                 1.0 * sin_sum + 
                 0.8 * poly_sum + 
                 0.6 * interaction)
        
        return result