import numpy as np

class PolynomialChaosBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute quaternion-like weights for cross-dimensional coupling
        self.weights = np.array([np.sin(i * np.pi / (dim + 1)) for i in range(dim)])
        # Precompute radial basis function centers and widths
        self.centers = np.random.uniform(-3.0, 3.0, (10, dim))
        self.widths = np.random.uniform(0.5, 2.0, 10)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial term with adaptive exponents
        f1 = np.sum(x**4 + 0.5 * x**3 + 0.2 * x**2)
        
        # Polynomial chaos expansion component with Hermite polynomials
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            f2 += (xi**3 - 3*xi) * self.weights[i]  # Third-order Hermite polynomial
        
        # Radial basis function component with multiple centers
        rbf = 0.0
        for i in range(10):
            diff = x - self.centers[i]
            rbf += np.exp(-np.sum(diff**2) / (2 * self.widths[i]**2))
        f3 = 0.8 * rbf
        
        # Quaternion-inspired cross-dimensional interaction
        quat_interaction = 0.0
        for i in range(self.dim - 1):
            j = (i + 1) % self.dim
            quat_interaction += x[i] * x[j] * np.sin(x[i] + x[j])
        f4 = 0.3 * quat_interaction
        
        # Multi-scale polynomial with exponential modulation
        poly_exp = 0.0
        for i in range(self.dim):
            poly_exp += (x[i]**6) * np.exp(-x[i]**2 / 10.0)
        f5 = 0.25 * poly_exp
        
        # Fractional dimensional coupling with cosine modulation
        frac_coupling = 0.0
        for i in range(self.dim - 1):
            frac_coupling += (1.0 / (i + 1)) * np.cos(x[i] * x[i+1])
        f6 = 0.2 * frac_coupling
        
        # Spherical harmonic component with degree 4
        r = np.sqrt(np.sum(x**2))
        if r > 1e-8:
            theta = np.arccos(x[0] / r) if self.dim > 1 else 0.0
            phi = np.arctan2(x[1], x[0]) if self.dim > 2 else 0.0
            spherical_harm = np.sin(4 * theta) * np.cos(4 * phi)
            f7 = 0.15 * r * spherical_harm
        else:
            f7 = 0.0
        
        # Mixed polynomial-exponential term with adaptive coefficients
        mixed_term = 0.0
        for i in range(self.dim):
            mixed_term += (x[i]**2) * np.exp(-x[i]**2 / 5.0)
        f8 = 0.3 * mixed_term
        
        # Cross-dimensional polynomial interaction with permutation symmetry
        cross_poly = 0.0
        for i in range(self.dim - 2):
            j, k = (i + 1) % self.dim, (i + 2) % self.dim
            cross_poly += x[i] * x[j] * x[k]
        f9 = 0.2 * cross_poly**2
        
        # Logarithmic polynomial component
        log_poly = 0.0
        for i in range(self.dim):
            log_poly += np.log(1.0 + np.abs(x[i])) * x[i]**3
        f10 = 0.18 * log_poly
        
        # Combined scaling factor
        scale_factor = 1.0 + 0.2 * np.sin(self.dim)
        
        # Final combined function
        return scale_factor * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10)