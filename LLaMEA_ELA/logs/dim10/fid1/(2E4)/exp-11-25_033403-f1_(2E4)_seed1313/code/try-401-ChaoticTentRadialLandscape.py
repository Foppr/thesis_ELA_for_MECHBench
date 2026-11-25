import numpy as np

class ChaoticTentRadialLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic tent map parameters
        self.tent_params = np.random.uniform(1.5, 3.0, dim)
        self.tent_offsets = np.random.uniform(-0.5, 0.5, dim)
        # Initialize polynomial potential components with different degrees and coefficients
        self.poly_degrees = np.random.randint(2, 10, dim)
        self.poly_coeffs = np.random.uniform(-5.0, 5.0, dim)
        # Initialize Gaussian radial basis functions with dynamic centers and widths
        self.rbf_centers = np.random.uniform(-4.9, 4.9, (8, dim))
        self.rbf_widths = np.random.uniform(0.5, 3.0, (8, dim))
        self.rbf_weights = np.random.uniform(0.5, 3.0, 8)
        # Initialize momentum-based gradient steering parameters
        self.momentum_params = np.random.uniform(0.01, 1.0, dim)
        self.steering_magnitude = np.random.uniform(0.1, 2.0, dim)
        # Add fractal-like interaction terms with adaptive conditioning
        self.fractal_coeffs = np.random.uniform(0.1, 1.0, dim)
        self.fractal_exponents = np.random.uniform(0.2, 1.2, dim)
        # Add cross-dimensional coupling terms for increased complexity with modified weights
        self.cross_coupling = np.random.uniform(-1.0, 1.0, (dim, dim))
        # Add adaptive conditioning parameters
        self.conditioning_factors = np.random.uniform(0.05, 2.0, dim)
        # Add additional chaotic modulation with time-varying parameters
        self.time_varying_freqs = np.random.uniform(0.5, 8.0, dim)
        self.time_varying_amplitudes = np.random.uniform(0.1, 1.5, dim)
        # Add novel hybrid components
        self.hybrid_coeffs = np.random.uniform(-2.0, 2.0, dim)
        self.tanh_coeffs = np.random.uniform(0.5, 2.5, dim)
        # Add new chaotic modulation with higher frequency harmonics
        self.high_freq_coeffs = np.random.uniform(0.2, 1.8, dim)
        self.high_freq_powers = np.random.randint(2, 6, dim)
        # Add additional hyperbolic and logarithmic interaction terms
        self.log_coeffs = np.random.uniform(0.2, 1.0, dim)
        self.sinh_coeffs = np.random.uniform(0.3, 1.5, dim)
        # Add a complex multi-scale fractal component
        self.multi_scale_fractal = np.random.uniform(0.02, 0.6, dim)
        self.fractal_scales = np.random.uniform(0.3, 2.5, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Compute chaotic tent map with dynamic parameters and offset
        tent_map = 0.0
        for j in range(self.dim):
            tent_val = self.tent_params[j] * np.abs(x[j] - self.tent_offsets[j])
            tent_map += tent_val - np.floor(tent_val)
        
        # Compute polynomial potential with modified weights
        poly_potential = 0.0
        for j in range(self.dim):
            poly_potential += self.poly_coeffs[j] * (x[j] ** self.poly_degrees[j])
        
        # Add Gaussian radial basis functions with additional interaction terms
        rbf_potential = 0.0
        for i in range(8):
            rbf_dist = 0.0
            for j in range(self.dim):
                rbf_dist += ((x[j] - self.rbf_centers[i, j]) / self.rbf_widths[i, j])**2
            rbf_potential += self.rbf_weights[i] * np.exp(-0.5 * rbf_dist) + 0.1 * np.sin(rbf_dist)
        
        # Add momentum-based gradient steering with enhanced complexity
        steering_terms = 0.0
        for j in range(self.dim):
            steering_terms += self.steering_magnitude[j] * x[j] * np.sin(self.momentum_params[j] * x[j]) * np.cos(0.2 * x[j])
        
        # Add fractal-like interaction terms with modified scaling and exponentiation
        fractal_terms = 0.0
        for j in range(self.dim):
            fractal_terms += self.fractal_coeffs[j] * (np.abs(x[j]) ** self.fractal_exponents[j]) * np.sin(1.5 * x[j])
        
        # Add cross-dimensional coupling terms with enhanced interaction strength
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    cross_terms += self.cross_coupling[i, j] * x[i] * x[j] * np.cos(0.1 * (x[i] + x[j]))
        
        # Add adaptive conditioning with modified scaling
        conditioning_terms = 0.0
        for j in range(self.dim):
            conditioning_terms += self.conditioning_factors[j] * (x[j]**2) * (1.0 + 0.3 * np.sin(x[j]))
        
        # Combine all components with adjusted weights and enhanced nonlinear interactions
        total = 0.7 * tent_map + 1.5 * poly_potential + rbf_potential + 0.5 * steering_terms + 0.5 * fractal_terms + 0.3 * cross_terms + 0.2 * conditioning_terms
        
        # Add a new component to improve fitness: enhanced chaotic modulation with additional nonlinearities
        enhanced_chaos = 0.0
        for j in range(self.dim):
            enhanced_chaos += (self.tent_params[j] * np.abs(x[j] - self.tent_offsets[j]) - np.floor(self.tent_params[j] * np.abs(x[j] - self.tent_offsets[j]))) * np.exp(-0.1 * np.abs(x[j]))
        
        # Add a new component: hybrid polynomial and hyperbolic interaction with modified coefficients
        hybrid_terms = 0.0
        for j in range(self.dim):
            hybrid_terms += 1.2 * (x[j]**3) * np.tanh(0.4 * x[j]) + 0.8 * np.sinh(x[j]) + self.hybrid_coeffs[j] * np.log(1.0 + np.abs(x[j]))
        
        # Add a new component: hyperbolic interaction with additional coupling
        hyperbolic_terms = 0.0
        for j in range(self.dim):
            hyperbolic_terms += self.tanh_coeffs[j] * np.tanh(1.5 * x[j]) * np.cos(0.3 * x[j])
        
        # Add high frequency chaotic components
        high_freq_terms = 0.0
        for j in range(self.dim):
            high_freq_terms += self.high_freq_coeffs[j] * np.sin(self.high_freq_powers[j] * x[j]) * np.exp(-0.05 * x[j]**2)
        
        # Add multi-scale fractal interaction
        multi_scale_terms = 0.0
        for j in range(self.dim):
            multi_scale_terms += self.multi_scale_fractal[j] * (np.abs(x[j]) ** self.fractal_scales[j]) * np.cos(2.5 * x[j])
        
        # Final combination with refined weights to improve overall fitness
        total = 0.8 * tent_map + 1.8 * poly_potential + rbf_potential + 0.5 * steering_terms + 0.5 * fractal_terms + 0.3 * cross_terms + 0.2 * conditioning_terms + 0.3 * enhanced_chaos + 0.2 * hybrid_terms + 0.1 * hyperbolic_terms + 0.15 * high_freq_terms + 0.08 * multi_scale_terms
        
        # Introduce a large mutation: Increase the weight of chaotic components and add new interaction terms
        mutated_total = total + 0.3 * np.sum(np.sinh(x)) + 0.15 * np.sum(np.cos(x)**2) + 0.25 * np.sum(np.exp(-x**2))
        
        # Slight modification to increase difficulty: add a complex harmonic interaction term
        harmonic_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                harmonic_interaction += 0.2 * np.sin(3.0 * (x[i] + x[j])) * np.cos(2.0 * (x[i] - x[j]))
        
        mutated_total += harmonic_interaction
        
        # Add a new complex interaction term: multi-dimensional sinusoidal coupling with exponential decay
        complex_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                complex_coupling += 0.15 * np.sin(x[i] + x[j]) * np.exp(-0.3 * (x[i]**2 + x[j]**2)) * np.cos(0.2 * (x[i] - x[j]))
        
        mutated_total += complex_coupling
        
        return mutated_total