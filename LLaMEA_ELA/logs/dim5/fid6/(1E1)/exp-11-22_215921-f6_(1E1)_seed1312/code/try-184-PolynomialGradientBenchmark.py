import numpy as np

class PolynomialGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute polynomial chaos coefficients for dimensionality
        self.poly_coeffs = np.random.randn(dim, 5) * 0.5
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial chaos expansion component
        poly_expansion = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Use Legendre polynomials up to degree 4
            poly_vals = np.array([1, xi, 2*xi**2 - 1, 4*xi**3 - 3*xi, 8*xi**4 - 8*xi**2 + 1])
            poly_expansion += np.dot(self.poly_coeffs[i], poly_vals)
        
        # Adaptive gradient field with dynamic step sizes
        grad_field = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Dynamic step size based on position
            step_size = 1.0 + 0.5 * np.sin(xi * np.pi)
            # Gradient component with sine modulation
            grad_field += step_size * np.sin(3 * xi) * np.cos(2 * xi)
        
        # Spectral clustering attraction basins with dynamic centers
        basin_term = 0.0
        num_centers = max(1, self.dim // 3)
        for c in range(num_centers):
            center = np.random.uniform(-1, 1, self.dim)
            # Distance to center with adaptive weighting
            dist = np.linalg.norm(x_norm - center)
            weight = 1.0 / (1.0 + dist**2)
            basin_term += weight * np.exp(-dist**2 / 2.0)
        
        # Coupling between dimensions using a chaotic sine map
        coupling = 0.0
        for i in range(self.dim - 1):
            xi = x_norm[i]
            xi1 = x_norm[i + 1]
            # Chaotic coupling with sine map dynamics
            coupling += np.sin(xi * xi1 * 3.0) * np.cos(xi + xi1)
        
        # High-frequency oscillatory component with dynamic frequency
        oscillation = 0.0
        for i in range(self.dim):
            freq = 5.0 + 2.0 * np.sin(i * np.pi / self.dim)
            oscillation += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i] * 0.5)
        
        # Dimension-dependent conditioning factor with fractal-like scaling
        condition_factor = 1.0 + 0.3 * np.sin(self.dim * np.pi / 6.0) + 0.2 * np.log(self.dim + 1)
        
        # Combine all components
        return condition_factor * (poly_expansion + grad_field + basin_term + coupling + oscillation)