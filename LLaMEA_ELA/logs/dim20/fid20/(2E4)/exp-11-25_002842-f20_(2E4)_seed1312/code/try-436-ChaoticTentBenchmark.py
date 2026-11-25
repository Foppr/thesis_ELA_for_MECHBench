import numpy as np

class ChaoticTentBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic parameter for sine map with dynamic transitions
        self.sine_params = np.random.uniform(3.0, 8.0, dim)
        # Trigonometric-polynomial coupling coefficients between dimensions
        self.trig_poly_coupling = np.random.uniform(-4.0, 4.0, (dim, dim))
        # Adaptive conditioning factors with extreme variability
        self.conditioning = np.random.uniform(0.02, 8.0, dim)
        # Phase shifts for trigonometric components
        self.phase_shifts = np.random.uniform(0, 12*np.pi, dim)
        # Polynomial degree for each dimension with higher values
        self.poly_degree = np.random.randint(5, 20, dim)
        # Amplitude scaling with greater variation
        self.amp_scaling = np.random.uniform(0.1, 5.0, dim)
        # Local minima positions with more diversity and clustering
        self.local_minima = np.random.uniform(-5.0, 5.0, (dim, 15))
        # Additional interaction terms with chaotic behavior
        self.interaction_coeffs = np.random.uniform(-3.0, 3.0, (dim, dim))
        # Dynamic parameter transitions with time-varying components
        self.transition_params = np.random.uniform(0.002, 0.5, dim)
        # Enhanced polynomial coupling coefficients
        self.poly_coupling = np.random.uniform(-3.0, 3.0, (dim, dim))
        # Modified interaction frequency with multi-scale oscillations
        self.freq_modifier = np.random.uniform(0.1, 4.0, dim)
        # Elastic energy terms for spatially varying ruggedness
        self.elastic_coeffs = np.random.uniform(-2.0, 2.0, (dim, dim))
        # Nonlinear chaotic feedback with memory effects
        self.feedback_params = np.random.uniform(0.05, 1.5, dim)
        # Multi-scale coupling with long-range interactions
        self.long_range_coupling = np.random.uniform(-0.8, 0.8, (dim, dim))
        # Additional chaotic coupling between dimensions
        self.chaotic_coupling = np.random.uniform(-1.5, 1.5, (dim, dim))
        # Non-separability enhancement through mixed trigonometric-polynomial terms
        self.mix_terms = np.random.uniform(-3.0, 3.0, (dim, dim))
        # Additional chaotic modulation with higher frequency components
        self.high_freq_mod = np.random.uniform(1.0, 6.0, dim)
        # Multi-modal peak structure with varying heights
        self.peak_heights = np.random.uniform(0.5, 3.0, dim)
        # Enhanced nonlinearity in the conditioning terms
        self.conditioning_nonlin = np.random.uniform(1.5, 4.0, dim)
        # Additional coupling through exponential interactions
        self.exp_coupling = np.random.uniform(-1.0, 1.0, (dim, dim))
        # Fractional polynomial terms for increased complexity
        self.frac_poly = np.random.uniform(0.2, 0.8, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Chaotic sine map oscillation with dynamic parameter transitions and feedback
        for i in range(self.dim):
            # Sine map with dynamic parameter and feedback
            param = self.sine_params[i] * (1 + 0.6 * np.sin(x[i] * self.feedback_params[i]))
            sine_value = np.sin(param * x[i])
            chaotic_term = param * sine_value
            result += self.amp_scaling[i] * np.sin(chaotic_term + self.phase_shifts[i]) ** 5
            
        # Trigonometric-polynomial coupling between dimensions with enhanced complexity
        trig_poly_coupling_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    trig_poly_coupling_energy += self.trig_poly_coupling[i, j] * np.sin(x[i] ** self.poly_degree[i]) * np.cos(x[j] ** (self.poly_degree[j] // 2))
                    
        # Adaptive conditioning with enhanced nonlinearity and chaos
        conditioning_energy = 0.0
        for i in range(self.dim):
            conditioning_energy += self.conditioning[i] * (x[i] ** 6) * np.sin(x[i] * self.conditioning_nonlin[i])
            
        # Local minima attraction with multiple candidates and clustering
        local_energy = 0.0
        for i in range(self.dim):
            min_dist = np.min(np.abs(x[i] - self.local_minima[i, :]))
            local_energy += min_dist ** 5
            
        # Additional interaction terms between dimensions with chaotic coupling and elastic effects
        interaction_energy = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction_energy += self.interaction_coeffs[i, j] * x[i] * x[j] * np.cos(x[i] * x[j]) + self.elastic_coeffs[i, j] * (x[i] - x[j]) ** 2
                
        # Enhanced polynomial coupling between dimensions with long-range effects
        poly_coupling_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    poly_coupling_energy += self.poly_coupling[i, j] * (x[i] ** (self.poly_degree[i] + 3)) * (x[j] ** 4) + self.long_range_coupling[i, j] * x[i] * np.log(1 + abs(x[j]))
                    
        # Modified interaction with frequency scaling and multi-scale components
        freq_interaction = 0.0
        for i in range(self.dim):
            freq_interaction += self.freq_modifier[i] * np.sin(x[i]) * np.cos(x[i] * 3) * np.exp(-abs(x[i])) + self.high_freq_mod[i] * np.sin(x[i] * 5)
            
        # Chaotic coupling between dimensions with additional nonlinearity
        chaotic_coupling_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    chaotic_coupling_energy += self.chaotic_coupling[i, j] * np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
                    
        # Mixed trigonometric-polynomial terms for increased non-separability
        mix_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    mix_energy += self.mix_terms[i, j] * np.sin(x[i]) * (x[j] ** 4) + np.cos(x[i]) * (x[j] ** 3)
        
        # Additional exponential coupling terms
        exp_energy = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exp_energy += self.exp_coupling[i, j] * np.exp(-abs(x[i] - x[j])) * (x[i] + x[j])
                
        # Fractional polynomial terms for increased complexity
        frac_energy = 0.0
        for i in range(self.dim):
            frac_energy += self.frac_poly[i] * (x[i] ** 1.5) * np.sin(x[i])
        
        # Combine components with weighted sum and chaotic weighting
        total = 0.10 * result + 0.15 * trig_poly_coupling_energy + 0.10 * conditioning_energy + 0.10 * local_energy + 0.10 * interaction_energy + 0.06 * poly_coupling_energy + 0.05 * freq_interaction + 0.07 * chaotic_coupling_energy + 0.03 * mix_energy + 0.04 * exp_energy + 0.02 * frac_energy
        
        return total