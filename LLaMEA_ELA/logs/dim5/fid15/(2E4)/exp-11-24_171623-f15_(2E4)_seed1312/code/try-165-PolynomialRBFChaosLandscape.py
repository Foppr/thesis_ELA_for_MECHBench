import numpy as np

class PolynomialRBFChaosLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute polynomial chaos coefficients
        self.poly_coeffs = np.random.randn(dim, 5)
        # Precompute RBF centers and widths
        self.rbf_centers = np.random.uniform(-1, 1, (dim, 10))
        self.rbf_widths = 0.5 + np.random.rand(10) * 2.0
        # Spectral decomposition components
        self.eigenvals = np.sort(np.random.rand(dim) * 10 + 1)[::-1]
        self.eigenvecs = np.random.randn(dim, dim)
        self.eigenvecs, _ = np.linalg.qr(self.eigenvecs)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial chaos expansion component
        poly_sum = 0.0
        for i in range(self.dim):
            for j in range(5):
                poly_sum += self.poly_coeffs[i, j] * np.polynomial.hermite.hermval(x_norm[i], [0]*j + [1])
        
        # Radial basis function component with adaptive centers
        rbf_sum = 0.0
        for i in range(self.dim):
            for j in range(10):
                dist = np.linalg.norm(x_norm[i] - self.rbf_centers[i, j])
                rbf_sum += np.exp(-self.rbf_widths[j] * dist**2)
        
        # Spectral decomposition component
        spectral_sum = 0.0
        for i in range(self.dim):
            spectral_sum += self.eigenvals[i] * (x_norm[i] ** 2)
        
        # Cross-dimension coupling through sine interactions
        cross_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = np.sin(np.pi * (x_norm[i] + x_norm[j]))
                cross_sum += interaction * (x_norm[i]**2 + x_norm[j]**2)
        
        # Combine components with dynamic weighting
        result = 0.3 * poly_sum + 0.4 * rbf_sum + 0.2 * spectral_sum + 0.1 * cross_sum
        
        # Add a chaotic modulation factor based on dimension
        chaos_factor = 1.0 + 0.2 * np.sin(np.sum(x_norm) * np.pi)
        
        # Apply transformation to increase non-convexity and create plateaus
        result = np.tanh(result) * (1.0 + 0.3 * np.abs(result))
        
        return result * chaos_factor