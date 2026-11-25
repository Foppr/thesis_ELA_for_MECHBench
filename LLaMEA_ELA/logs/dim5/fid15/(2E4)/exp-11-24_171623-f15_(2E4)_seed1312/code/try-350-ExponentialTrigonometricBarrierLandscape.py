import numpy as np

class ExponentialTrigonometricBarrierLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Exponential barrier parameters with varying decay rates
        self.barrier_rates = 0.5 + 2.0 * np.random.rand(dim)
        self.barrier_heights = 1.0 + 3.0 * np.random.rand(dim)
        # Trigonometric coupling coefficients with mixed frequencies
        self.coupling_freqs = 1.0 + 4.0 * np.random.rand(dim, dim)
        self.coupling_amplitudes = 0.5 + 2.0 * np.random.rand(dim, dim)
        # Adaptive noise parameters with dynamic scaling
        self.noise_scales = 0.5 + 2.5 * np.random.rand(dim)
        self.noise_frequencies = 0.1 + 3.0 * np.random.rand(dim)
        # Condition factors for variable conditioning
        self.conditioning_factors = 0.1 + 2.0 * np.random.rand(dim)
        # Modified chaotic component with different frequencies and coupling
        self.chaotic_coeffs = 0.2 + 0.6 * np.random.rand(dim)
        # Polynomial barrier modification with altered exponents
        self.poly_exponents = 1.5 + 4.0 * np.random.rand(dim)
        # New: Additional quadratic barrier terms for increased complexity
        self.quad_barrier_coeffs = 0.5 + 1.5 * np.random.rand(dim)
        # New: Cross-term coupling with higher-order interactions
        self.cross_coupling_coeffs = 0.3 + 1.2 * np.random.rand(dim, dim, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponential barrier component
        barrier_sum = 0.0
        for i in range(self.dim):
            barrier_sum += self.barrier_heights[i] * np.exp(-self.barrier_rates[i] * np.abs(x_norm[i]))
        
        # Trigonometric coupling between dimensions
        coupling_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_sum += (self.coupling_amplitudes[i, j] * 
                                   np.sin(self.coupling_freqs[i, j] * x_norm[i]) * 
                                   np.cos(self.coupling_freqs[i, j] * x_norm[j]))
        
        # Cross-dimensional coupling with third-order terms
        cross_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                for k in range(self.dim):
                    if i != j and j != k and i != k:
                        cross_sum += self.cross_coupling_coeffs[i, j, k] * np.sin(x_norm[i]) * np.cos(x_norm[j]) * np.sin(x_norm[k])
        
        # Adaptive noise component
        noise_sum = 0.0
        for i in range(self.dim):
            noise_sum += self.noise_scales[i] * (np.sin(self.noise_frequencies[i] * x_norm[i]) + 
                                                0.5 * np.cos(2 * self.noise_frequencies[i] * x_norm[i]))
        
        # Chaotic component for enhanced complexity
        chaotic_sum = 0.0
        for i in range(self.dim):
            chaotic_sum += self.chaotic_coeffs[i] * np.sin(4 * x_norm[i]) * np.cos(6 * x_norm[i])
        
        # Polynomial barrier modification
        poly_sum = 0.0
        for i in range(self.dim):
            poly_sum += np.power(np.abs(x_norm[i]), self.poly_exponents[i])
        
        # Quadratic barrier terms for additional complexity
        quad_sum = 0.0
        for i in range(self.dim):
            quad_sum += self.quad_barrier_coeffs[i] * np.power(x_norm[i], 2)
        
        # Combine components with modified weights
        result = 0.15 * barrier_sum + 0.3 * coupling_sum + 0.15 * cross_sum + 0.2 * noise_sum + 0.1 * chaotic_sum + 0.05 * poly_sum + 0.05 * quad_sum
        
        # Apply adaptive conditioning
        condition_factor = 1.0
        for i in range(self.dim):
            condition_factor *= (1.0 + self.conditioning_factors[i] * np.abs(x_norm[i]))
        
        # Add global penalty term
        penalty = 0.2 * np.sum(np.abs(x_norm)**3)
        
        return result * condition_factor + penalty