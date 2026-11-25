import numpy as np

class PolynomialRBFChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize parameters for polynomial chaos and RBF components
        self.poly_degree = 4
        self.rbf_centers = np.random.uniform(-1, 1, (dim, dim))
        self.rbf_widths = np.random.uniform(0.5, 2.0, dim)
        self.sin_freqs = np.random.uniform(1, 8, dim)
        self.chaos_params = np.random.uniform(3.5, 4.0, dim)
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Polynomial chaos component (multivariate polynomial)
        poly_sum = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            for d in range(1, self.poly_degree + 1):
                poly_sum += (xi ** d) * np.sin(d * np.pi / (self.dim + 1))
        
        # Radial Basis Function component with varying widths
        rbf_sum = 0.0
        for i in range(self.dim):
            center = self.rbf_centers[i]
            width = self.rbf_widths[i]
            diff = x_scaled - center
            rbf_sum += np.exp(-0.5 * np.sum(diff**2) / (width**2))
        
        # Sinusoidal modulation component with chaotic frequency coupling
        sin_sum = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            freq = self.sin_freqs[i] * (1 + 0.3 * np.sin(self.chaos_params[i] * xi))
            sin_sum += np.sin(freq * xi) * np.cos(freq * xi)
        
        # Cross-dimensional coupling with chaotic interaction
        cross_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                diff = x_scaled[i] - x_scaled[j]
                cross_sum += np.sin(5 * diff) * np.exp(-0.1 * abs(diff))
        
        # Combine components with dimensionality-adaptive weights
        dim_factor = 1.0 + 0.3 * np.log(self.dim + 1)
        return dim_factor * (0.4 * poly_sum + 0.3 * rbf_sum + 
                           0.2 * sin_sum + 0.1 * cross_sum)