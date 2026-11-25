import numpy as np

class ExponentialTrigonometricBarrierLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Exponential barrier parameters with varying decay rates
        self.barrier_rates = 0.3 + 1.8 * np.random.rand(dim)
        self.barrier_heights = 1.5 + 2.5 * np.random.rand(dim)
        # Trigonometric coupling coefficients with mixed frequencies
        self.coupling_freqs = 0.8 + 3.5 * np.random.rand(dim, dim)
        self.coupling_amplitudes = 0.3 + 1.8 * np.random.rand(dim, dim)
        # Adaptive noise parameters with dynamic scaling
        self.noise_scales = 0.3 + 2.2 * np.random.rand(dim)
        self.noise_frequencies = 0.05 + 2.8 * np.random.rand(dim)
        # Condition factors for variable conditioning
        self.conditioning_factors = 0.05 + 1.8 * np.random.rand(dim)
        # Additional chaotic components for enhanced complexity
        self.chaotic_coeffs = 0.05 + 1.3 * np.random.rand(dim)
        self.polynomial_orders = 2 + np.random.randint(3, size=dim)
        
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
        
        # Adaptive noise component
        noise_sum = 0.0
        for i in range(self.dim):
            noise_sum += self.noise_scales[i] * (np.sin(self.noise_frequencies[i] * x_norm[i]) + 
                                                0.3 * np.cos(2 * self.noise_frequencies[i] * x_norm[i]))
        
        # Chaotic polynomial components for additional complexity
        chaotic_sum = 0.0
        for i in range(self.dim):
            chaotic_sum += self.chaotic_coeffs[i] * np.sin(x_norm[i]**self.polynomial_orders[i])
        
        # Combine components with varying weights
        result = 0.25 * barrier_sum + 0.3 * coupling_sum + 0.2 * noise_sum + 0.25 * chaotic_sum
        
        # Apply adaptive conditioning
        condition_factor = 1.0
        for i in range(self.dim):
            condition_factor *= (1.0 + self.conditioning_factors[i] * np.abs(x_norm[i]))
        
        # Add global penalty term with higher weight to improve fitness
        penalty = 0.4 * np.sum(np.abs(x_norm)**3)
        
        return result * condition_factor + penalty