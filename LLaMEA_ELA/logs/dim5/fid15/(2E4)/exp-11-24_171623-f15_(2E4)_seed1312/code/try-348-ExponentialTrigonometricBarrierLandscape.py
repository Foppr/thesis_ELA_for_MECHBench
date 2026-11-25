import numpy as np

class ExponentialTrigonometricBarrierLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced exponential barrier parameters with multi-scale decay
        self.barrier_rates = 0.2 + 3.0 * np.random.rand(dim)
        self.barrier_heights = 0.5 + 4.0 * np.random.rand(dim)
        # Multi-frequency trigonometric coupling with phase shifts
        self.coupling_freqs = 0.5 + 5.0 * np.random.rand(dim, dim)
        self.coupling_amplitudes = 0.3 + 2.5 * np.random.rand(dim, dim)
        self.phase_shifts = np.pi * np.random.rand(dim, dim)
        # Advanced noise with fractal-like characteristics
        self.noise_scales = 0.2 + 3.0 * np.random.rand(dim)
        self.noise_frequencies = 0.05 + 4.0 * np.random.rand(dim)
        self.fractal_dims = 0.1 + 0.9 * np.random.rand(dim)
        # Variable conditioning with exponential scaling
        self.conditioning_factors = 0.05 + 2.5 * np.random.rand(dim)
        # Enhanced chaotic component with logistic map influence
        self.chaotic_coeffs = 0.05 + 0.7 * np.random.rand(dim)
        self.logistic_r = 3.8 + 0.4 * np.random.rand(dim)
        # Modified polynomial barriers with variable exponents
        self.poly_exponents = 1.5 + 4.0 * np.random.rand(dim)
        # Additional cubic barrier terms for increased complexity
        self.cubic_barrier_coeffs = 0.2 + 1.8 * np.random.rand(dim)
        # Higher-order cross-term coupling with tensor interactions
        self.cross_coupling_coeffs = 0.1 + 1.5 * np.random.rand(dim, dim, dim, dim)
        # New: Adaptive penalty mechanisms with dynamic thresholds
        self.penalty_thresholds = 0.3 + 2.0 * np.random.rand(dim)
        self.penalty_strengths = 0.5 + 2.0 * np.random.rand(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced exponential barrier component with multi-scale features
        barrier_sum = 0.0
        for i in range(self.dim):
            barrier_sum += self.barrier_heights[i] * np.exp(-self.barrier_rates[i] * np.abs(x_norm[i]))
        
        # Multi-frequency trigonometric coupling with phase shifts
        coupling_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_sum += (self.coupling_amplitudes[i, j] * 
                                   np.sin(self.coupling_freqs[i, j] * x_norm[i] + self.phase_shifts[i, j]) * 
                                   np.cos(self.coupling_freqs[i, j] * x_norm[j] + self.phase_shifts[i, j]))
        
        # Higher-order cross-dimensional coupling with fourth-order terms
        cross_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                for k in range(self.dim):
                    for l in range(self.dim):
                        if i != j and j != k and i != k and k != l:
                            cross_sum += self.cross_coupling_coeffs[i, j, k, l] * np.sin(x_norm[i]) * np.cos(x_norm[j]) * np.sin(x_norm[k]) * np.cos(x_norm[l])
        
        # Fractal-like noise component
        noise_sum = 0.0
        for i in range(self.dim):
            noise_sum += self.noise_scales[i] * (np.sin(self.noise_frequencies[i] * x_norm[i]) + 
                                                0.5 * np.cos(2 * self.noise_frequencies[i] * x_norm[i]) +
                                                0.3 * np.sin(3 * self.noise_frequencies[i] * x_norm[i]))
        
        # Enhanced chaotic component with logistic influence
        chaotic_sum = 0.0
        for i in range(self.dim):
            logistic_val = (self.logistic_r[i] * x_norm[i] * (1 - x_norm[i]))
            chaotic_sum += self.chaotic_coeffs[i] * np.sin(3 * x_norm[i]) * np.cos(5 * x_norm[i]) * logistic_val
        
        # Modified polynomial barrier with variable exponents
        poly_sum = 0.0
        for i in range(self.dim):
            poly_sum += np.power(np.abs(x_norm[i]), self.poly_exponents[i])
        
        # Cubic barrier terms for additional complexity
        cubic_sum = 0.0
        for i in range(self.dim):
            cubic_sum += self.cubic_barrier_coeffs[i] * np.power(x_norm[i], 3)
        
        # Combine components with varying weights
        result = 0.15 * barrier_sum + 0.2 * coupling_sum + 0.15 * cross_sum + 0.2 * noise_sum + 0.1 * chaotic_sum + 0.08 * poly_sum + 0.07 * cubic_sum
        
        # Apply exponential conditioning
        condition_factor = 1.0
        for i in range(self.dim):
            condition_factor *= np.exp(self.conditioning_factors[i] * np.abs(x_norm[i]))
        
        # Adaptive penalty with dynamic thresholds
        penalty = 0.0
        for i in range(self.dim):
            if np.abs(x_norm[i]) > self.penalty_thresholds[i]:
                penalty += self.penalty_strengths[i] * np.power(np.abs(x_norm[i]) - self.penalty_thresholds[i], 2)
        
        # Add global penalty term with cubic scaling
        global_penalty = 0.1 * np.sum(np.abs(x_norm)**4)
        
        return result * condition_factor + penalty + global_penalty