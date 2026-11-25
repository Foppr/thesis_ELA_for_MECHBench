import numpy as np

class RadialChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Radial basis function centers distributed across the domain
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (dim, 20))
        # Radial basis function widths with varying scales
        self.rbf_widths = np.random.uniform(0.5, 3.0, 20)
        # Chaotic phase modulators for each dimension
        self.phase_modulators = np.random.uniform(0.5, 2.0, dim)
        # Polynomial coupling coefficients between dimensions
        self.poly_coupling = np.random.uniform(-1.0, 1.0, (dim, dim))
        # Adaptive conditioning factors
        self.conditioning = np.random.uniform(0.1, 3.0, dim)
        # Chaos parameters for phase modulation
        self.chaos_params = np.random.uniform(3.5, 4.0, dim)
        # Interaction weights between dimensions
        self.interaction_weights = np.random.uniform(-0.5, 0.5, (dim, dim))
        # Exponent values for polynomial terms
        self.poly_exponents = np.random.randint(2, 6, dim)
        # Baseline noise scaling factors
        self.noise_scales = np.random.uniform(0.1, 0.5, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Radial basis function component
        rbf_sum = 0.0
        for i in range(20):
            dist = np.sum((x - self.rbf_centers[:, i]) ** 2)
            rbf_sum += np.exp(-dist / (2 * self.rbf_widths[i] ** 2))
        
        # Chaotic phase modulation component
        chaos_mod = 0.0
        for i in range(self.dim):
            # Logistic map for chaotic behavior
            chaos_val = self.chaos_params[i] * x[i] * (1 - x[i])
            phase_shift = np.sin(chaos_val * self.phase_modulators[i])
            chaos_mod += phase_shift * np.cos(x[i] ** 2)
            
        # Polynomial coupling between dimensions
        poly_coupling = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    poly_coupling += self.poly_coupling[i, j] * (x[i] ** self.poly_exponents[i]) * x[j]
                    
        # Adaptive conditioning
        cond_term = 0.0
        for i in range(self.dim):
            cond_term += self.conditioning[i] * (x[i] ** 4) * np.sin(x[i])
            
        # Interaction terms with weighted coupling
        interaction = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    interaction += self.interaction_weights[i, j] * x[i] * x[j] ** 2
                    
        # Noise component with chaotic scaling
        noise = 0.0
        for i in range(self.dim):
            noise += self.noise_scales[i] * np.sin(x[i] * (1 + np.sin(x[i])))
            
        # Combine all components with appropriate weights
        total = 0.3 * rbf_sum + 0.25 * chaos_mod + 0.2 * poly_coupling + 0.15 * cond_term + 0.08 * interaction + 0.02 * noise
        
        return total