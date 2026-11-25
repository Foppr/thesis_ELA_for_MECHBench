import numpy as np

class ChaoticTentRadialLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic tent map parameters with broader range
        self.tent_params = np.random.uniform(1.05, 1.95, dim)
        # Initialize polynomial potential coefficients with higher degree terms
        self.poly_coeffs = np.random.uniform(-3.0, 3.0, (5, dim))
        # Initialize radial basis functions with more centers and adaptive variances
        self.rbf_centers = np.random.uniform(-4.8, 4.8, (8, dim))
        self.rbf_vars = np.random.uniform(0.2, 2.0, (8, dim))
        self.rbf_weights = np.random.uniform(0.5, 2.5, 8)
        # Initialize dynamic conditioning parameters with sinusoidal modulation
        self.conditioning_params = np.random.uniform(0.3, 1.7, dim)
        # Initialize cross-dimensional coupling matrix with stronger interactions
        self.coupling_matrix = np.random.uniform(-0.5, 0.5, (dim, dim))
        # Initialize chaotic modulation factors with hyperbolic tangent components
        self.chaos_factors = np.random.uniform(0.05, 0.6, dim)
        # Add sine modulation parameters for enhanced complexity
        self.sine_modulation = np.random.uniform(0.1, 1.0, dim)
        # Add hyperbolic tangent chaotic components
        self.tanh_chaos_factors = np.random.uniform(0.02, 0.4, dim)
        # Add adaptive scaling factors
        self.scaling_factors = np.random.uniform(0.8, 1.2, dim)
        
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
        
        # Compute polynomial potential terms with higher degrees
        poly_terms = 0.0
        for j in range(self.dim):
            poly_term = 0.0
            for i in range(5):
                poly_term += self.poly_coeffs[i, j] * (x[j] ** (i + 1))
            poly_terms += poly_term
        
        # Compute radial basis function components
        rbf_terms = 0.0
        for i in range(8):
            rbf_dist = 0.0
            for j in range(self.dim):
                rbf_dist += ((x[j] - self.rbf_centers[i, j]) ** 2) / (2 * self.rbf_vars[i, j]**2)
            rbf_terms += self.rbf_weights[i] * np.exp(-rbf_dist)
        
        # Compute adaptive conditioning terms with sinusoidal modulation
        cond_terms = 0.0
        for j in range(self.dim):
            cond_terms += self.conditioning_params[j] * (x[j]**2) * (1.0 + 0.5 * np.sin(3.0 * x[j]))
        
        # Compute cross-dimensional coupling terms with stronger weights
        coupling_terms = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_terms += self.coupling_matrix[i, j] * x[i] * x[j]
        
        # Add chaotic modulation component with sine enhancement and hyperbolic tangent
        chaos_modulation = 0.0
        for j in range(self.dim):
            chaos_modulation += self.chaos_factors[j] * np.sin(5.0 * x[j]) * np.cos(3.0 * x[j])
            chaos_modulation += self.tanh_chaos_factors[j] * np.tanh(2.0 * x[j])
        
        # Add sine modulation for additional complexity
        sine_terms = 0.0
        for j in range(self.dim):
            sine_terms += self.sine_modulation[j] * np.sin(7.0 * x[j]) * np.cos(4.0 * x[j])
        
        # Apply adaptive scaling to all components
        tent_terms *= self.scaling_factors[0]
        poly_terms *= self.scaling_factors[1]
        rbf_terms *= self.scaling_factors[2]
        cond_terms *= self.scaling_factors[3]
        coupling_terms *= self.scaling_factors[4]
        chaos_modulation *= self.scaling_factors[5]
        sine_terms *= self.scaling_factors[6]
        
        # Combine all components with appropriate weights
        total = 1.2 * tent_terms + 0.8 * poly_terms + 0.7 * rbf_terms + 0.6 * cond_terms + 0.5 * coupling_terms + 0.4 * chaos_modulation + 0.3 * sine_terms
        
        return total