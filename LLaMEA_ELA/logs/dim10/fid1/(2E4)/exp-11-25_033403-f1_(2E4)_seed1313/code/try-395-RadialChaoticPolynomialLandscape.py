import numpy as np

class RadialChaoticPolynomialLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize radial basis functions with random centers, widths, and weights
        self.rbf_centers = np.random.uniform(-4.5, 4.5, (12, dim))
        self.rbf_widths = np.random.uniform(0.5, 3.0, (12, dim))
        self.rbf_weights = np.random.uniform(-2.0, 2.0, 12)
        # Initialize polynomial terms with varying degrees and coefficients
        self.poly_degrees = np.random.randint(2, 8, dim)
        self.poly_coeffs = np.random.uniform(-3.0, 3.0, dim)
        # Initialize chaotic sine-wave modulations with time-varying parameters
        self.chaos_freqs = np.random.uniform(2.0, 15.0, dim)
        self.chaos_amplitudes = np.random.uniform(0.5, 5.0, dim)
        # Add dynamic conditioning factors
        self.conditioning_factors = np.random.uniform(0.1, 4.0, dim)
        # Add cross-dimensional coupling terms with adaptive weights
        self.cross_coupling = np.random.uniform(-1.0, 1.0, (dim, dim))
        # Add fractal-like harmonic interactions
        self.fractal_harmonic_coeffs = np.random.uniform(0.1, 2.5, dim)
        self.fractal_harmonic_exponents = np.random.uniform(0.2, 1.8, dim)
        # Add hyperbolic tangent interaction terms
        self.tanh_coeffs = np.random.uniform(0.3, 3.0, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Compute radial basis function potential
        rbf_potential = 0.0
        for i in range(12):
            rbf_dist = 0.0
            for j in range(self.dim):
                rbf_dist += ((x[j] - self.rbf_centers[i, j]) / self.rbf_widths[i, j])**2
            rbf_potential += self.rbf_weights[i] * np.exp(-0.5 * rbf_dist)
        
        # Compute polynomial potential
        poly_potential = 0.0
        for j in range(self.dim):
            poly_potential += self.poly_coeffs[j] * (x[j] ** self.poly_degrees[j])
        
        # Add chaotic sine-wave modulation
        chaos_modulation = 0.0
        for j in range(self.dim):
            chaos_modulation += self.chaos_amplitudes[j] * np.sin(self.chaos_freqs[j] * x[j]) * np.cos(0.3 * x[j])
        
        # Add dynamic conditioning terms
        conditioning_terms = 0.0
        for j in range(self.dim):
            conditioning_terms += self.conditioning_factors[j] * (x[j]**2) * (1.0 + 0.5 * np.sin(x[j]))
        
        # Add cross-dimensional coupling
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    cross_terms += self.cross_coupling[i, j] * x[i] * x[j]
        
        # Add fractal-like harmonic interactions
        fractal_harmonic = 0.0
        for j in range(self.dim):
            fractal_harmonic += self.fractal_harmonic_coeffs[j] * (np.abs(x[j]) ** self.fractal_harmonic_exponents[j]) * np.sin(2.0 * x[j])
        
        # Add hyperbolic tangent interactions
        tanh_terms = 0.0
        for j in range(self.dim):
            tanh_terms += self.tanh_coeffs[j] * np.tanh(1.5 * x[j]) * np.cos(0.4 * x[j])
        
        # Combine all components with adjusted weights
        total = 0.6 * rbf_potential + 0.8 * poly_potential + 1.2 * chaos_modulation + 0.4 * conditioning_terms + 0.3 * cross_terms + 0.25 * fractal_harmonic + 0.2 * tanh_terms
        
        # Add a complex interaction term for increased difficulty
        complex_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                complex_interaction += 0.15 * np.sin(4.0 * x[i]) * np.cos(3.0 * x[j]) * np.exp(-0.1 * (x[i] - x[j])**2)
        
        total += complex_interaction
        
        return total