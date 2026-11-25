import numpy as np

class ChaoticExponentialTrigonometricLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic exponential potentials with sine-modulated rates and amplitudes
        self.potential_amplitudes = 1.0 + 9.0 * np.random.rand(dim)
        self.potential_rates = 0.1 + 5.0 * np.random.rand(dim)
        self.potential_chaos = 0.5 + 2.0 * np.random.rand(dim)
        # Multi-scale trigonometric coupling with chaotic frequency modulation
        self.coupling_frequencies = 0.5 + 8.0 * np.random.rand(dim, dim)
        self.coupling_amplitudes = 0.1 + 4.0 * np.random.rand(dim, dim)
        self.coupling_chaos = 0.2 + 1.5 * np.random.rand(dim, dim)
        # Fractal-like structure with chaotic scaling and power exponents
        self.fractal_scales = 0.05 + 3.0 * np.random.rand(dim)
        self.fractal_exponents = 0.1 + 2.0 * np.random.rand(dim)
        self.fractal_chaos = 0.3 + 1.2 * np.random.rand(dim)
        # Adaptive conditioning with chaotic logarithmic and power scaling
        self.conditioning_log_factors = 0.5 + 6.0 * np.random.rand(dim)
        self.conditioning_power_exponents = 0.1 + 4.0 * np.random.rand(dim)
        self.conditioning_chaos = 0.2 + 1.8 * np.random.rand(dim)
        # Cross-dimensional interference with chaotic amplitude and frequency
        self.interference_amplitudes = 1.0 + 5.0 * np.random.rand(dim)
        self.interference_frequencies = 1.0 + 10.0 * np.random.rand(dim)
        self.interference_chaos = 0.4 + 2.0 * np.random.rand(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic exponential potential component
        potential_sum = 0.0
        for i in range(self.dim):
            chaotic_factor = np.sin(self.potential_chaos[i] * x_norm[i])
            potential_sum += self.potential_amplitudes[i] * np.exp(-self.potential_rates[i] * np.abs(x_norm[i])) * (1.0 + 0.5 * chaotic_factor)
        
        # Multi-scale trigonometric coupling with chaos
        coupling_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    chaotic_factor = np.cos(self.coupling_chaos[i, j] * x_norm[i] * x_norm[j])
                    coupling_sum += self.coupling_amplitudes[i, j] * np.cos(self.coupling_frequencies[i, j] * x_norm[i] * x_norm[j]) * (1.0 + 0.3 * chaotic_factor)
        
        # Fractal-like self-similarity with chaos
        fractal_sum = 0.0
        for i in range(self.dim):
            chaotic_factor = np.sin(self.fractal_chaos[i] * x_norm[i])
            fractal_sum += self.fractal_scales[i] * np.power(np.abs(x_norm[i]), self.fractal_exponents[i]) * (1.0 + 0.4 * chaotic_factor)
        
        # Adaptive conditioning with chaotic scaling
        cond_sum = 0.0
        for i in range(self.dim):
            chaotic_factor = np.cos(self.conditioning_chaos[i] * x_norm[i])
            cond_sum += self.conditioning_log_factors[i] * np.log(1.0 + np.abs(x_norm[i])) * (1.0 + 0.2 * chaotic_factor)
        
        # Cross-dimensional interference with chaos
        interference_sum = 0.0
        for i in range(self.dim):
            chaotic_factor = np.sin(self.interference_chaos[i] * x_norm[i])
            interference_sum += self.interference_amplitudes[i] * np.sin(self.interference_frequencies[i] * x_norm[i]) * (1.0 + 0.3 * chaotic_factor)
        
        # Combine all components with adjusted weights
        result = 0.25 * potential_sum + 0.20 * coupling_sum + 0.25 * fractal_sum + 0.15 * cond_sum + 0.15 * interference_sum
        
        # Enhanced penalty term with chaotic and higher-order effects
        penalty = 0.20 * np.sum(np.abs(x_norm)**7) + 0.15 * np.sum(np.cos(6.0 * x_norm)) + 0.10 * np.sum(x_norm**5)
        
        # Additional chaotic correlation term
        if self.dim >= 2:
            correlation_term = 0.08 * np.sum((x_norm[:-1] - x_norm[1:])**4)
            result += correlation_term
            
        # Chaotic interaction between dimensions
        chaotic_interaction = 0.05 * np.sum(np.sin(3.0 * x_norm) * np.cos(2.0 * x_norm))
        result += chaotic_interaction
        
        return result + penalty