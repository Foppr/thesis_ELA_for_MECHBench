import numpy as np

class SinusoidalPolynomialBarrierLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic sinusoidal wave parameters with multi-scale frequencies and amplitude modulation
        self.freqs = np.exp(2.0 + 4.0 * np.random.rand(dim))
        self.amps = 5.0 + 5.0 * np.random.rand(dim)
        # Higher-order polynomial barrier coefficients (degree 9) with increased complexity
        self.barrier_coeffs = np.random.uniform(-5, 5, (dim, 10))
        # Cross-dimensional coupling with non-linear interaction weights and chaotic modulation
        self.coupling_weights = np.random.uniform(-2.0, 2.0, (dim, dim))
        # Time-varying noise parameters with chaotic behavior and multi-scale frequencies
        self.noise_scales = 3.0 + 4.0 * np.random.rand(dim)
        self.noise_freqs = 2.0 + 3.0 * np.random.rand(dim)
        # Adaptive conditioning factors with dynamic scaling and enhanced chaos
        self.condition_factors = 3.0 + 2.0 * np.random.rand(dim)
        # Additional chaotic modulation parameters with increased complexity
        self.modulation_coeffs = np.random.uniform(-1.0, 1.0, (dim, 4))
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic sinusoidal component with exponential decay and multi-scale modulation
        sin_sum = 0.0
        for i in range(self.dim):
            mod_term = (self.modulation_coeffs[i, 0] * np.sin(self.modulation_coeffs[i, 1] * x_norm[i]) + 
                       self.modulation_coeffs[i, 2] * np.cos(self.modulation_coeffs[i, 3] * x_norm[i]))
            sin_sum += self.amps[i] * np.sin(self.freqs[i] * x_norm[i]) * np.exp(-0.1 * x_norm[i]**2) * mod_term
        
        # High-order polynomial barrier with 9th degree terms and chaotic scaling
        poly_sum = 0.0
        for i in range(self.dim):
            coeffs = self.barrier_coeffs[i]
            poly_val = (coeffs[0] + coeffs[1] * x_norm[i] + coeffs[2] * x_norm[i]**2 + 
                       coeffs[3] * x_norm[i]**3 + coeffs[4] * x_norm[i]**4 + coeffs[5] * x_norm[i]**5 +
                       coeffs[6] * x_norm[i]**6 + coeffs[7] * x_norm[i]**7 + coeffs[8] * x_norm[i]**8 + coeffs[9] * x_norm[i]**9)
            poly_sum += poly_val * np.exp(-0.2 * x_norm[i]**2)
        
        # Non-linear coupling with cross-dimensional interaction and chaotic modulation
        coupling_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling = self.coupling_weights[i, j] * np.sin(x_norm[i] * x_norm[j]) * (x_norm[i]**5 + x_norm[j]**5)
                    coupling_sum += coupling * np.exp(-0.3 * (x_norm[i]**2 + x_norm[j]**2))
        
        # Dynamic noise with time-varying frequencies, amplitude scaling, and chaotic behavior
        noise_sum = 0.0
        for i in range(self.dim):
            noise_sum += self.noise_scales[i] * np.sin(self.noise_freqs[i] * x_norm[i]) * np.cos(self.noise_freqs[i] * x_norm[i]) * np.tan(0.5 * x_norm[i])
        
        # Combined landscape with enhanced non-linearity and chaotic behavior
        result = 0.25 * sin_sum + 0.35 * poly_sum + 0.3 * coupling_sum + 0.1 * noise_sum
        
        # Dynamic conditioning with exponential scaling and global penalty with chaotic components
        condition_factor = 1.0
        for i in range(self.dim):
            freq_factor = 1.0 + np.abs(np.sin(self.freqs[i])) + 0.5 * np.abs(np.cos(self.freqs[i]))
            mag_factor = 1.0 + 0.6 * np.abs(x_norm[i]) + 0.3 * np.abs(x_norm[i]**2)
            cond_val = freq_factor * mag_factor * self.condition_factors[i]
            condition_factor *= cond_val
        
        # Global penalty with higher-order terms and chaotic modulation
        penalty = 0.4 * np.sum(np.abs(x_norm)**8)
        return result * condition_factor + penalty + 0.1 * np.sum(x_norm**10)