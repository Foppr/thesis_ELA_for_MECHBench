import numpy as np

class ExponentialTrigonometricBarrierLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced exponential barrier parameters with chaotic decay rates
        self.barrier_rates = 1.0 + 5.0 * np.random.rand(dim)
        self.barrier_heights = 2.0 + 4.0 * np.random.rand(dim)
        # Chaotic trigonometric coupling with non-linear frequency interactions
        self.coupling_freqs = 2.0 + 6.0 * np.random.rand(dim, dim)
        self.coupling_amplitudes = 1.0 + 3.0 * np.random.rand(dim, dim)
        # Dynamic noise parameters with time-varying scaling
        self.noise_scales = 1.0 + 4.0 * np.random.rand(dim)
        self.noise_frequencies = 0.5 + 5.0 * np.random.rand(dim)
        # Enhanced conditioning factors with exponential scaling
        self.conditioning_factors = 0.5 + 3.0 * np.random.rand(dim)
        # Additional chaotic component parameters
        self.chaos_params = 0.1 + 2.0 * np.random.rand(dim, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced exponential barrier component with chaotic modulation
        barrier_sum = 0.0
        for i in range(self.dim):
            barrier_sum += self.barrier_heights[i] * np.exp(-self.barrier_rates[i] * np.abs(x_norm[i]))
            # Add chaotic modulation to barriers
            chaos_mod = 0.0
            for j in range(self.dim):
                if i != j:
                    chaos_mod += self.chaos_params[i, j] * np.sin(self.coupling_freqs[i, j] * x_norm[j])
            barrier_sum += 0.5 * chaos_mod * np.exp(-self.barrier_rates[i] * np.abs(x_norm[i]))
        
        # Chaotic trigonometric coupling with non-linear interactions
        coupling_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_sum += (self.coupling_amplitudes[i, j] * 
                                   np.sin(self.coupling_freqs[i, j] * x_norm[i]) * 
                                   np.cos(self.coupling_freqs[i, j] * x_norm[j]) *
                                   np.tan(0.5 * self.coupling_freqs[i, j] * (x_norm[i] + x_norm[j])))
        
        # Dynamic noise component with multi-frequency modulation
        noise_sum = 0.0
        for i in range(self.dim):
            noise_sum += self.noise_scales[i] * (
                np.sin(self.noise_frequencies[i] * x_norm[i]) + 
                0.5 * np.cos(2 * self.noise_frequencies[i] * x_norm[i]) +
                0.3 * np.sin(3 * self.noise_frequencies[i] * x_norm[i]) +
                0.2 * np.cos(4 * self.noise_frequencies[i] * x_norm[i])
            )
        
        # Combine components with dynamic weights
        result = 0.3 * barrier_sum + 0.4 * coupling_sum + 0.3 * noise_sum
        
        # Enhanced adaptive conditioning with exponential scaling
        condition_factor = 1.0
        for i in range(self.dim):
            condition_factor *= (1.0 + self.conditioning_factors[i] * np.exp(self.conditioning_factors[i] * np.abs(x_norm[i])))
        
        # Add complex global penalty term with multiple polynomial components
        penalty = 0.3 * np.sum(np.abs(x_norm)**4) + 0.2 * np.sum(x_norm**6)
        
        return result * condition_factor + penalty