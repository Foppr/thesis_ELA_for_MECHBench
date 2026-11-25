import numpy as np

class ChaoticSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic parameters with higher variability
        self.chaotic_params = np.random.uniform(1.5, 4.0, dim)
        # Multi-scale frequencies for fractal-like behavior
        self.freqs = np.random.uniform(1.0, 10.0, dim)
        # Adaptive amplitude modulation with chaotic feedback
        self.amp_modulation = np.random.uniform(0.5, 3.5, dim)
        # Phase shifts with dynamic variation
        self.phases = np.random.uniform(0, 4*np.pi, dim)
        # Multiple local minima positions with clustering
        self.minima_positions = np.random.uniform(-5.0, 5.0, (dim, 12))
        # Dynamic scaling factors with exponential growth
        self.scaling = np.random.uniform(0.8, 2.5, dim)
        # Complex interaction coefficients with sparse connectivity
        self.interaction_coeffs = np.random.uniform(-0.5, 0.5, (dim, dim))
        # Nonlinear terms with higher-order polynomials
        self.nonlinear_coeff = np.random.uniform(0.2, 1.5, dim)
        # Fractional Brownian motion with varying Hurst exponents
        self.fbm_scaling = np.random.uniform(0.2, 1.8, dim)
        # Multi-level penalty coefficients with different exponents
        self.penalty_coeffs = np.random.uniform(0.6, 2.0, dim)
        # High-order polynomial interaction terms with sparse tensors
        self.poly_coeffs = np.random.uniform(-0.3, 0.3, (dim, dim, dim))
        # Fractal-like chaotic attractor coefficients
        self.fractal_coeffs = np.random.uniform(0.1, 0.9, dim)
        # Dynamic coupling strength between dimensions
        self.coupling_strength = np.random.uniform(0.4, 1.2, (dim, dim))
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Chaotic sinusoidal component with fractal-like structure
        for i in range(self.dim):
            chaotic_term = np.sin(self.chaotic_params[i] * x[i])
            chaotic_term += 0.7 * np.sin(2 * self.chaotic_params[i] * x[i])
            chaotic_term += 0.5 * np.sin(3 * self.chaotic_params[i] * x[i])
            chaotic_term += 0.3 * np.sin(5 * self.chaotic_params[i] * x[i])
            chaotic_term += 0.1 * np.sin(7 * self.chaotic_params[i] * x[i])
            chaotic_term += 0.05 * np.sin(9 * self.chaotic_params[i] * x[i])
            result += chaotic_term ** 2
            
        # Multi-scale periodic attractor component
        periodic_energy = 0.0
        for i in range(self.dim):
            freq_term = np.sin(self.freqs[i] * x[i] + self.phases[i])
            freq_term += 0.5 * np.sin(2 * self.freqs[i] * x[i] + self.phases[i])
            freq_term += 0.3 * np.sin(4 * self.freqs[i] * x[i] + self.phases[i])
            periodic_energy += freq_term ** 2
            
        # Adaptive amplitude modulation with feedback
        amp_modulation_energy = 0.0
        for i in range(self.dim):
            amp_mod = 1.0 + self.amp_modulation[i] * np.sin(x[i] * (1.0 + 0.2 * np.sin(3 * x[i])))
            amp_modulation_energy += amp_mod ** 2
            
        # Clustered local minima attraction
        minima_energy = 0.0
        for i in range(self.dim):
            min_dist = np.min(np.abs(x[i] - self.minima_positions[i, :]))
            minima_energy += min_dist ** 2
            
        # Sparse cross-dimensional interactions with dynamic coupling
        interaction_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j and np.random.rand() > 0.7:  # Sparse connectivity
                    interaction_energy += self.coupling_strength[i, j] * x[i] * x[j]
                    
        # Higher-order nonlinear terms
        nonlinear_energy = 0.0
        for i in range(self.dim):
            nonlinear_energy += self.nonlinear_coeff[i] * (x[i] ** 3 + 0.5 * x[i] ** 4)
            
        # Fractal Brownian motion component
        fbm_energy = 0.0
        for i in range(self.dim):
            fbm_term = np.sin(x[i] * self.fbm_scaling[i])
            fbm_term += 0.5 * np.sin(2 * x[i] * self.fbm_scaling[i])
            fbm_energy += fbm_term ** 2
            
        # Multi-level penalty mechanism
        penalty_energy = 0.0
        for i in range(self.dim):
            penalty_energy += self.penalty_coeffs[i] * (np.abs(x[i]) - 2.5) ** 5
            
        # High-order polynomial interactions with sparse tensor
        poly_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                for k in range(self.dim):
                    if i != j and j != k and i != k and np.random.rand() > 0.8:
                        poly_energy += self.poly_coeffs[i, j, k] * x[i] * x[j] * x[k]
        
        # Fractal-like chaotic attractor component
        fractal_energy = 0.0
        for i in range(self.dim):
            fractal_term = np.sin(self.fractal_coeffs[i] * x[i])
            fractal_term += 0.4 * np.sin(3 * self.fractal_coeffs[i] * x[i])
            fractal_energy += fractal_term ** 2
            
        # Combine components with new weights
        total = 0.3 * result + 0.2 * periodic_energy + 0.15 * amp_modulation_energy + 0.1 * minima_energy + 0.08 * interaction_energy + 0.07 * nonlinear_energy + 0.06 * fbm_energy + 0.04 * penalty_energy + 0.03 * poly_energy + 0.02 * fractal_energy
        
        # Apply dynamic scaling with chaotic modulation
        for i in range(self.dim):
            total += self.scaling[i] * np.sin(x[i]) * np.cos(x[i]) * np.sin(0.5 * x[i])
            
        return total