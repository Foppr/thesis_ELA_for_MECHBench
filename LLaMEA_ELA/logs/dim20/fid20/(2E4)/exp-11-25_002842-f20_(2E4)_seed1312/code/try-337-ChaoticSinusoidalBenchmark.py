import numpy as np

class ChaoticSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic parameters with higher variability and nonlinearity
        self.chaotic_params = np.random.uniform(2.0, 5.0, dim)
        # Multi-scale frequencies for fractal-like behavior with exponential growth
        self.freqs = np.random.uniform(1.0, 15.0, dim)
        # Adaptive amplitude modulation with chaotic feedback and dynamic scaling
        self.amp_modulation = np.random.uniform(1.0, 4.0, dim)
        # Phase shifts with dynamic variation and periodic modulation
        self.phases = np.random.uniform(0, 6*np.pi, dim)
        # Multiple local minima positions with clustering and geometric distribution
        self.minima_positions = np.random.uniform(-5.0, 5.0, (dim, 15))
        # Dynamic scaling factors with exponential growth and chaotic variation
        self.scaling = np.random.uniform(1.0, 3.0, dim)
        # Complex interaction coefficients with sparse connectivity and directional coupling
        self.interaction_coeffs = np.random.uniform(-0.8, 0.8, (dim, dim))
        # Nonlinear terms with higher-order polynomials and chaotic feedback
        self.nonlinear_coeff = np.random.uniform(0.5, 2.0, dim)
        # Fractional Brownian motion with varying Hurst exponents and multi-fractal structure
        self.fbm_scaling = np.random.uniform(0.3, 2.2, dim)
        # Multi-level penalty coefficients with different exponents and chaotic modulation
        self.penalty_coeffs = np.random.uniform(1.0, 3.0, dim)
        # High-order polynomial interaction terms with sparse tensors and multi-dimensional coupling
        self.poly_coeffs = np.random.uniform(-0.5, 0.5, (dim, dim, dim, dim))
        # Fractal-like chaotic attractor coefficients with dynamic scaling and feedback loops
        self.fractal_coeffs = np.random.uniform(0.2, 1.0, dim)
        # Dynamic coupling strength between dimensions with time-varying weights
        self.coupling_strength = np.random.uniform(0.5, 1.5, (dim, dim))
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Chaotic sinusoidal component with fractal-like structure and higher-order harmonics
        for i in range(self.dim):
            chaotic_term = np.sin(self.chaotic_params[i] * x[i])
            chaotic_term += 0.8 * np.sin(2 * self.chaotic_params[i] * x[i])
            chaotic_term += 0.6 * np.sin(3 * self.chaotic_params[i] * x[i])
            chaotic_term += 0.4 * np.sin(5 * self.chaotic_params[i] * x[i])
            chaotic_term += 0.2 * np.sin(7 * self.chaotic_params[i] * x[i])
            chaotic_term += 0.1 * np.sin(9 * self.chaotic_params[i] * x[i])
            chaotic_term += 0.05 * np.sin(11 * self.chaotic_params[i] * x[i])
            result += chaotic_term ** 2
            
        # Multi-scale periodic attractor component with multiple harmonic combinations
        periodic_energy = 0.0
        for i in range(self.dim):
            freq_term = np.sin(self.freqs[i] * x[i] + self.phases[i])
            freq_term += 0.6 * np.sin(2 * self.freqs[i] * x[i] + self.phases[i])
            freq_term += 0.4 * np.sin(4 * self.freqs[i] * x[i] + self.phases[i])
            freq_term += 0.2 * np.sin(8 * self.freqs[i] * x[i] + self.phases[i])
            periodic_energy += freq_term ** 2
            
        # Adaptive amplitude modulation with feedback and chaotic variation
        amp_modulation_energy = 0.0
        for i in range(self.dim):
            amp_mod = 1.0 + self.amp_modulation[i] * np.sin(x[i] * (1.0 + 0.3 * np.sin(3 * x[i])))
            amp_modulation_energy += amp_mod ** 2
            
        # Clustered local minima attraction with enhanced clustering and geometric distribution
        minima_energy = 0.0
        for i in range(self.dim):
            min_dist = np.min(np.abs(x[i] - self.minima_positions[i, :]))
            minima_energy += min_dist ** 2
            
        # Sparse cross-dimensional interactions with dynamic coupling and directional bias
        interaction_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j and np.random.rand() > 0.6:  # Increased connectivity
                    interaction_energy += self.coupling_strength[i, j] * x[i] * x[j]
                    
        # Higher-order nonlinear terms with chaotic feedback and exponential growth
        nonlinear_energy = 0.0
        for i in range(self.dim):
            nonlinear_energy += self.nonlinear_coeff[i] * (x[i] ** 3 + 0.7 * x[i] ** 4 + 0.3 * x[i] ** 5)
            
        # Fractal Brownian motion component with multi-fractal structure and higher-order harmonics
        fbm_energy = 0.0
        for i in range(self.dim):
            fbm_term = np.sin(x[i] * self.fbm_scaling[i])
            fbm_term += 0.6 * np.sin(2 * x[i] * self.fbm_scaling[i])
            fbm_term += 0.3 * np.sin(4 * x[i] * self.fbm_scaling[i])
            fbm_energy += fbm_term ** 2
            
        # Multi-level penalty mechanism with chaotic modulation and higher-order exponents
        penalty_energy = 0.0
        for i in range(self.dim):
            penalty_energy += self.penalty_coeffs[i] * (np.abs(x[i]) - 3.0) ** 6
            
        # High-order polynomial interactions with sparse tensor and multi-dimensional coupling
        poly_energy = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                for k in range(self.dim):
                    for l in range(self.dim):
                        if i != j and j != k and i != k and i != l and j != l and k != l and np.random.rand() > 0.85:
                            poly_energy += self.poly_coeffs[i, j, k, l] * x[i] * x[j] * x[k] * x[l]
        
        # Fractal-like chaotic attractor component with enhanced complexity
        fractal_energy = 0.0
        for i in range(self.dim):
            fractal_term = np.sin(self.fractal_coeffs[i] * x[i])
            fractal_term += 0.5 * np.sin(3 * self.fractal_coeffs[i] * x[i])
            fractal_term += 0.2 * np.sin(9 * self.fractal_coeffs[i] * x[i])
            fractal_energy += fractal_term ** 2
            
        # Combine components with new weights and enhanced complexity
        total = 0.25 * result + 0.2 * periodic_energy + 0.18 * amp_modulation_energy + 0.12 * minima_energy + 0.09 * interaction_energy + 0.07 * nonlinear_energy + 0.06 * fbm_energy + 0.05 * penalty_energy + 0.04 * poly_energy + 0.03 * fractal_energy
        
        # Apply dynamic scaling with chaotic modulation and multi-dimensional feedback
        for i in range(self.dim):
            total += self.scaling[i] * np.sin(x[i]) * np.cos(x[i]) * np.sin(0.5 * x[i]) * np.cos(0.2 * x[i])
            
        return total