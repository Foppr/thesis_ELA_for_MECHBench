import numpy as np

class ChaoticHyperEllipsoidalLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize polynomial potential components with different degrees and coefficients
        self.poly_degrees = np.random.randint(2, 15, dim)
        self.poly_coeffs = np.random.uniform(-8.0, 8.0, dim)
        # Initialize chaotic sine-wave modulations with varying frequencies and amplitudes
        self.chaos_freqs = np.random.uniform(6.0, 20.0, dim)
        self.chaos_amplitudes = np.random.uniform(1.0, 7.0, dim)
        # Initialize hyper-ellipsoidal structures with dynamic centers and axes
        self.ellipsoid_centers = np.random.uniform(-4.9, 4.9, (15, dim))
        self.ellipsoid_axes = np.random.uniform(0.2, 6.0, (15, dim))
        self.ellipsoid_weights = np.random.uniform(0.1, 5.0, 15)
        # Initialize momentum-based gradient steering parameters
        self.momentum_params = np.random.uniform(0.01, 1.5, dim)
        self.steering_magnitude = np.random.uniform(0.2, 3.0, dim)
        # Add fractal-like interaction terms with adaptive conditioning
        self.fractal_coeffs = np.random.uniform(0.01, 1.5, dim)
        self.fractal_exponents = np.random.uniform(0.02, 1.5, dim)
        # Add cross-dimensional coupling terms for increased complexity
        self.cross_coupling = np.random.uniform(-1.0, 1.0, (dim, dim))
        # Add adaptive conditioning parameters
        self.conditioning_factors = np.random.uniform(0.005, 5.0, dim)
        # Add additional chaotic modulation with time-varying parameters
        self.time_varying_freqs = np.random.uniform(0.2, 12.0, dim)
        self.time_varying_amplitudes = np.random.uniform(0.01, 2.5, dim)
        # Add novel hybrid polynomial-hyperbolic components
        self.hybrid_coeffs = np.random.uniform(0.5, 4.0, dim)
        self.hybrid_exponents = np.random.uniform(0.1, 2.0, dim)
        # Add enhanced cross-dimensional coupling with sine-wave interactions
        self.sine_coupling = np.random.uniform(-0.8, 0.8, (dim, dim))
        # Add additional complex interaction terms
        self.complex_coupling = np.random.uniform(-0.5, 0.5, (dim, dim, dim))
        # Add higher-order polynomial components
        self.high_order_coeffs = np.random.uniform(-0.7, 0.7, dim)
        # Add new chaotic modulation with enhanced nonlinearity and interaction
        self.enhanced_chaos_freqs = np.random.uniform(8.0, 25.0, dim)
        self.enhanced_chaos_amplitudes = np.random.uniform(1.5, 8.0, dim)
        # Add new hyperbolic interaction terms with modified parameters
        self.hyperbolic_coeffs = np.random.uniform(0.3, 2.5, dim)
        self.hyperbolic_exponents = np.random.uniform(0.05, 1.8, dim)
        # Add new complex coupling with higher-order interactions
        self.high_order_coupling = np.random.uniform(-0.3, 0.3, (dim, dim, dim, dim))
        
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
        for i in range(15):
            ell_dist = 0.0
            for j in range(self.dim):
                ell_dist += ((x[j] - self.ellipsoid_centers[i, j]) / self.ellipsoid_axes[i, j])**2
            ellipsoid_potential += self.ellipsoid_weights[i] * np.exp(-0.1 * ell_dist) + 0.3 * np.sin(ell_dist)
        
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
        total = 0.7 * poly_potential + 1.8 * chaos_modulation + ellipsoid_potential + 0.5 * steering_terms + 0.45 * fractal_terms + 0.3 * cross_terms + 0.25 * conditioning_terms
        
        # Add a new component to improve fitness: enhanced chaotic modulation with additional nonlinearities
        enhanced_chaos = 0.0
        for j in range(self.dim):
            enhanced_chaos += (self.chaos_amplitudes[j] * np.sin(self.chaos_freqs[j] * x[j]) + 
                              0.6 * np.sin(2.0 * self.chaos_freqs[j] * x[j]) * np.cos(x[j])) * \
                             np.exp(-0.15 * np.abs(x[j]))
        
        # Add a new component: hybrid polynomial and hyperbolic interaction with modified coefficients
        hybrid_terms = 0.0
        for j in range(self.dim):
            hybrid_terms += self.hybrid_coeffs[j] * (x[j]**3) * np.tanh(0.5 * x[j]) + self.hybrid_exponents[j] * np.sinh(x[j])
        
        # Add sine-wave cross-dimensional coupling terms
        sine_cross_terms = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    sine_cross_terms += self.sine_coupling[i, j] * np.sin(x[i]) * np.cos(x[j])
        
        # Add complex higher-order coupling terms
        complex_terms = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                for k in range(self.dim):
                    if i != j and j != k and i != k:
                        complex_terms += self.complex_coupling[i, j, k] * x[i] * x[j] * x[k]
        
        # Add higher-order polynomial terms
        high_order_terms = 0.0
        for j in range(self.dim):
            high_order_terms += self.high_order_coeffs[j] * (x[j]**5)
        
        # Add new enhanced chaotic components with additional interaction
        new_chaos = 0.0
        for j in range(self.dim):
            new_chaos += self.enhanced_chaos_amplitudes[j] * np.sin(self.enhanced_chaos_freqs[j] * x[j]) * np.cos(0.3 * x[j]) + 0.2 * np.sin(3.0 * x[j])
        
        # Add new hyperbolic interaction terms
        new_hyperbolic = 0.0
        for j in range(self.dim):
            new_hyperbolic += self.hyperbolic_coeffs[j] * np.tanh(0.8 * x[j]) * (x[j]**2) + self.hyperbolic_exponents[j] * np.cosh(x[j])
        
        # Add higher-order coupling with 4-dimensional interactions
        high_order_coupling_terms = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                for k in range(self.dim):
                    for l in range(self.dim):
                        if i != j and j != k and k != l and i != l:
                            high_order_coupling_terms += self.high_order_coupling[i, j, k, l] * x[i] * x[j] * x[k] * x[l]
        
        # Final combination with refined weights to improve overall fitness
        total = 0.75 * poly_potential + 2.0 * chaos_modulation + ellipsoid_potential + 0.5 * steering_terms + 0.45 * fractal_terms + 0.3 * cross_terms + 0.25 * conditioning_terms + 0.45 * enhanced_chaos + 0.3 * hybrid_terms + 0.2 * sine_cross_terms + 0.15 * complex_terms + 0.08 * high_order_terms + 0.3 * new_chaos + 0.25 * new_hyperbolic + 0.1 * high_order_coupling_terms
        
        # Introduce a larger mutation: Increase the weight of chaotic components and add new hyperbolic interaction terms
        mutated_total = total + 0.4 * np.sum(np.sinh(x)) + 0.3 * np.sum(np.cos(x)**2) + 0.2 * np.sum(np.tan(x))
        
        return mutated_total