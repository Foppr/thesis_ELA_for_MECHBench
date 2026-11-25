import numpy as np

class ExponentialTrigonometricBarrierLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Hyperchaotic barrier parameters with fractal-like decay rates
        self.barrier_rates = 1.0 + 4.0 * np.random.rand(dim)
        self.barrier_heights = 2.0 + 5.0 * np.random.rand(dim)
        # Enhanced trigonometric coupling with multi-frequency interactions
        self.coupling_freqs = 2.0 + 8.0 * np.random.rand(dim, dim)
        self.coupling_amplitudes = 1.0 + 3.0 * np.random.rand(dim, dim)
        # Hyperchaotic noise parameters with fractal scaling
        self.noise_scales = 1.0 + 4.0 * np.random.rand(dim)
        self.noise_frequencies = 0.5 + 6.0 * np.random.rand(dim)
        # Enhanced conditioning factors with exponential scaling
        self.conditioning_factors = 0.5 + 3.0 * np.random.rand(dim)
        # Hyperchaotic polynomial components with higher-order terms
        self.chaotic_coeffs = 0.2 + 1.0 * np.random.rand(dim)
        # Multi-scale adaptive parameters
        self.adaptive_scale = 2.0 + 3.0 * np.random.rand()
        self.multi_scale_factors = 0.1 + 1.5 * np.random.rand(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Hyperchaotic barrier component with fractal characteristics
        barrier_sum = 0.0
        for i in range(self.dim):
            barrier_sum += self.barrier_heights[i] * np.exp(-self.barrier_rates[i] * np.abs(x_norm[i])) * \
                          (1.0 + 0.5 * np.sin(10 * x_norm[i]) + 0.3 * np.cos(15 * x_norm[i]))
        
        # Enhanced trigonometric coupling with multi-scale interactions
        coupling_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_sum += (self.coupling_amplitudes[i, j] * 
                                   np.sin(self.coupling_freqs[i, j] * x_norm[i]) * 
                                   np.cos(self.coupling_freqs[i, j] * x_norm[j]) *
                                   np.exp(-0.3 * (x_norm[i] - x_norm[j])**2) *
                                   (1.0 + 0.2 * np.sin(5 * (x_norm[i] + x_norm[j]))))
        
        # Hyperchaotic noise component with multi-fractal characteristics
        noise_sum = 0.0
        for i in range(self.dim):
            noise_sum += self.noise_scales[i] * (
                np.sin(self.noise_frequencies[i] * x_norm[i]) + 
                0.5 * np.cos(2 * self.noise_frequencies[i] * x_norm[i]) +
                0.3 * np.sin(3 * self.noise_frequencies[i] * x_norm[i]) +
                0.1 * np.cos(4 * self.noise_frequencies[i] * x_norm[i]) +
                0.05 * np.sin(7 * self.noise_frequencies[i] * x_norm[i])
            )
        
        # Hyperchaotic polynomial component with higher-order terms
        chaotic_sum = 0.0
        for i in range(self.dim):
            chaotic_sum += self.chaotic_coeffs[i] * (
                np.sin(3 * x_norm[i]) * np.cos(5 * x_norm[i]) + 
                0.1 * x_norm[i]**3 +
                0.05 * x_norm[i]**5 +
                0.02 * np.sin(10 * x_norm[i])
            )
        
        # Combine components with enhanced weights
        result = 0.2 * barrier_sum + 0.35 * coupling_sum + 0.25 * noise_sum + 0.2 * chaotic_sum
        
        # Enhanced adaptive conditioning with multi-scale factors
        condition_factor = 1.0
        for i in range(self.dim):
            condition_factor *= (1.0 + self.conditioning_factors[i] * np.abs(x_norm[i])**2.5 + 
                               self.multi_scale_factors[i] * np.abs(x_norm[i])**3.5)
        
        # Augmented global penalty term with hyperchaotic components
        penalty = 0.2 * np.sum(np.abs(x_norm)**4) + 0.1 * np.sum(x_norm**6) + \
                 0.05 * np.sum(np.sin(5 * x_norm)**2)
        
        # Apply multi-scale adaptive scaling
        result = result * self.adaptive_scale
        
        return result * condition_factor + penalty