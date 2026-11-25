import numpy as np

class PolynomialChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize polynomial chaos parameters with more variation
        self.poly_orders = 3 + np.random.randint(0, 4, dim)
        self.rbf_centers = np.random.uniform(-1.5, 1.5, (dim, dim))
        self.rbf_widths = 0.3 + 2.0 * np.random.rand(dim)
        self.conditioning_factors = 0.5 + 3.0 * np.random.rand(dim)
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Polynomial chaos component with varying orders and enhanced nonlinearity
        poly_component = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            order = self.poly_orders[i]
            poly_component += np.sum([np.sin((j+1) * xi) * (xi**(order + 1)) for j in range(order)])
        
        # Radial basis function component with adaptive widths and enhanced interaction
        rbf_component = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            for j in range(self.dim):
                center = self.rbf_centers[i, j]
                width = self.rbf_widths[j]
                rbf_component += np.exp(-width * (xi - center)**2) * np.sin(xi * center)
        
        # Cross-dimensional coupling with adaptive conditioning and enhanced interaction
        coupling_component = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            for j in range(i+1, self.dim):
                xj = x_scaled[j]
                cond_factor = self.conditioning_factors[i] * self.conditioning_factors[j]
                coupling_component += np.sin(xi * xj) * cond_factor * np.cos(xi + xj)
        
        # Enhanced chaotic modulation with multiple frequency components
        adaptive_component = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            # Chaotic modulation using multiple sine and cosine with varying frequencies
            freq1 = 1.0 + 0.3 * np.sin(i * np.pi / (self.dim + 1))
            freq2 = 1.5 + 0.7 * np.cos(i * np.pi / (self.dim + 2))
            adaptive_component += np.sin(freq1 * xi) * np.cos(freq2 * xi**2) * np.sin(xi * freq1)
        
        # High-frequency oscillatory component with multiple interacting frequencies
        oscillatory_component = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            oscillatory_component += np.sin(15 * xi + np.sin(7 * xi)) * np.cos(12 * xi + np.cos(4 * xi)) * np.sin(9 * xi)
        
        # Additional harmonic coupling component
        harmonic_component = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            harmonic_component += np.sum([np.sin((j+1) * xi**2) * np.cos((j+1) * xi) for j in range(3)])
        
        # Combine all components with different weights and add noise
        return 0.2 * poly_component + 0.25 * rbf_component + 0.15 * coupling_component + 0.2 * adaptive_component + 0.15 * oscillatory_component + 0.05 * harmonic_component