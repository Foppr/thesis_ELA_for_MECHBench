import numpy as np

class ChaoticRadialPolynomialLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic sine wave components with logistic map modulation
        self.chaotic_amplitudes = 3.0 + 5.0 * np.random.rand(dim)
        self.chaotic_frequencies = 8.0 + 20.0 * np.random.rand(dim)
        self.logistic_r = 3.8 + 0.2 * np.random.rand(dim)  # Logistic map parameter
        # Radial polynomial components with varying degrees
        self.rp_centers = 5.0 * np.random.rand(dim, 12) - 2.5
        self.rp_degrees = 2 + np.random.randint(3, size=12)
        self.rp_weights = 0.5 + 2.0 * np.random.rand(12)
        # Cross-terms with dynamic coupling and time-dependent asymmetry
        self.cross_coupling = 2.0 + 4.0 * np.random.rand(dim, dim)
        self.cross_exponents = 1.0 + 3.0 * np.random.rand(dim, dim)
        # Adaptive conditioning with multi-scale factors
        self.adaptive_factors = 0.1 + 3.0 * np.random.rand(dim)
        self.scale_factors = 1.0 + 2.0 * np.random.rand(dim)
        # Asymmetric interaction with dynamic modulation
        self.modulation_params = 0.2 + 0.8 * np.random.rand(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic sine wave component using logistic map
        chaotic_sum = 0.0
        for i in range(self.dim):
            # Logistic map for chaotic modulation
            r = self.logistic_r[i]
            x_log = 0.5
            for _ in range(10):  # Iterate to stabilize
                x_log = r * x_log * (1 - x_log)
            chaotic_sum += self.chaotic_amplitudes[i] * np.sin(self.chaotic_frequencies[i] * x_norm[i]) * x_log
        
        # Radial polynomial component
        rp_sum = 0.0
        for k in range(12):
            dist = 0.0
            for i in range(self.dim):
                dist += (x_norm[i] - self.rp_centers[i, k])**2
            rp_sum += self.rp_weights[k] * np.power(dist, self.rp_degrees[k] / 2.0)
        
        # Cross-term interactions with dynamic coupling and modulation
        cross_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    mod_factor = 1.0 + self.modulation_params[i] * np.cos(x_norm[j])
                    cross_sum += self.cross_coupling[i, j] * np.power(np.abs(x_norm[i] - x_norm[j]), self.cross_exponents[i, j]) * mod_factor
        
        # Adaptive conditioning with multi-scale factors
        cond_sum = 0.0
        for i in range(self.dim):
            cond_sum += self.adaptive_factors[i] * (x_norm[i]**2 + self.scale_factors[i] * np.sin(5.0 * x_norm[i]))
        
        # Combine all components
        result = 0.30 * chaotic_sum + 0.25 * rp_sum + 0.20 * cross_sum + 0.25 * cond_sum
        
        # Enhanced penalty term with dynamic scaling
        penalty = 0.15 * np.sum(np.abs(x_norm)**4) + 0.05 * np.sum(np.abs(x_norm)**6)
        
        return result + penalty