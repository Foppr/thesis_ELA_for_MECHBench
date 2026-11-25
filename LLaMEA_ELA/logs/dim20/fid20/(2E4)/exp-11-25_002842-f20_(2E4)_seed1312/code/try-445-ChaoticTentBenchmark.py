import numpy as np

class ChaoticTentBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic parameter for sine map with dynamic transitions
        self.sine_params = np.random.uniform(2.0, 6.0, dim)
        # Trigonometric-polynomial coupling coefficients between dimensions
        self.trig_poly_coupling = np.random.uniform(-3.0, 3.0, (dim, dim))
        # Adaptive conditioning factors with extreme variability
        self.conditioning = np.random.uniform(0.05, 5.0, dim)
        # Phase shifts for trigonometric components
        self.phase_shifts = np.random.uniform(0, 8*np.pi, dim)
        # Polynomial degree for each dimension with higher values
        self.poly_degree = np.random.randint(4, 15, dim)
        # Amplitude scaling with greater variation
        self.amp_scaling = np.random.uniform(0.2, 4.0, dim)
        # Local minima positions with more diversity and clustering
        self.local_minima = np.random.uniform(-5.0, 5.0, (dim, 12))
        # Additional interaction terms with chaotic behavior
        self.interaction_coeffs = np.random.uniform(-2.0, 2.0, (dim, dim))
        # Dynamic parameter transitions with time-varying components
        self.transition_params = np.random.uniform(0.005, 0.3, dim)
        # Enhanced polynomial coupling coefficients
        self.poly_coupling = np.random.uniform(-2.0, 2.0, (dim, dim))
        # Modified interaction frequency with multi-scale oscillations
        self.freq_modifier = np.random.uniform(0.2, 3.0, dim)
        # Elastic energy terms for spatially varying ruggedness
        self.elastic_coeffs = np.random.uniform(-1.5, 1.5, (dim, dim))
        # Nonlinear chaotic feedback with memory effects
        self.feedback_params = np.random.uniform(0.1, 1.0, dim)
        # Multi-scale coupling with long-range interactions
        self.long_range_coupling = np.random.uniform(-0.5, 0.5, (dim, dim))
        # Additional chaotic modulation for increased complexity
        self.modulation_coeffs = np.random.uniform(0.5, 2.0, dim)
        # Modified chaotic sine map with additional sinusoidal feedback
        self.sine_feedback = np.random.uniform(0.1, 0.5, dim)
        # Enhanced interaction terms with cubic coupling and modified elastic energy
        self.cubic_interaction = np.random.uniform(-1.0, 1.0, (dim, dim))
        # New: Fractional chaos parameters for more complex dynamics
        self.frac_params = np.random.uniform(0.3, 1.7, dim)
        # New: Cross-dimensional interaction with hyperbolic functions
        self.hyperbolic_coupling = np.random.uniform(-1.0, 1.0, (dim, dim))
        # New: Memory-based chaotic terms using previous x values
        self.memory_weights = np.random.uniform(0.05, 0.5, dim)
        # New: Fractional Brownian motion parameters for multi-scale roughness
        self.fbm_params = np.random.uniform(0.1, 0.9, dim)
        # New: Quaternion-based coupling for higher-dimensional complexity
        self.quaternion_coupling = np.random.uniform(-1.0, 1.0, (dim, dim, dim))
        # New: Temporal chaos with time-delayed feedback
        self.delay_params = np.random.uniform(0.01, 0.2, dim)
        # New: Multi-modal Gaussian mixture components
        self.gaussian_means = np.random.uniform(-5.0, 5.0, (dim, 8))
        self.gaussian_vars = np.random.uniform(0.1, 2.0, (dim, 8))
        self.gaussian_weights = np.random.dirichlet(np.ones(8), dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Chaotic sine map oscillation with dynamic parameter transitions and feedback
        for i in range(self.dim):
            # Enhanced sine map with additional feedback term
            param = self.sine_params[i] * (1 + 0.4 * np.sin(x[i] * self.feedback_params[i]))
            sine_value = np.sin(param * x[i])
            chaotic_term = param * sine_value
            result += self.amp_scaling[i] * np.sin(chaotic_term + self.phase_shifts[i]) ** 4
            
        # Trigonometric-polynomial coupling between dimensions with enhanced complexity
        trig_poly_coupling_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    trig_poly_coupling_energy += self.trig_poly_coupling[i, j] * np.sin(x[i] ** self.poly_degree[i]) * np.cos(x[j] ** (self.poly_degree[j] // 2))
                    
        # Adaptive conditioning with enhanced nonlinearity and chaos
        conditioning_energy = 0.0
        for i in range(self.dim):
            conditioning_energy += self.conditioning[i] * (x[i] ** 5) * np.sin(x[i] * 2)
            
        # Local minima attraction with multiple candidates and clustering
        local_energy = 0.0
        for i in range(self.dim):
            min_dist = np.min(np.abs(x[i] - self.local_minima[i, :]))
            local_energy += min_dist ** 4
            
        # Additional interaction terms between dimensions with chaotic coupling and elastic effects
        interaction_energy = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Modified interaction with cubic coupling term
                interaction_energy += (self.interaction_coeffs[i, j] * x[i] * x[j] * np.cos(x[i] * x[j]) + 
                                     self.elastic_coeffs[i, j] * (x[i] - x[j]) ** 2 +
                                     self.cubic_interaction[i, j] * x[i] ** 3 * x[j])
                
        # Enhanced polynomial coupling between dimensions with long-range effects
        poly_coupling_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    poly_coupling_energy += self.poly_coupling[i, j] * (x[i] ** (self.poly_degree[i] + 2)) * (x[j] ** 3) + self.long_range_coupling[i, j] * x[i] * np.log(1 + abs(x[j]))
                    
        # Modified interaction with frequency scaling and multi-scale components
        freq_interaction = 0.0
        for i in range(self.dim):
            freq_interaction += self.freq_modifier[i] * np.sin(x[i]) * np.cos(x[i] * 2) * np.exp(-abs(x[i]))
            
        # Additional chaotic modulation term to increase landscape complexity
        modulation_energy = 0.0
        for i in range(self.dim):
            modulation_energy += self.modulation_coeffs[i] * np.sin(x[i] ** 3) * np.cos(x[i] * self.sine_params[i])
            
        # New: Hyperbolic coupling between dimensions
        hyperbolic_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    hyperbolic_energy += self.hyperbolic_coupling[i, j] * np.tanh(x[i]) * np.cosh(x[j])
                    
        # New: Memory-based chaotic terms
        memory_energy = 0.0
        for i in range(self.dim):
            memory_energy += self.memory_weights[i] * np.sin(x[i] * self.frac_params[i]) * np.cos(x[i] ** 2)
            
        # New: Fractional Brownian motion component for multi-scale roughness
        fbm_energy = 0.0
        for i in range(self.dim):
            fbm_energy += self.fbm_params[i] * np.sin(x[i] ** 2) * np.cos(x[i] * self.fbm_params[i])
            
        # New: Quaternion-based coupling component
        quaternion_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    for k in range(self.dim):
                        quaternion_energy += self.quaternion_coupling[i, j, k] * np.sin(x[i]) * np.cos(x[j]) * np.tan(x[k])
                        
        # New: Time-delayed chaotic feedback
        delay_energy = 0.0
        for i in range(self.dim):
            delay_energy += self.delay_params[i] * np.sin(x[i] - x[(i+1)%self.dim]) ** 2
            
        # New: Gaussian mixture components for multi-modal structure
        gaussian_energy = 0.0
        for i in range(self.dim):
            gauss_sum = 0.0
            for k in range(8):
                gauss_sum += self.gaussian_weights[i, k] * np.exp(-0.5 * ((x[i] - self.gaussian_means[i, k]) ** 2) / (self.gaussian_vars[i, k] ** 2))
            gaussian_energy += -np.log(gauss_sum)
        
        # Combine components with weighted sum and chaotic weighting
        total = 0.08 * result + 0.12 * trig_poly_coupling_energy + 0.10 * conditioning_energy + 0.13 * local_energy + 0.12 * interaction_energy + 0.10 * poly_coupling_energy + 0.05 * freq_interaction + 0.06 * modulation_energy + 0.05 * hyperbolic_energy + 0.03 * memory_energy + 0.04 * fbm_energy + 0.02 * quaternion_energy + 0.02 * delay_energy + 0.03 * gaussian_energy
        
        return total