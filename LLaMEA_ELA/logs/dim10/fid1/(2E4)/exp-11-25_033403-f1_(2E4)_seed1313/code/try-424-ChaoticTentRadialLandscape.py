import numpy as np

class ChaoticTentRadialLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic tent map parameters
        self.tent_params = np.random.uniform(1.5, 2.0, dim)
        # Initialize polynomial potential exponents and coefficients
        self.poly_exponents = np.random.uniform(2.0, 6.0, dim)
        self.poly_coeffs = np.random.uniform(0.5, 2.5, dim)
        # Initialize radial basis functions with random centers and variances
        self.rbf_centers = np.random.uniform(-4.0, 4.0, (5, dim))
        self.rbf_vars = np.random.uniform(0.3, 1.5, (5, dim))
        self.rbf_weights = np.random.uniform(1.0, 4.0, 5)
        # Initialize dynamic conditioning parameters
        self.conditioning_factors = np.random.uniform(0.05, 0.5, dim)
        # Initialize cross-dimensional coupling matrix with higher-order terms
        self.coupling_matrix = np.random.uniform(-0.8, 0.8, (dim, dim))
        self.high_order_coupling = np.random.uniform(-0.3, 0.3, (dim, dim, dim))
        # Initialize phase shifts and modulation frequencies
        self.phase_shifts = np.random.uniform(0, 2*np.pi, dim)
        self.modulation_freqs = np.random.uniform(2.0, 8.0, dim)
        # Initialize adaptive scaling factors
        self.scaling_factors = np.random.uniform(0.8, 1.5, dim)
        # Initialize harmonic interaction terms
        self.harmonic_amps = np.random.uniform(0.3, 1.8, dim)
        self.harmonic_freqs = np.random.uniform(1.0, 5.0, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Compute chaotic tent map components
        tent_terms = 0.0
        for j in range(self.dim):
            tent_val = self.tent_params[j] * np.abs(x[j])
            if x[j] > 0.5:
                tent_val = 1.0 - tent_val
            tent_terms += tent_val
        
        # Compute polynomial potential components
        poly_terms = 0.0
        for j in range(self.dim):
            poly_terms += self.poly_coeffs[j] * (x[j] ** self.poly_exponents[j])
        
        # Compute radial basis function components
        rbf_terms = 0.0
        for i in range(5):
            rbf_dist = 0.0
            for j in range(self.dim):
                rbf_dist += ((x[j] - self.rbf_centers[i, j]) ** 2) / (2 * self.rbf_vars[i, j]**2)
            rbf_terms += self.rbf_weights[i] * np.exp(-rbf_dist)
        
        # Compute dynamic conditioning terms
        cond_terms = 0.0
        for j in range(self.dim):
            cond_terms += self.conditioning_factors[j] * (x[j]**2) * (1.0 + 0.5 * np.sin(3.0 * x[j]) + 0.3 * np.cos(5.0 * x[j]))
        
        # Compute cross-dimensional coupling terms with higher-order interactions
        coupling_terms = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_terms += self.coupling_matrix[i, j] * x[i] * x[j]
                    # Add higher-order coupling terms
                    for k in range(self.dim):
                        if i != k and j != k:
                            coupling_terms += self.high_order_coupling[i, j, k] * x[i] * x[j] * x[k]
        
        # Compute sine modulation components
        sin_mod_terms = 0.0
        for j in range(self.dim):
            sin_mod_terms += np.sin(self.modulation_freqs[j] * x[j]) * (1.0 + 0.2 * np.cos(2.0 * x[j]))
        
        # Compute harmonic interaction terms
        harmonic_terms = 0.0
        for j in range(self.dim):
            harmonic_terms += self.harmonic_amps[j] * np.sin(self.harmonic_freqs[j] * x[j])
        
        # Combine all components with appropriate weights and scaling factors
        total = (0.7 * tent_terms + 
                 0.5 * poly_terms + 
                 0.6 * rbf_terms + 
                 0.3 * cond_terms + 
                 0.4 * coupling_terms + 
                 0.2 * sin_mod_terms + 
                 0.1 * harmonic_terms)
        
        # Apply adaptive scaling
        for j in range(self.dim):
            total *= self.scaling_factors[j]
            
        return total