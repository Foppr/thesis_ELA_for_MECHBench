import numpy as np

class ChaoticTentRadialLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic tent map parameters
        self.tent_params = np.random.uniform(1.1, 1.9, dim)
        # Initialize radial basis functions with random centers and variances
        self.rbf_centers = np.random.uniform(-4.5, 4.5, (5, dim))
        self.rbf_vars = np.random.uniform(0.3, 1.8, (5, dim))
        self.rbf_weights = np.random.uniform(0.8, 2.2, 5)
        # Initialize polynomial conditioning with dynamic exponents
        self.poly_exponents = np.random.uniform(2.0, 5.0, dim)
        self.poly_coeffs = np.random.uniform(0.5, 1.5, dim)
        # Initialize dynamic coupling matrix with fractal properties
        self.coupling_matrix = np.zeros((dim, dim))
        for i in range(dim):
            for j in range(dim):
                if i != j:
                    self.coupling_matrix[i, j] = np.random.uniform(-0.4, 0.4) * np.sin(0.5 * (i + j))
        # Initialize fractal interference parameters
        self.fractal_freqs = np.random.uniform(2.0, 8.0, dim)
        self.fractal_amps = np.random.uniform(0.3, 1.2, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Compute chaotic tent map dynamics
        tent_terms = 0.0
        for j in range(self.dim):
            # Tent map with dynamic parameter
            tent_val = x[j]
            for _ in range(3):  # Apply tent map 3 times for chaos
                if tent_val < 0.5:
                    tent_val = self.tent_params[j] * tent_val
                else:
                    tent_val = self.tent_params[j] * (1.0 - tent_val)
            tent_terms += tent_val ** 2
        
        # Compute radial basis function components
        rbf_terms = 0.0
        for i in range(5):
            rbf_dist = 0.0
            for j in range(self.dim):
                rbf_dist += ((x[j] - self.rbf_centers[i, j]) ** 2) / (2 * self.rbf_vars[i, j]**2)
            rbf_terms += self.rbf_weights[i] * np.exp(-rbf_dist)
        
        # Compute polynomial conditioning terms
        poly_terms = 0.0
        for j in range(self.dim):
            poly_terms += self.poly_coeffs[j] * (x[j] ** self.poly_exponents[j])
        
        # Compute dynamic coupling terms with fractal interference
        coupling_terms = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_terms += self.coupling_matrix[i, j] * x[i] * x[j]
        
        # Compute fractal interference terms
        fractal_terms = 0.0
        for j in range(self.dim):
            fractal_terms += self.fractal_amps[j] * np.sin(self.fractal_freqs[j] * x[j]) * np.cos(0.3 * x[j])
        
        # Combine all components with refined weights
        total = 1.1 * tent_terms + 0.9 * rbf_terms + 0.7 * poly_terms + 0.5 * coupling_terms + 0.3 * fractal_terms
        
        return total