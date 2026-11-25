import numpy as np

class DeceptiveRadialSinusoidalLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize radial basis function centers and widths
        self.rbf_centers = np.random.uniform(-4.5, 4.5, (8, dim))
        self.rbf_widths = np.random.uniform(0.5, 3.0, (8, dim))
        self.rbf_weights = np.random.uniform(-2.0, 2.0, 8)
        # Initialize sinusoidal wave parameters
        self.sin_freqs = np.random.uniform(1.0, 10.0, dim)
        self.sin_amplitudes = np.random.uniform(0.5, 3.0, dim)
        self.sin_phases = np.random.uniform(0, 2*np.pi, dim)
        # Initialize polynomial interaction terms
        self.poly_coeffs = np.random.uniform(-1.0, 1.0, dim)
        self.poly_exponents = np.random.randint(2, 8, dim)
        # Initialize dynamic scaling factors
        self.scaling_factors = np.random.uniform(0.1, 5.0, dim)
        # Initialize cross-dimensional coupling
        self.coupling_matrix = np.random.uniform(-0.5, 0.5, (dim, dim))
        # Initialize deceptive terms with multiple local minima
        self.deception_centers = np.random.uniform(-4.0, 4.0, (6, dim))
        self.deception_strengths = np.random.uniform(1.0, 4.0, 6)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Compute radial basis function components
        rbf_sum = 0.0
        for i in range(8):
            dist_sq = np.sum(((x - self.rbf_centers[i]) / self.rbf_widths[i]) ** 2)
            rbf_sum += self.rbf_weights[i] * np.exp(-0.5 * dist_sq)
        
        # Compute sinusoidal wave components
        sin_sum = 0.0
        for j in range(self.dim):
            sin_sum += self.sin_amplitudes[j] * np.sin(self.sin_freqs[j] * x[j] + self.sin_phases[j])
        
        # Compute polynomial interaction terms
        poly_sum = 0.0
        for j in range(self.dim):
            poly_sum += self.poly_coeffs[j] * (x[j] ** self.poly_exponents[j])
        
        # Apply dynamic scaling
        scaled_sum = 0.0
        for j in range(self.dim):
            scaled_sum += self.scaling_factors[j] * x[j] ** 2
        
        # Compute cross-dimensional coupling
        coupling_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_sum += self.coupling_matrix[i, j] * x[i] * x[j]
        
        # Compute deceptive terms with multiple local minima
        deception_sum = 0.0
        for i in range(6):
            dist_sq = np.sum((x - self.deception_centers[i]) ** 2)
            deception_sum += self.deception_strengths[i] * np.exp(-0.1 * dist_sq) * np.cos(2.0 * np.sqrt(dist_sq))
        
        # Combine all components with appropriate weights
        total = 0.8 * rbf_sum + 0.6 * sin_sum + 0.4 * poly_sum + 0.3 * scaled_sum + 0.2 * coupling_sum + 0.5 * deception_sum
        
        return total