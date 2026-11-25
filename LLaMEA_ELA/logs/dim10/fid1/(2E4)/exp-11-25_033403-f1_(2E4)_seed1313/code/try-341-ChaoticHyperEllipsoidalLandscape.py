import numpy as np

class ChaoticHyperEllipsoidalLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize polynomial potential components with different degrees and coefficients
        self.poly_degrees = np.random.randint(2, 7, dim)
        self.poly_coeffs = np.random.uniform(-3.0, 3.0, dim)
        # Initialize chaotic sine-wave modulations with varying frequencies and amplitudes
        self.chaos_freqs = np.random.uniform(2.0, 9.0, dim)
        self.chaos_amplitudes = np.random.uniform(0.4, 3.0, dim)
        # Initialize hyper-ellipsoidal structures with dynamic centers and axes
        self.ellipsoid_centers = np.random.uniform(-4.5, 4.5, (6, dim))
        self.ellipsoid_axes = np.random.uniform(0.8, 3.5, (6, dim))
        self.ellipsoid_weights = np.random.uniform(0.4, 2.5, 6)
        # Initialize momentum-based gradient steering parameters
        self.momentum_params = np.random.uniform(0.1, 0.95, dim)
        self.steering_magnitude = np.random.uniform(0.2, 1.8, dim)
        # Add fractal-like interaction terms with adaptive conditioning
        self.fractal_coeffs = np.random.uniform(0.05, 0.6, dim)
        self.fractal_exponents = np.random.uniform(0.2, 0.9, dim)
        # Add cross-dimensional coupling terms for increased complexity
        self.cross_coupling = np.random.uniform(-0.4, 0.4, (dim, dim))
        # Add adaptive conditioning parameters
        self.conditioning_factors = np.random.uniform(0.05, 2.5, dim)
        # Add additional chaotic modulation with time-varying parameters
        self.time_varying_freqs = np.random.uniform(0.8, 6.0, dim)
        self.time_varying_amplitudes = np.random.uniform(0.1, 1.2, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Compute polynomial potential with modified weights
        poly_potential = 0.0
        for j in range(self.dim):
            poly_potential += self.poly_coeffs[j] * (x[j] ** self.poly_degrees[j])
        
        # Add chaotic sine-wave modulation with time-varying components and enhanced nonlinearity
        chaos_modulation = 0.0
        for j in range(self.dim):
            time_component = np.sin(self.time_varying_freqs[j] * x[j]) * self.time_varying_amplitudes[j]
            chaos_modulation += self.chaos_amplitudes[j] * np.sin(self.chaos_freqs[j] * x[j] + time_component) * np.cos(0.5 * x[j])
        
        # Add hyper-ellipsoidal structures with additional interaction terms
        ellipsoid_potential = 0.0
        for i in range(6):
            ell_dist = 0.0
            for j in range(self.dim):
                ell_dist += ((x[j] - self.ellipsoid_centers[i, j]) / self.ellipsoid_axes[i, j])**2
            ellipsoid_potential += self.ellipsoid_weights[i] * np.exp(-0.3 * ell_dist) + 0.1 * np.sin(ell_dist)
        
        # Add momentum-based gradient steering with enhanced complexity
        steering_terms = 0.0
        for j in range(self.dim):
            steering_terms += self.steering_magnitude[j] * x[j] * np.sin(self.momentum_params[j] * x[j]) * np.cos(0.3 * x[j])
        
        # Add fractal-like interaction terms with modified scaling and exponentiation
        fractal_terms = 0.0
        for j in range(self.dim):
            fractal_terms += self.fractal_coeffs[j] * (np.abs(x[j]) ** self.fractal_exponents[j]) * np.sin(2.0 * x[j])
        
        # Add cross-dimensional coupling terms with enhanced interaction strength
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    cross_terms += self.cross_coupling[i, j] * x[i] * x[j] * np.cos(0.2 * (x[i] + x[j]))
        
        # Add adaptive conditioning with modified scaling
        conditioning_terms = 0.0
        for j in range(self.dim):
            conditioning_terms += self.conditioning_factors[j] * (x[j]**2) * (1.0 + 0.2 * np.sin(x[j]))
        
        # Combine all components with adjusted weights and enhanced nonlinear interactions
        total = 0.8 * poly_potential + 1.3 * chaos_modulation + ellipsoid_potential + 0.4 * steering_terms + 0.4 * fractal_terms + 0.25 * cross_terms + 0.2 * conditioning_terms
        
        # Add a new component to improve fitness: enhanced chaotic modulation with additional nonlinearities
        enhanced_chaos = 0.0
        for j in range(self.dim):
            enhanced_chaos += (self.chaos_amplitudes[j] * np.sin(self.chaos_freqs[j] * x[j]) + 
                              0.3 * np.sin(2.0 * self.chaos_freqs[j] * x[j]) * np.cos(x[j])) * \
                             np.exp(-0.1 * np.abs(x[j]))
        
        # Add a new component: hybrid polynomial and hyperbolic interaction with modified coefficients
        hybrid_terms = 0.0
        for j in range(self.dim):
            hybrid_terms += 1.2 * (x[j]**3) * np.tanh(0.5 * x[j]) + 0.7 * np.sinh(x[j])
        
        # Final combination with refined weights to improve overall fitness
        total = 0.9 * poly_potential + 1.5 * chaos_modulation + ellipsoid_potential + 0.4 * steering_terms + 0.4 * fractal_terms + 0.25 * cross_terms + 0.2 * conditioning_terms + 0.3 * enhanced_chaos + 0.15 * hybrid_terms
        
        return total