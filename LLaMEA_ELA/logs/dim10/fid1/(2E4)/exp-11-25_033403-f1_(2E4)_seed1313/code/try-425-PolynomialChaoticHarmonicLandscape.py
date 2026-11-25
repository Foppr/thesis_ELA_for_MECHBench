import numpy as np

class PolynomialChaoticHarmonicLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize polynomial exponents and coefficients
        self.poly_exponents = np.random.uniform(2.0, 6.0, dim)
        self.poly_coeffs = np.random.uniform(0.5, 2.5, dim)
        # Initialize chaotic logistic map parameters
        self.logistic_r = np.random.uniform(3.5, 4.0, dim)
        self.logistic_x = np.random.uniform(0.1, 0.9, dim)
        # Initialize spherical harmonic components
        self.sph_harm_l = np.random.randint(1, 4, dim)
        self.sph_harm_m = np.random.randint(-3, 4, dim)
        # Initialize dynamic conditioning factors
        self.dynamic_factors = np.random.uniform(0.2, 1.0, dim)
        # Initialize cross-dimensional coupling matrix
        self.coupling_matrix = np.random.uniform(-0.3, 0.3, (dim, dim))
        # Initialize phase shifts for harmonic components
        self.phase_shifts = np.random.uniform(0, 2*np.pi, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Compute polynomial potential components
        poly_terms = 0.0
        for j in range(self.dim):
            poly_term = self.poly_coeffs[j] * (x[j] ** self.poly_exponents[j])
            poly_terms += poly_term
        
        # Compute chaotic logistic map components
        logistic_terms = 0.0
        for j in range(self.dim):
            self.logistic_x[j] = self.logistic_r[j] * self.logistic_x[j] * (1.0 - self.logistic_x[j])
            logistic_terms += self.logistic_x[j] * np.sin(x[j])
        
        # Compute spherical harmonic components
        sph_harm_terms = 0.0
        for j in range(self.dim):
            r = np.sqrt(x[j]**2 + 1e-8)
            theta = np.arctan2(x[j], 1.0) if x[j] != 0 else 0.0
            # Simplified spherical harmonic approximation
            sph_harm_term = (self.sph_harm_l[j] * np.cos(self.sph_harm_m[j] * theta) + 
                           self.sph_harm_m[j] * np.sin(self.sph_harm_m[j] * theta))
            sph_harm_terms += sph_harm_term
        
        # Compute dynamic conditioning terms
        cond_terms = 0.0
        for j in range(self.dim):
            cond_terms += self.dynamic_factors[j] * (x[j]**2) * np.cos(2.0 * x[j])
        
        # Compute cross-dimensional coupling terms
        coupling_terms = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_terms += self.coupling_matrix[i, j] * x[i] * np.sin(x[j])
        
        # Combine all components with appropriate weights
        total = 0.7 * poly_terms + 0.5 * logistic_terms + 0.4 * sph_harm_terms + 0.3 * cond_terms + 0.2 * coupling_terms
        
        return total