import numpy as np

class ChaoticHyperEllipsoidalLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize polynomial potential components with different degrees and coefficients
        self.poly_degrees = np.random.randint(2, 15, dim)
        self.poly_coeffs = np.random.uniform(-8.0, 8.0, dim)
        # Initialize chaotic sine-wave modulations with varying frequencies and amplitudes
        self.chaos_freqs = np.random.uniform(2.0, 20.0, dim)
        self.chaos_amplitudes = np.random.uniform(0.5, 6.0, dim)
        # Initialize hyper-ellipsoidal structures with dynamic centers and axes
        self.ellipsoid_centers = np.random.uniform(-4.9, 4.9, (12, dim))
        self.ellipsoid_axes = np.random.uniform(0.3, 5.0, (12, dim))
        self.ellipsoid_weights = np.random.uniform(0.2, 4.0, 12)
        # Initialize momentum-based gradient steering parameters
        self.momentum_params = np.random.uniform(0.02, 1.5, dim)
        self.steering_magnitude = np.random.uniform(0.05, 3.0, dim)
        # Add fractal-like interaction terms with adaptive conditioning
        self.fractal_coeffs = np.random.uniform(0.05, 1.2, dim)
        self.fractal_exponents = np.random.uniform(0.1, 1.5, dim)
        # Add cross-dimensional coupling terms for increased complexity with modified weights
        self.cross_coupling = np.random.uniform(-1.2, 1.2, (dim, dim))
        # Add adaptive conditioning parameters
        self.conditioning_factors = np.random.uniform(0.01, 4.0, dim)
        # Add additional chaotic modulation with time-varying parameters
        self.time_varying_freqs = np.random.uniform(0.3, 12.0, dim)
        self.time_varying_amplitudes = np.random.uniform(0.02, 2.0, dim)
        # Add novel hybrid components
        self.hybrid_coeffs = np.random.uniform(-3.0, 3.0, dim)
        self.hyperbolic_coeffs = np.random.uniform(0.3, 3.5, dim)
        # Add new chaotic modulation with higher frequency harmonics
        self.high_freq_coeffs = np.random.uniform(0.1, 2.5, dim)
        self.high_freq_powers = np.random.randint(3, 8, dim)
        # Add additional hyperbolic and logarithmic interaction terms
        self.log_coeffs = np.random.uniform(0.1, 1.5, dim)
        self.sinh_coeffs = np.random.uniform(0.2, 2.0, dim)
        # Add a complex multi-scale fractal component
        self.multi_scale_fractal = np.random.uniform(0.01, 0.8, dim)
        self.fractal_scales = np.random.uniform(0.5, 3.0, dim)
        
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
        for i in range(12):
            ell_dist = 0.0
            for j in range(self.dim):
                ell_dist += ((x[j] - self.ellipsoid_centers[i, j]) / self.ellipsoid_axes[i, j])**2
            ellipsoid_potential += self.ellipsoid_weights[i] * np.exp(-0.3 * ell_dist) + 0.2 * np.sin(ell_dist)
        
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
            conditioning_terms += self.conditioning_factors[j] * (x[j]**2) * (1.0 + 0.5 * np.sin(x[j]))
        
        # Combine all components with adjusted weights and enhanced nonlinear interactions
        total = 0.8 * poly_potential + 1.8 * chaos_modulation + ellipsoid_potential + 0.6 * steering_terms + 0.6 * fractal_terms + 0.4 * cross_terms + 0.3 * conditioning_terms
        
        # Add a new component to improve fitness: enhanced chaotic modulation with additional nonlinearities
        enhanced_chaos = 0.0
        for j in range(self.dim):
            enhanced_chaos += (self.chaos_amplitudes[j] * np.sin(self.chaos_freqs[j] * x[j]) + 
                              0.5 * np.sin(2.0 * self.chaos_freqs[j] * x[j]) * np.cos(x[j])) * \
                             np.exp(-0.2 * np.abs(x[j]))
        
        # Add a new component: hybrid polynomial and hyperbolic interaction with modified coefficients
        hybrid_terms = 0.0
        for j in range(self.dim):
            hybrid_terms += 1.5 * (x[j]**3) * np.tanh(0.5 * x[j]) + 1.0 * np.sinh(x[j]) + self.hybrid_coeffs[j] * np.log(1.0 + np.abs(x[j]))
        
        # Add a new component: hyperbolic interaction with additional coupling
        hyperbolic_terms = 0.0
        for j in range(self.dim):
            hyperbolic_terms += self.hyperbolic_coeffs[j] * np.tanh(2.0 * x[j]) * np.cos(0.5 * x[j])
        
        # Add high frequency chaotic components
        high_freq_terms = 0.0
        for j in range(self.dim):
            high_freq_terms += self.high_freq_coeffs[j] * np.sin(self.high_freq_powers[j] * x[j]) * np.exp(-0.1 * x[j]**2)
        
        # Add multi-scale fractal interaction
        multi_scale_terms = 0.0
        for j in range(self.dim):
            multi_scale_terms += self.multi_scale_fractal[j] * (np.abs(x[j]) ** self.fractal_scales[j]) * np.cos(3.0 * x[j])
        
        # Final combination with refined weights to improve overall fitness
        total = 0.9 * poly_potential + 2.0 * chaos_modulation + ellipsoid_potential + 0.6 * steering_terms + 0.6 * fractal_terms + 0.4 * cross_terms + 0.3 * conditioning_terms + 0.4 * enhanced_chaos + 0.25 * hybrid_terms + 0.15 * hyperbolic_terms + 0.2 * high_freq_terms + 0.1 * multi_scale_terms
        
        # Introduce a large mutation: Increase the weight of chaotic components and add new interaction terms
        mutated_total = total + 0.4 * np.sum(np.sinh(x)) + 0.2 * np.sum(np.cos(x)**2) + 0.3 * np.sum(np.exp(-x**2))
        
        # Slight modification to increase difficulty: add a complex harmonic interaction term
        harmonic_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                harmonic_interaction += 0.3 * np.sin(4.0 * (x[i] + x[j])) * np.cos(2.5 * (x[i] - x[j]))
        
        mutated_total += harmonic_interaction
        
        # Add a new complex interaction term: multi-dimensional sinusoidal coupling with exponential decay
        complex_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                complex_coupling += 0.2 * np.sin(x[i] + x[j]) * np.exp(-0.5 * (x[i]**2 + x[j]**2)) * np.cos(0.3 * (x[i] - x[j]))
        
        mutated_total += complex_coupling
        
        return mutated_total