import numpy as np

class ChaoticRadialPolynomialLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Exponential decay potentials with varying rates and amplitudes
        self.potential_amplitudes = 1.5 + 6.0 * np.random.rand(dim)
        self.potential_rates = 0.3 + 3.0 * np.random.rand(dim)
        # Trigonometric coupling terms with multiple frequencies
        self.coupling_frequencies = 0.5 + 5.0 * np.random.rand(dim, dim)
        self.coupling_amplitudes = 0.3 + 2.5 * np.random.rand(dim, dim)
        # Fractal-like self-similarity structure with multiple scales
        self.fractal_scales = 0.05 + 1.5 * np.random.rand(dim)
        self.fractal_exponents = 0.2 + 1.5 * np.random.rand(dim)
        # Adaptive conditioning with logarithmic and power scaling
        self.conditioning_log_factors = 0.8 + 4.0 * np.random.rand(dim)
        self.conditioning_power_exponents = 0.3 + 2.5 * np.random.rand(dim)
        # Cross-dimensional interference patterns
        self.interference_amplitudes = 1.0 + 3.0 * np.random.rand(dim)
        self.interference_frequencies = 1.5 + 7.0 * np.random.rand(dim)
        # Chaotic sine wave component for increased complexity
        self.chaos_amplitudes = 0.5 + 2.0 * np.random.rand(dim)
        self.chaos_frequencies = 3.0 + 8.0 * np.random.rand(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponential decay potential component
        potential_sum = 0.0
        for i in range(self.dim):
            potential_sum += self.potential_amplitudes[i] * np.exp(-self.potential_rates[i] * np.abs(x_norm[i]))
        
        # Trigonometric coupling terms
        coupling_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_sum += self.coupling_amplitudes[i, j] * np.cos(self.coupling_frequencies[i, j] * x_norm[i] * x_norm[j])
        
        # Fractal-like self-similarity structure
        fractal_sum = 0.0
        for i in range(self.dim):
            fractal_sum += self.fractal_scales[i] * np.power(np.abs(x_norm[i]), self.fractal_exponents[i])
        
        # Adaptive conditioning component
        cond_sum = 0.0
        for i in range(self.dim):
            cond_sum += self.conditioning_log_factors[i] * np.log(1.0 + np.abs(x_norm[i]))
        
        # Cross-dimensional interference patterns
        interference_sum = 0.0
        for i in range(self.dim):
            interference_sum += self.interference_amplitudes[i] * np.sin(self.interference_frequencies[i] * x_norm[i])
        
        # Chaotic sine wave component
        chaos_sum = 0.0
        for i in range(self.dim):
            chaos_sum += self.chaos_amplitudes[i] * np.sin(self.chaos_frequencies[i] * x_norm[i] + np.sin(x_norm[i]))
        
        # Combine all components with adjusted weights
        result = 0.25 * potential_sum + 0.20 * coupling_sum + 0.18 * fractal_sum + 0.15 * cond_sum + 0.12 * interference_sum + 0.10 * chaos_sum
        
        # Add a complex penalty term based on higher-order moments and correlations
        penalty = 0.12 * np.sum(np.abs(x_norm)**6) + 0.08 * np.sum(np.cos(5.0 * x_norm)) + 0.04 * np.sum(x_norm**4)
        
        # Add a self-similarity correlation term for multi-scale complexity
        if self.dim >= 2:
            correlation_term = 0.03 * np.sum((x_norm[:-1] - x_norm[1:])**3)
            result += correlation_term
        
        return result + penalty