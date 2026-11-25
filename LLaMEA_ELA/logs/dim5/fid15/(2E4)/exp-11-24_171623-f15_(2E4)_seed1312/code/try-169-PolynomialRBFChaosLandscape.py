import numpy as np

class PolynomialRBFChaosLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute radial basis function centers and weights
        np.random.seed(42)
        self.rbf_centers = np.random.uniform(-1, 1, (dim, dim))
        self.rbf_weights = np.random.normal(0, 1, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial chaos expansion components with Hermite polynomials
        poly_sum = 0.0
        for i in range(self.dim):
            # Use third-order Hermite polynomial: H3(x) = 8x^3 - 12x
            poly_sum += self.rbf_weights[i] * (8 * x_norm[i]**3 - 12 * x_norm[i])
        
        # Radial basis functions with adaptive centers and variable widths
        rbf_sum = 0.0
        for i in range(self.dim):
            center = self.rbf_centers[i]
            # Adaptive width based on dimension and position
            width = 0.5 + 0.5 * np.abs(np.sin(i * np.pi / (self.dim + 1)))
            rbf_sum += np.exp(-np.sum((x_norm - center)**2) / (2 * width**2))
        
        # Spectral decomposition with frequency modulation
        spec_sum = 0.0
        for i in range(self.dim):
            freq_mod = 1.0 + 0.5 * np.sin(i * np.pi / (self.dim + 2))
            spec_sum += np.sin(freq_mod * x_norm[i]) * np.cos(freq_mod * x_norm[i])
        
        # Multi-scale harmonic modulation with exponential weights
        mod_sum = 0.0
        for i in range(self.dim):
            scale = 3.0**(i % 4)
            weight = 1.0 / (1.0 + np.exp(-scale))
            mod_sum += weight * np.sin(scale * x_norm[i]) * np.exp(-0.3 * x_norm[i]**2)
        
        # Cross-dimensional interaction terms with polynomial coupling
        cross_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                coupling = (x_norm[i]**2 + x_norm[j]**2) * np.sin(x_norm[i] * x_norm[j])
                cross_sum += coupling
        
        # Asymmetric basin structure with polynomial basins
        basin_sum = 0.0
        for i in range(self.dim):
            if x_norm[i] < 0:
                basin_sum += (x_norm[i]**5 + 0.3 * x_norm[i]**3) * np.exp(-x_norm[i]**2)
            else:
                basin_sum += (x_norm[i]**4 - 0.4 * x_norm[i]**2) * np.exp(-x_norm[i]**2)
        
        # Combine all components with dynamic weights
        result = 0.25 * poly_sum + 0.3 * rbf_sum + 0.2 * spec_sum + 0.15 * mod_sum + 0.1 * cross_sum + 0.05 * basin_sum
        
        # Add conditioning factor based on problem dimensionality
        condition_factor = 1.0 + 0.4 * np.log(self.dim + 1) + 0.2 * np.sum(np.abs(x_norm))
        
        return result * condition_factor * (1.0 + 0.3 * np.sum(x_norm**2))
