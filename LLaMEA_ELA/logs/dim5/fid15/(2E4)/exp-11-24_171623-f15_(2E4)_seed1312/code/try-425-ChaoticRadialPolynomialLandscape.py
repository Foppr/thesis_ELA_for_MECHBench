import numpy as np

class ChaoticRadialPolynomialLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic sine wave components with logistic map modulation
        self.chaotic_amplitudes = 3.0 + 5.0 * np.random.rand(dim)
        self.chaotic_frequencies = 8.0 + 20.0 * np.random.rand(dim)
        self.logistic_r = 3.9 + 0.1 * np.random.rand(dim)  # Logistic map parameter
        # Radial polynomial components with dynamic exponents
        self.rp_centers = 5.0 * np.random.rand(dim, 20) - 2.5
        self.rp_exponents = 2.0 + 6.0 * np.random.rand(20)
        # Cross-terms with dynamic coupling strengths and exponents
        self.cross_strengths = 2.0 + 4.0 * np.random.rand(dim, dim)
        self.cross_exponents = 1.0 + 4.0 * np.random.rand(dim, dim)
        # Adaptive conditioning factors with exponential scaling
        self.conditioning_factors = 1.0 + 3.0 * np.random.rand(dim)
        self.adaptive_scaling = 0.5 + 2.0 * np.random.rand(dim)
        # Asymmetric interaction terms with multi-modal coupling
        self.asymmetry_params = 0.2 + 1.8 * np.random.rand(dim)
        self.multi_modal_shifts = 2.0 * np.random.rand(dim) - 1.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic sine wave component with logistic modulation
        chaotic_sum = 0.0
        for i in range(self.dim):
            # Logistic map for dynamic modulation
            logistic_val = 1.0 / (1.0 + np.exp(-self.logistic_r[i] * (x_norm[i] - 0.5)))
            chaotic_sum += self.chaotic_amplitudes[i] * np.sin(self.chaotic_frequencies[i] * x_norm[i]) * logistic_val
        
        # Radial polynomial component
        rp_sum = 0.0
        for k in range(20):
            dist = 0.0
            for i in range(self.dim):
                dist += (x_norm[i] - self.rp_centers[i, k])**2
            rp_sum += np.power(dist + 1e-8, self.rp_exponents[k])
        
        # Cross-term interactions with dynamic coupling
        cross_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    # Dynamic coupling strength based on distance
                    dist_ij = np.abs(x_norm[i] - x_norm[j])
                    dynamic_strength = self.cross_strengths[i, j] * (1.0 + 0.5 * np.sin(dist_ij))
                    cross_sum += dynamic_strength * np.power(np.abs(x_norm[i] - x_norm[j]), self.cross_exponents[i, j])
        
        # Adaptive conditioning with exponential scaling
        cond_sum = 0.0
        for i in range(self.dim):
            cond_sum += self.conditioning_factors[i] * np.exp(self.adaptive_scaling[i] * (x_norm[i]**2)) + np.sin(5.0 * x_norm[i])
        
        # Multi-modal asymmetric coupling
        asym_sum = 0.0
        for i in range(self.dim):
            asym_factor = 1.0 + self.asymmetry_params[i] * np.cos(x_norm[i] + self.multi_modal_shifts[i])
            asym_sum += asym_factor * np.sin(2.0 * x_norm[i])**2
        
        # Combine all components
        result = 0.20 * chaotic_sum + 0.30 * rp_sum + 0.25 * cross_sum + 0.20 * cond_sum + 0.05 * asym_sum
        
        # Enhanced penalty term with cubic and quartic components
        penalty = 0.15 * np.sum(np.abs(x_norm)**4) + 0.05 * np.sum(x_norm**4)
        
        return result + penalty