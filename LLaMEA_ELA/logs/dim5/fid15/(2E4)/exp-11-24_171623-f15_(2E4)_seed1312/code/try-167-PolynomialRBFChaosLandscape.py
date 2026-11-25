import numpy as np

class PolynomialRBFChaosLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute polynomial chaos coefficients with higher order terms
        self.poly_coeffs = np.random.randn(dim, 8)
        # Precompute RBF centers and widths with more diverse spacing
        self.rbf_centers = np.random.uniform(-1, 1, (dim, 15))
        self.rbf_widths = 0.2 + np.random.rand(15) * 3.0
        # Spectral decomposition components with stronger conditioning
        self.eigenvals = np.sort(np.random.rand(dim) * 15 + 2)[::-1]
        self.eigenvecs = np.random.randn(dim, dim)
        self.eigenvecs, _ = np.linalg.qr(self.eigenvecs)
        # Add harmonic coupling terms for increased complexity
        self.harmonic_freqs = np.random.randint(1, 10, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial chaos expansion component with higher order terms
        poly_sum = 0.0
        for i in range(self.dim):
            for j in range(8):
                poly_sum += self.poly_coeffs[i, j] * np.polynomial.hermite.hermval(x_norm[i], [0]*j + [1])
        
        # Radial basis function component with adaptive centers and wider spread
        rbf_sum = 0.0
        for i in range(self.dim):
            for j in range(15):
                dist = np.linalg.norm(x_norm[i] - self.rbf_centers[i, j])
                rbf_sum += np.exp(-self.rbf_widths[j] * dist**2)
        
        # Spectral decomposition component with stronger conditioning
        spectral_sum = 0.0
        for i in range(self.dim):
            spectral_sum += self.eigenvals[i] * (x_norm[i] ** 2)
        
        # Cross-dimension coupling through high-frequency harmonic interactions
        cross_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = np.sin(self.harmonic_freqs[i] * np.pi * x_norm[i] + self.harmonic_freqs[j] * np.pi * x_norm[j])
                cross_sum += interaction * (x_norm[i]**2 + x_norm[j]**2)
        
        # Add quartic and quintic terms for enhanced non-convexity
        quartic_sum = 0.0
        for i in range(self.dim):
            quartic_sum += x_norm[i] ** 4
        
        quintic_sum = 0.0
        for i in range(self.dim):
            quintic_sum += x_norm[i] ** 5
        
        # Combine components with dynamic weighting
        result = 0.2 * poly_sum + 0.3 * rbf_sum + 0.25 * spectral_sum + 0.15 * cross_sum + 0.1 * quartic_sum + 0.05 * quintic_sum
        
        # Add a chaotic modulation factor based on multiple dimensions
        chaos_factor = 1.0 + 0.3 * np.sin(np.sum(x_norm) * np.pi * 2)
        
        # Apply transformation to increase non-convexity and create plateaus
        result = np.tanh(result) * (1.0 + 0.4 * np.abs(result))
        
        return result * chaos_factor