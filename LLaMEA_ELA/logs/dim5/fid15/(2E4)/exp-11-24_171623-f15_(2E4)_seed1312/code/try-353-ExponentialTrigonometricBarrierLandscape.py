import numpy as np

class ExponentialTrigonometricBarrierLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced exponential barrier parameters with varied decay rates
        self.barrier_rates = 0.3 + 1.8 * np.random.rand(dim)
        self.barrier_heights = 1.2 + 2.8 * np.random.rand(dim)
        # Modified trigonometric coupling with higher frequencies and altered amplitudes
        self.coupling_freqs = 2.0 + 5.0 * np.random.rand(dim, dim)
        self.coupling_amplitudes = 0.3 + 1.7 * np.random.rand(dim, dim)
        # Enhanced adaptive noise with more complex frequency interactions
        self.noise_scales = 0.4 + 2.2 * np.random.rand(dim)
        self.noise_frequencies = 0.2 + 2.8 * np.random.rand(dim)
        # Improved conditioning factors with non-linear scaling
        self.conditioning_factors = 0.2 + 1.8 * np.random.rand(dim)
        # Enhanced chaotic component with modified frequencies and coupling
        self.chaotic_coeffs = 0.3 + 0.7 * np.random.rand(dim)
        # Modified polynomial barrier with variable exponents and cross-dimensional interactions
        self.poly_exponents = 2.0 + 3.5 * np.random.rand(dim)
        # Additional cubic barrier terms for increased complexity
        self.cubic_barrier_coeffs = 0.4 + 1.6 * np.random.rand(dim)
        # Cross-term coupling with higher-order polynomial interactions
        self.cross_coupling_coeffs = 0.2 + 1.0 * np.random.rand(dim, dim, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced exponential barrier component
        barrier_sum = 0.0
        for i in range(self.dim):
            barrier_sum += self.barrier_heights[i] * np.exp(-self.barrier_rates[i] * np.abs(x_norm[i]))
        
        # Modified trigonometric coupling between dimensions
        coupling_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_sum += (self.coupling_amplitudes[i, j] * 
                                   np.sin(self.coupling_freqs[i, j] * x_norm[i]) * 
                                   np.cos(self.coupling_freqs[i, j] * x_norm[j]))
        
        # Cross-dimensional coupling with third-order polynomial terms
        cross_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                for k in range(self.dim):
                    if i != j and j != k and i != k:
                        cross_sum += self.cross_coupling_coeffs[i, j, k] * np.sin(x_norm[i]) * np.cos(x_norm[j]) * np.power(x_norm[k], 3)
        
        # Enhanced adaptive noise component
        noise_sum = 0.0
        for i in range(self.dim):
            noise_sum += self.noise_scales[i] * (np.sin(self.noise_frequencies[i] * x_norm[i]) + 
                                                0.4 * np.cos(3 * self.noise_frequencies[i] * x_norm[i]) + 
                                                0.2 * np.sin(2 * self.noise_frequencies[i] * x_norm[i]))
        
        # Enhanced chaotic component
        chaotic_sum = 0.0
        for i in range(self.dim):
            chaotic_sum += self.chaotic_coeffs[i] * np.sin(5 * x_norm[i]) * np.cos(7 * x_norm[i])
        
        # Modified polynomial barrier with cross-dimensional interaction
        poly_sum = 0.0
        for i in range(self.dim):
            poly_sum += np.power(np.abs(x_norm[i]), self.poly_exponents[i])
        
        # Cubic barrier terms for additional complexity
        cubic_sum = 0.0
        for i in range(self.dim):
            cubic_sum += self.cubic_barrier_coeffs[i] * np.power(x_norm[i], 3)
        
        # Combine components with modified weights
        result = 0.2 * barrier_sum + 0.25 * coupling_sum + 0.15 * cross_sum + 0.2 * noise_sum + 0.1 * chaotic_sum + 0.05 * poly_sum + 0.05 * cubic_sum
        
        # Apply improved conditioning
        condition_factor = 1.0
        for i in range(self.dim):
            condition_factor *= (1.0 + self.conditioning_factors[i] * np.power(np.abs(x_norm[i]), 1.5))
        
        # Add global penalty term with enhanced non-linearity
        penalty = 0.3 * np.sum(np.abs(x_norm)**4)
        
        return result * condition_factor + penalty