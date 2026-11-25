import numpy as np

class ChaoticHyperEllipsoidalLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize polynomial potential components
        self.poly_degrees = np.random.randint(2, 6, dim)
        self.poly_coeffs = np.random.uniform(-2.0, 2.0, dim)
        # Initialize chaotic sine-wave modulations
        self.chaos_freqs = np.random.uniform(3.0, 8.0, dim)
        self.chaos_amplitudes = np.random.uniform(0.5, 2.5, dim)
        # Initialize hyper-ellipsoidal structures with dynamic centers
        self.ellipsoid_centers = np.random.uniform(-4.0, 4.0, (5, dim))
        self.ellipsoid_axes = np.random.uniform(1.0, 3.0, (5, dim))
        self.ellipsoid_weights = np.random.uniform(0.5, 2.0, 5)
        # Initialize momentum-based gradient steering parameters
        self.momentum_params = np.random.uniform(0.1, 0.9, dim)
        self.steering_magnitude = np.random.uniform(0.3, 1.5, dim)
        # Add fractal-like interaction terms with adaptive conditioning
        self.fractal_coeffs = np.random.uniform(0.1, 0.5, dim)
        self.fractal_exponents = np.random.uniform(0.3, 0.8, dim)
        # Add cross-dimensional coupling terms for increased complexity
        self.cross_coupling = np.random.uniform(-0.3, 0.3, (dim, dim))
        # Add adaptive conditioning parameters
        self.conditioning_factors = np.random.uniform(0.1, 2.0, dim)
        # Add additional chaotic modulation with time-varying parameters
        self.time_varying_freqs = np.random.uniform(1.0, 5.0, dim)
        self.time_varying_amplitudes = np.random.uniform(0.2, 1.0, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Compute polynomial potential
        poly_potential = 0.0
        for j in range(self.dim):
            poly_potential += self.poly_coeffs[j] * (x[j] ** self.poly_degrees[j])
        
        # Add chaotic sine-wave modulation with time-varying components
        chaos_modulation = 0.0
        for j in range(self.dim):
            time_component = np.sin(self.time_varying_freqs[j] * x[j]) * self.time_varying_amplitudes[j]
            chaos_modulation += self.chaos_amplitudes[j] * np.sin(self.chaos_freqs[j] * x[j] + time_component)
        
        # Add hyper-ellipsoidal structures
        ellipsoid_potential = 0.0
        for i in range(5):
            ell_dist = 0.0
            for j in range(self.dim):
                ell_dist += ((x[j] - self.ellipsoid_centers[i, j]) / self.ellipsoid_axes[i, j])**2
            ellipsoid_potential += self.ellipsoid_weights[i] * np.exp(-0.5 * ell_dist)
        
        # Add momentum-based gradient steering
        steering_terms = 0.0
        for j in range(self.dim):
            steering_terms += self.steering_magnitude[j] * x[j] * np.sin(self.momentum_params[j] * x[j])
        
        # Add fractal-like interaction terms for enhanced complexity
        fractal_terms = 0.0
        for j in range(self.dim):
            fractal_terms += self.fractal_coeffs[j] * (np.abs(x[j]) ** self.fractal_exponents[j])
        
        # Add cross-dimensional coupling terms
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    cross_terms += self.cross_coupling[i, j] * x[i] * x[j]
        
        # Add adaptive conditioning
        conditioning_terms = 0.0
        for j in range(self.dim):
            conditioning_terms += self.conditioning_factors[j] * (x[j]**2)
        
        # Combine all components with dynamic weighting - significant mutation to improve performance
        total = 0.7 * poly_potential + 1.5 * chaos_modulation + ellipsoid_potential + 0.3 * steering_terms + 0.3 * fractal_terms + 0.2 * cross_terms + 0.15 * conditioning_terms
        
        return total