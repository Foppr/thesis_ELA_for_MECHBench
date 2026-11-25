import numpy as np

class ChaoticTentRadialLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic tent map parameters with more varied ranges
        self.tent_params = np.random.uniform(1.2, 1.8, dim)
        # Initialize polynomial potential coefficients with higher degrees
        self.poly_coeffs = np.random.uniform(-3.0, 3.0, (4, dim))
        # Initialize radial basis functions with more centers and adjusted variances
        self.rbf_centers = np.random.uniform(-4.8, 4.8, (7, dim))
        self.rbf_vars = np.random.uniform(0.2, 2.0, (7, dim))
        self.rbf_weights = np.random.uniform(0.5, 2.5, 7)
        # Initialize dynamic conditioning parameters with stronger modulation
        self.conditioning_params = np.random.uniform(0.3, 1.8, dim)
        # Initialize cross-dimensional coupling matrix with stronger weights
        self.coupling_matrix = np.random.uniform(-0.5, 0.5, (dim, dim))
        # Initialize chaotic modulation factors with different frequencies
        self.chaos_factors = np.random.uniform(0.2, 0.7, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Compute chaotic tent map components with modified dynamics
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
        
        # Compute polynomial potential terms with higher degree components
        poly_terms = 0.0
        for j in range(self.dim):
            poly_term = 0.0
            for i in range(4):
                poly_term += self.poly_coeffs[i, j] * (x[j] ** (i + 1))
            poly_terms += poly_term
        
        # Compute radial basis function components with more centers
        rbf_terms = 0.0
        for i in range(7):
            rbf_dist = 0.0
            for j in range(self.dim):
                rbf_dist += ((x[j] - self.rbf_centers[i, j]) ** 2) / (2 * self.rbf_vars[i, j]**2)
            rbf_terms += self.rbf_weights[i] * np.exp(-rbf_dist)
        
        # Compute adaptive conditioning terms with enhanced nonlinearity
        cond_terms = 0.0
        for j in range(self.dim):
            cond_terms += self.conditioning_params[j] * (x[j]**2) * (1.0 + 0.5 * np.sin(3.0 * x[j]) + 0.3 * np.cos(2.0 * x[j]))
        
        # Compute cross-dimensional coupling terms with stronger interactions
        coupling_terms = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_terms += self.coupling_matrix[i, j] * x[i] * x[j] * np.sin(0.5 * (x[i] + x[j]))
        
        # Add chaotic modulation component with enhanced complexity
        chaos_modulation = 0.0
        for j in range(self.dim):
            chaos_modulation += self.chaos_factors[j] * (np.sin(7.0 * x[j]) * np.cos(4.0 * x[j]) + 
                                                          0.5 * np.sin(3.0 * x[j]) * np.cos(5.0 * x[j]))
        
        # Combine all components with adjusted weights for better balance
        total = 1.2 * tent_terms + 0.8 * poly_terms + 0.7 * rbf_terms + 0.6 * cond_terms + 0.5 * coupling_terms + 0.4 * chaos_modulation
        
        return total