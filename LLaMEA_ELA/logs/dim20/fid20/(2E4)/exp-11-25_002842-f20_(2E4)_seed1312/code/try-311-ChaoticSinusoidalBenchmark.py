import numpy as np

class ChaoticSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic parameters for each dimension
        self.chaotic_params = np.random.uniform(1.5, 3.5, dim)
        # Periodic attractor frequencies
        self.freqs = np.random.uniform(1.5, 8.0, dim)
        # Amplitude modulation parameters (significantly modified)
        self.amp_modulation = np.random.uniform(0.5, 3.0, dim)
        # Phase shifts for each dimension
        self.phases = np.random.uniform(0, 2*np.pi, dim)
        # Local minima positions
        self.minima_positions = np.random.uniform(-5.0, 5.0, (dim, 9))
        # Dynamic scaling factors
        self.scaling = np.random.uniform(0.7, 2.0, dim)
        # Cross-dimensional interaction coefficients (enhanced)
        self.interaction_coeffs = np.random.uniform(-0.3, 0.3, (dim, dim))
        # Additional nonlinear term (enhanced)
        self.nonlinear_coeff = np.random.uniform(0.15, 0.9, dim)
        # Fractional Brownian motion scaling
        self.fbm_scaling = np.random.uniform(0.2, 1.2, dim)
        # Novel dynamic penalty coefficients
        self.penalty_coeffs = np.random.uniform(0.4, 1.8, dim)
        # High-order polynomial interaction terms
        self.poly_coeffs = np.random.uniform(-0.15, 0.15, (dim, dim, dim))
        # Stochastic perturbation terms
        self.stochastic_perturb = np.random.uniform(0.1, 0.5, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Chaotic sinusoidal component with enhanced complexity
        for i in range(self.dim):
            chaotic_term = np.sin(self.chaotic_params[i] * x[i])
            chaotic_term += 0.6 * np.sin(2 * self.chaotic_params[i] * x[i])
            chaotic_term += 0.4 * np.sin(3 * self.chaotic_params[i] * x[i])
            chaotic_term += 0.2 * np.sin(5 * self.chaotic_params[i] * x[i])
            chaotic_term += 0.1 * np.sin(7 * self.chaotic_params[i] * x[i])
            chaotic_term += 0.05 * np.sin(9 * self.chaotic_params[i] * x[i])
            result += chaotic_term ** 2
            
        # Periodic attractor component
        periodic_energy = 0.0
        for i in range(self.dim):
            freq_term = np.sin(self.freqs[i] * x[i] + self.phases[i])
            periodic_energy += freq_term ** 2
            
        # Amplitude modulation (modified with dynamic element)
        amp_modulation_energy = 0.0
        for i in range(self.dim):
            amp_mod = 1.0 + self.amp_modulation[i] * np.sin(x[i] * (1.0 + 0.2 * np.sin(2 * x[i])))
            amp_modulation_energy += amp_mod ** 2
            
        # Local minima attraction
        minima_energy = 0.0
        for i in range(self.dim):
            min_dist = np.min(np.abs(x[i] - self.minima_positions[i, :]))
            minima_energy += min_dist ** 2
            
        # Cross-dimensional interactions (enhanced)
        interaction_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    interaction_energy += self.interaction_coeffs[i, j] * x[i] * x[j]
                    
        # Additional nonlinear terms (enhanced)
        nonlinear_energy = 0.0
        for i in range(self.dim):
            nonlinear_energy += self.nonlinear_coeff[i] * x[i] ** 3
            
        # Fractional Brownian motion component
        fbm_energy = 0.0
        for i in range(self.dim):
            fbm_term = np.sin(x[i] * self.fbm_scaling[i])
            fbm_energy += fbm_term ** 2
            
        # Novel dynamic penalty mechanism
        penalty_energy = 0.0
        for i in range(self.dim):
            penalty_energy += self.penalty_coeffs[i] * (np.abs(x[i]) - 3.0) ** 4
            
        # High-order polynomial interactions
        poly_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                for k in range(self.dim):
                    if i != j and j != k and i != k:
                        poly_energy += self.poly_coeffs[i, j, k] * x[i] * x[j] * x[k]
        
        # Combine components with optimized weights
        total = 0.2 * result + 0.18 * periodic_energy + 0.16 * amp_modulation_energy + 0.12 * minima_energy + 0.1 * interaction_energy + 0.09 * nonlinear_energy + 0.08 * fbm_energy + 0.06 * penalty_energy + 0.05 * poly_energy
        
        # Apply dynamic scaling and stochastic perturbations
        for i in range(self.dim):
            total += self.scaling[i] * np.sin(x[i]) * np.cos(x[i])
            total += self.stochastic_perturb[i] * np.random.uniform(-0.1, 0.1)
            
        return total