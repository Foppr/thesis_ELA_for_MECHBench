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
        
    def f(self, x):
        x_norm = x / 5.0
        f_val = 0.0
        
        # Polynomial chaos expansion component
        for i in range(self.dim):
            poly_term = 0.0
            for j in range(5):
                poly_term += self.poly_coeffs[i, j] * np.power(x_norm[i], j)
            f_val += 0.2 * np.abs(poly_term)**1.5
        
        # Radial basis function component
        for i in range(self.dim):
            rbf_sum = 0.0
            for j in range(10):
                rbf_sum += self.rbf_widths[j] * np.exp(-0.5 * np.sum((x_norm[i] - self.rbf_centers[i, j])**2))
            f_val += 0.3 * rbf_sum**2
        
        # Sine-wave coupling between dimensions
        for i in range(self.dim):
            coupling_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling_sum += self.coupling_ampls[i] * np.sin(self.coupling_freqs[i] * x_norm[j])
            f_val += 0.15 * coupling_sum**2
        
        # Add multi-scale harmonic components
        for scale in [0.1, 0.3, 0.7, 1.0]:
            harmonic_sum = 0.0
            for i in range(self.dim):
                harmonic_sum += np.sin(scale * 2.0 * np.pi * x_norm[i]) * np.cos(scale * 3.0 * np.pi * x_norm[i])
            f_val += 0.1 * harmonic_sum**2
        
        # Add noise-like perturbations with varying intensity
        noise_pert = 0.05 * np.sum(np.sin(7.0 * x_norm) + np.cos(4.0 * x_norm) + np.tan(2.0 * x_norm))
        f_val += noise_pert
        
        return f_val