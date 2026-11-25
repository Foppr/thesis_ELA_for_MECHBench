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
        # Additional chaotic component with enhanced nonlinearity
        self.chaotic_coeffs = 0.1 + 0.5 * np.random.rand(dim)
        # New adaptive scaling factor
        self.adaptive_scale = 1.0 + 2.0 * np.random.rand()
        # New hyperparameter for enhanced multimodality
        self.multimodal_strength = 0.5 + 1.5 * np.random.rand()
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponential barrier component
        barrier_sum = 0.0
        for i in range(self.dim):
            barrier_sum += self.barrier_heights[i] * np.exp(-self.barrier_rates[i] * np.abs(x_norm[i]))
        
        # Trigonometric coupling between dimensions with enhanced interaction
        coupling_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_sum += (self.coupling_amplitudes[i, j] * 
                                   np.sin(self.coupling_freqs[i, j] * x_norm[i]) * 
                                   np.cos(self.coupling_freqs[i, j] * x_norm[j]) *
                                   np.exp(-0.5 * (x_norm[i] - x_norm[j])**2))
        
        # Adaptive noise component with enhanced complexity
        noise_sum = 0.0
        for i in range(self.dim):
            noise_sum += self.noise_scales[i] * (np.sin(self.noise_frequencies[i] * x_norm[i]) + 
                                                0.5 * np.cos(2 * self.noise_frequencies[i] * x_norm[i]) +
                                                0.3 * np.sin(3 * self.noise_frequencies[i] * x_norm[i]))
        
        # Chaotic component for enhanced complexity with polynomial terms
        chaotic_sum = 0.0
        for i in range(self.dim):
            chaotic_sum += self.chaotic_coeffs[i] * (np.sin(3 * x_norm[i]) * np.cos(5 * x_norm[i]) + 
                                                   0.1 * x_norm[i]**3)
        
        # Combine components with varying weights and enhanced multimodality
        result = 0.2 * barrier_sum + 0.3 * coupling_sum + 0.3 * noise_sum + 0.2 * chaotic_sum
        
        # Apply adaptive conditioning with enhanced nonlinearity
        condition_factor = 1.0
        for i in range(self.dim):
            condition_factor *= (1.0 + self.conditioning_factors[i] * np.abs(x_norm[i])**1.5)
        
        # Add global penalty term with enhanced complexity and multimodality
        penalty = 0.1 * np.sum(np.abs(x_norm)**4) + 0.05 * np.sum(x_norm**6) + \
                  self.multimodal_strength * np.sum(np.sin(5 * x_norm))
        
        # Apply adaptive scaling
        result = result * self.adaptive_scale
        
        return result * condition_factor + penalty