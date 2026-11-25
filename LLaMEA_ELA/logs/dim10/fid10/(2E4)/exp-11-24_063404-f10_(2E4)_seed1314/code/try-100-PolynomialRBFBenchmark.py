import numpy as np

class PolynomialRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize polynomial chaos coefficients
        self.poly_coeffs = np.random.uniform(-1.0, 1.0, dim)
        # Initialize radial basis function centers and widths
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (dim, dim))
        self.rbf_widths = np.random.uniform(0.5, 2.0, dim)
        # Sine-cosine coupling parameters
        self.coupling_freq = 2.0 * np.pi * (1 + np.arange(dim) * 0.5)
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Polynomial chaos component
        poly_term = np.sum(self.poly_coeffs * (x_norm ** 3))
        
        # Radial basis function component
        rbf_sum = 0.0
        for i in range(self.dim):
            diff = x_norm - self.rbf_centers[i]
            rbf_sum += np.exp(-np.sum(diff**2) / (2 * self.rbf_widths[i]**2))
        
        # Sine-cosine coupling term
        coupling_term = 0.0
        for i in range(self.dim):
            coupling_term += np.sin(self.coupling_freq[i] * x_norm[i]) * np.cos(self.coupling_freq[i] * x_norm[i])
        
        # Cross-dimensional interaction with chaotic modulation
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic modulation using logistic map
                logistic_mod = 1.0 / (1.0 + np.exp(-3.8 * (x_norm[i] - 0.5)))
                cross_term += logistic_mod * np.sin(self.coupling_freq[i] * x_norm[j]) * np.cos(self.coupling_freq[j] * x_norm[i])
        
        # Add a global scaling and noise component
        noise = np.sum(np.sin(13 * x_norm) * np.cos(17 * x_norm))
        
        # Combine all terms with appropriate weights
        return 0.5 * poly_term + 0.3 * rbf_sum + 0.2 * coupling_term - 0.1 * cross_term + 0.05 * noise