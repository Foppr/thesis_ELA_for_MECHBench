import numpy as np

class PolynomialRBFChaosBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate random coefficients for polynomial chaos expansion
        self.poly_coeffs = np.random.uniform(-1.0, 1.0, (dim, 5))
        # Radial basis function centers and widths
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (dim, 10))
        self.rbf_widths = np.random.uniform(0.5, 2.0, (10,))
        # Sine-wave coupling parameters
        self.coupling_freqs = np.random.uniform(1.0, 5.0, dim)
        self.coupling_ampls = np.random.uniform(0.5, 2.0, dim)
        # Additional adaptive scaling factors
        self.adaptive_scales = np.random.uniform(0.5, 1.5, dim)
        
    def f(self, x):
        x_norm = x / 5.0
        f_val = 0.0
        
        # Polynomial chaos expansion component with adaptive scaling
        for i in range(self.dim):
            poly_term = 0.0
            for j in range(5):
                poly_term += self.poly_coeffs[i, j] * np.power(x_norm[i], j)
            f_val += 0.2 * np.abs(poly_term)**1.5 * self.adaptive_scales[i]
        
        # Radial basis function component with enhanced nonlinearity
        for i in range(self.dim):
            rbf_sum = 0.0
            for j in range(10):
                rbf_sum += self.rbf_widths[j] * np.exp(-0.5 * np.sum((x_norm[i] - self.rbf_centers[i, j])**2))
            f_val += 0.3 * (rbf_sum**2 + 0.1 * rbf_sum**3)
        
        # Sine-wave coupling between dimensions with higher-order harmonics
        for i in range(self.dim):
            coupling_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling_sum += self.coupling_ampls[i] * np.sin(self.coupling_freqs[i] * x_norm[j])
            f_val += 0.15 * (coupling_sum**2 + 0.05 * coupling_sum**4)
        
        # Multi-scale harmonic components with varying amplitudes
        scale_factors = [0.1, 0.3, 0.7, 1.0]
        for k, scale in enumerate(scale_factors):
            harmonic_sum = 0.0
            for i in range(self.dim):
                harmonic_sum += np.sin(scale * 2.0 * np.pi * x_norm[i]) * np.cos(scale * 3.0 * np.pi * x_norm[i])
            f_val += 0.1 * (harmonic_sum**2 + 0.02 * harmonic_sum**4)
        
        # Enhanced noise-like perturbations with multiple frequency components
        noise_pert = 0.05 * np.sum(
            np.sin(7.0 * x_norm) + 
            np.cos(4.0 * x_norm) + 
            np.tan(2.0 * x_norm) + 
            0.3 * np.sin(11.0 * x_norm)**2 + 
            0.2 * np.cos(9.0 * x_norm)**2
        )
        f_val += noise_pert
        
        # Add cross-dimensional interaction terms for increased complexity
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(x_norm[i] * x_norm[j]) * (i + j)
        f_val += 0.1 * cross_term**2
        
        return f_val