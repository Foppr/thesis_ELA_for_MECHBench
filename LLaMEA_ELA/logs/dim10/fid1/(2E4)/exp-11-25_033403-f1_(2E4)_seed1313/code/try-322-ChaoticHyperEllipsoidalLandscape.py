import numpy as np

class ChaoticHyperEllipsoidalLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize polynomial potential components with increased complexity
        self.poly_degrees = np.random.randint(2, 8, dim)
        self.poly_coeffs = np.random.uniform(-3.0, 3.0, dim)
        # Initialize chaotic sine-wave modulations with higher frequency and amplitude
        self.chaos_freqs = np.random.uniform(5.0, 12.0, dim)
        self.chaos_amplitudes = np.random.uniform(1.0, 4.0, dim)
        # Initialize hyper-ellipsoidal structures with dynamic centers and more varied axes
        self.ellipsoid_centers = np.random.uniform(-3.5, 3.5, (7, dim))
        self.ellipsoid_axes = np.random.uniform(0.5, 4.0, (7, dim))
        self.ellipsoid_weights = np.random.uniform(0.3, 2.5, 7)
        # Initialize momentum-based gradient steering parameters with enhanced steering
        self.momentum_params = np.random.uniform(0.05, 1.2, dim)
        self.steering_magnitude = np.random.uniform(0.5, 2.0, dim)
        # Add fractal-like interaction terms with more complex exponents
        self.fractal_coeffs = np.random.uniform(0.05, 0.8, dim)
        self.fractal_exponents = np.random.uniform(0.1, 1.0, dim)
        # Add cross-dimensional coupling terms with stronger interactions
        self.cross_coupling = np.random.uniform(-0.7, 0.7, (dim, dim))
        # Add adaptive conditioning parameters with more varied factors
        self.conditioning_factors = np.random.uniform(0.05, 3.0, dim)
        # Add additional chaotic modulation with time-varying parameters
        self.time_varying_freqs = np.random.uniform(2.0, 8.0, dim)
        self.time_varying_amplitudes = np.random.uniform(0.1, 1.5, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Compute polynomial potential with higher degree terms
        poly_potential = 0.0
        for j in range(self.dim):
            poly_potential += self.poly_coeffs[j] * (x[j] ** self.poly_degrees[j])
        
        # Add chaotic sine-wave modulation with time-varying components and more complex interaction
        chaos_modulation = 0.0
        for j in range(self.dim):
            time_component = np.sin(self.time_varying_freqs[j] * x[j]) * self.time_varying_amplitudes[j]
            chaos_modulation += self.chaos_amplitudes[j] * np.sin(self.chaos_freqs[j] * x[j] + time_component) * np.cos(0.5 * x[j])
        
        # Add hyper-ellipsoidal structures with more complex interaction
        ellipsoid_potential = 0.0
        for i in range(7):
            ell_dist = 0.0
            for j in range(self.dim):
                ell_dist += ((x[j] - self.ellipsoid_centers[i, j]) / self.ellipsoid_axes[i, j])**2
            ellipsoid_potential += self.ellipsoid_weights[i] * np.exp(-0.3 * ell_dist)
        
        # Add momentum-based gradient steering with enhanced effect
        steering_terms = 0.0
        for j in range(self.dim):
            steering_terms += self.steering_magnitude[j] * x[j] * np.sin(self.momentum_params[j] * x[j]) * np.cos(0.3 * x[j])
        
        # Add fractal-like interaction terms for enhanced complexity
        fractal_terms = 0.0
        for j in range(self.dim):
            fractal_terms += self.fractal_coeffs[j] * (np.abs(x[j]) ** self.fractal_exponents[j]) * np.sin(2.0 * x[j])
        
        # Add cross-dimensional coupling terms with stronger interactions
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    cross_terms += self.cross_coupling[i, j] * x[i] * x[j] * np.sin(0.5 * (x[i] + x[j]))
        
        # Add adaptive conditioning with more complex structure
        conditioning_terms = 0.0
        for j in range(self.dim):
            conditioning_terms += self.conditioning_factors[j] * (x[j]**2) * np.cos(0.2 * x[j])
        
        # Combine all components with optimized weighting - significant mutation to improve performance
        total = 0.9 * poly_potential + 1.6 * chaos_modulation + 1.3 * ellipsoid_potential + 0.5 * steering_terms + 0.6 * fractal_terms + 0.4 * cross_terms + 0.25 * conditioning_terms
        
        return total