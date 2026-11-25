import numpy as np

class ChaoticSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic parameters for each dimension with higher variability
        self.chaotic_params = np.random.uniform(1.5, 3.5, dim)
        # Periodic attractor frequencies with increased diversity
        self.freqs = np.random.uniform(3.0, 8.0, dim)
        # Amplitude modulation parameters with stronger coupling
        self.amp_modulation = np.random.uniform(1.0, 3.0, dim)
        # Phase shifts for each dimension
        self.phases = np.random.uniform(0, 2*np.pi, dim)
        # Local minima positions with clustered structure
        self.minima_positions = np.random.uniform(-5.0, 5.0, (dim, 5))
        # Dynamic scaling factors with exponential variation
        self.scaling = np.random.uniform(1.0, 2.0, dim)
        # Cross-dimensional interaction coefficients with sparse pattern
        self.interaction_coeffs = np.random.uniform(-0.5, 0.5, (dim, dim))
        # Additional nonlinear term with cubic scaling
        self.nonlinear_coeff = np.random.uniform(0.3, 1.0, dim)
        # Fractional Brownian motion scaling with irregular pattern
        self.fbm_scaling = np.random.uniform(0.3, 1.5, dim)
        # Novel dynamic penalty coefficients with asymmetric distribution
        self.penalty_coeffs = np.random.uniform(0.7, 2.0, dim)
        # High-order polynomial interaction terms with complex coupling
        self.poly_coeffs = np.random.uniform(-0.2, 0.2, (dim, dim, dim))
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Chaotic sinusoidal component with enhanced complexity
        for i in range(self.dim):
            chaotic_term = np.sin(self.chaotic_params[i] * x[i])
            chaotic_term += 0.7 * np.sin(2 * self.chaotic_params[i] * x[i])
            chaotic_term += 0.5 * np.sin(3 * self.chaotic_params[i] * x[i])
            chaotic_term += 0.3 * np.sin(5 * self.chaotic_params[i] * x[i])
            chaotic_term += 0.15 * np.sin(7 * self.chaotic_params[i] * x[i])
            result += chaotic_term ** 2
            
        # Periodic attractor component with increased frequency diversity
        periodic_energy = 0.0
        for i in range(self.dim):
            freq_term = np.sin(self.freqs[i] * x[i] + self.phases[i])
            periodic_energy += freq_term ** 2
            
        # Amplitude modulation with stronger coupling effects
        amp_modulation_energy = 0.0
        for i in range(self.dim):
            amp_mod = 1.0 + self.amp_modulation[i] * np.sin(x[i] * (1.0 + 0.2 * np.sin(2 * x[i])))
            amp_modulation_energy += amp_mod ** 2
            
        # Local minima attraction with clustering effect
        minima_energy = 0.0
        for i in range(self.dim):
            min_dist = np.min(np.abs(x[i] - self.minima_positions[i, :]))
            minima_energy += min_dist ** 2
            
        # Cross-dimensional interactions with sparse connectivity
        interaction_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j and np.random.rand() > 0.7:  # Sparse connections
                    interaction_energy += self.interaction_coeffs[i, j] * x[i] * x[j]
                    
        # Additional nonlinear terms with cubic scaling
        nonlinear_energy = 0.0
        for i in range(self.dim):
            nonlinear_energy += self.nonlinear_coeff[i] * x[i] ** 3
            
        # Fractional Brownian motion component with irregular scaling
        fbm_energy = 0.0
        for i in range(self.dim):
            fbm_term = np.sin(x[i] * self.fbm_scaling[i])
            fbm_energy += fbm_term ** 2
            
        # Novel dynamic penalty mechanism with asymmetric distribution
        penalty_energy = 0.0
        for i in range(self.dim):
            penalty_energy += self.penalty_coeffs[i] * (np.abs(x[i]) - 3.0) ** 4
            
        # High-order polynomial interactions with complex coupling
        poly_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                for k in range(self.dim):
                    if i != j and j != k and i != k and np.random.rand() > 0.8:  # Sparse connections
                        poly_energy += self.poly_coeffs[i, j, k] * x[i] * x[j] * x[k]
        
        # Combine components with optimized weights for better conditioning
        total = 0.3 * result + 0.25 * periodic_energy + 0.18 * amp_modulation_energy + 0.12 * minima_energy + 0.08 * interaction_energy + 0.06 * nonlinear_energy + 0.05 * fbm_energy + 0.04 * penalty_energy + 0.02 * poly_energy
        
        # Apply dynamic scaling with enhanced nonlinearity
        for i in range(self.dim):
            total += self.scaling[i] * np.sin(x[i]) * np.cos(x[i])
            
        return total