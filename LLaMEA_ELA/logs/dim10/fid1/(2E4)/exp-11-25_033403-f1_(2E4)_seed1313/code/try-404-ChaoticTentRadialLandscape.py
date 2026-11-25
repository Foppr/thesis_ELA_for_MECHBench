import numpy as np

class ChaoticTentRadialLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic tent map parameters
        self.tent_params = np.random.uniform(1.1, 1.9, dim)
        # Initialize polynomial potential coefficients
        self.poly_coeffs = np.random.uniform(-2.0, 2.0, (3, dim))
        # Initialize radial basis functions with random centers and variances
        self.rbf_centers = np.random.uniform(-4.5, 4.5, (5, dim))
        self.rbf_vars = np.random.uniform(0.3, 1.8, (5, dim))
        self.rbf_weights = np.random.uniform(0.8, 2.2, 5)
        # Initialize dynamic conditioning parameters
        self.conditioning_params = np.random.uniform(0.5, 1.5, dim)
        # Initialize cross-dimensional coupling matrix with modified weights
        self.coupling_matrix = np.random.uniform(-0.3, 0.3, (dim, dim))
        # Initialize chaotic modulation factors
        self.chaos_factors = np.random.uniform(0.1, 0.5, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Compute chaotic tent map components
        tent_terms = 0.0
        for j in range(self.dim):
            # Tent map: f(x) = mu * min(x, 1-x) for x in [0,1], else 0
            # Normalize x to [0,1] range
            x_norm = (x[j] + 5.0) / 10.0
            if x_norm < 0.5:
                tent_val = self.tent_params[j] * x_norm
            else:
                tent_val = self.tent_params[j] * (1.0 - x_norm)
            tent_terms += tent_val
        
        # Compute polynomial potential terms
        poly_terms = 0.0
        for j in range(self.dim):
            poly_term = 0.0
            for i in range(3):
                poly_term += self.poly_coeffs[i, j] * (x[j] ** (i + 1))
            poly_terms += poly_term
        
        # Compute radial basis function components
        rbf_terms = 0.0
        for i in range(5):
            rbf_dist = 0.0
            for j in range(self.dim):
                rbf_dist += ((x[j] - self.rbf_centers[i, j]) ** 2) / (2 * self.rbf_vars[i, j]**2)
            rbf_terms += self.rbf_weights[i] * np.exp(-rbf_dist)
        
        # Compute adaptive conditioning terms
        cond_terms = 0.0
        for j in range(self.dim):
            cond_terms += self.conditioning_params[j] * (x[j]**2) * (1.0 + 0.3 * np.sin(2.0 * x[j]))
        
        # Compute cross-dimensional coupling terms
        coupling_terms = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_terms += self.coupling_matrix[i, j] * x[i] * x[j]
        
        # Add chaotic modulation component
        chaos_modulation = 0.0
        for j in range(self.dim):
            chaos_modulation += self.chaos_factors[j] * np.sin(5.0 * x[j]) * np.cos(3.0 * x[j])
        
        # Combine all components with appropriate weights
        total = 1.0 * tent_terms + 0.7 * poly_terms + 0.6 * rbf_terms + 0.5 * cond_terms + 0.4 * coupling_terms + 0.3 * chaos_modulation
        
        return total