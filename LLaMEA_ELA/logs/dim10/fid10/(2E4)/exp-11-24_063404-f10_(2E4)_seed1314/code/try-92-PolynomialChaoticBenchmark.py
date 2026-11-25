import numpy as np

class PolynomialChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize polynomial chaos parameters
        self.poly_orders = 2 + np.random.randint(0, 3, dim)
        self.rbf_centers = np.random.uniform(-1, 1, (dim, dim))
        self.rbf_widths = 0.5 + 1.5 * np.random.rand(dim)
        self.conditioning_factors = 1.0 + 2.0 * np.random.rand(dim)
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Polynomial chaos component with varying orders
        poly_component = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            order = self.poly_orders[i]
            poly_component += np.sum([np.sin((j+1) * xi) * (xi**order) for j in range(order)])
        
        # Radial basis function component with adaptive widths
        rbf_component = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            for j in range(self.dim):
                center = self.rbf_centers[i, j]
                width = self.rbf_widths[j]
                rbf_component += np.exp(-width * (xi - center)**2)
        
        # Cross-dimensional coupling with adaptive conditioning
        coupling_component = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            for j in range(i+1, self.dim):
                xj = x_scaled[j]
                cond_factor = self.conditioning_factors[i] * self.conditioning_factors[j]
                coupling_component += np.sin(xi * xj) * cond_factor
        
        # Adaptive conditioning with chaotic modulation
        adaptive_component = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            # Chaotic modulation using sine and cosine with varying frequencies
            freq = 1.0 + 0.5 * np.sin(i * np.pi / (self.dim + 1))
            adaptive_component += np.sin(freq * xi) * np.cos(freq * xi**2)
        
        # High-frequency oscillatory component
        oscillatory_component = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            oscillatory_component += np.sin(10 * xi + np.sin(5 * xi)) * np.cos(8 * xi + np.cos(3 * xi))
        
        # Combine all components with different weights
        return 0.25 * poly_component + 0.3 * rbf_component + 0.2 * coupling_component + 0.15 * adaptive_component + 0.1 * oscillatory_component