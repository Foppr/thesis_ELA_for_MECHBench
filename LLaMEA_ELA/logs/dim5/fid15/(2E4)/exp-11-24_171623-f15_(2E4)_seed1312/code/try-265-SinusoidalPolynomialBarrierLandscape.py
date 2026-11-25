import numpy as np

class SinusoidalPolynomialBarrierLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic sinusoidal wave parameters with exponential growth
        self.freqs = np.exp(1.0 + 2.0 * np.random.rand(dim))
        self.amps = 2.0 + 3.0 * np.random.rand(dim)
        # Higher-order polynomial barrier coefficients (degree 5)
        self.barrier_coeffs = np.random.uniform(-2, 2, (dim, 6))
        # Cross-dimensional coupling with non-linear interaction weights
        self.coupling_weights = np.random.uniform(-0.5, 0.5, (dim, dim))
        # Time-varying noise parameters
        self.noise_scales = 1.0 + 2.0 * np.random.rand(dim)
        self.noise_freqs = 0.5 + 1.5 * np.random.rand(dim)
        # Adaptive conditioning factors
        self.condition_factors = 1.0 + 0.5 * np.random.rand(dim)
        # Additional chaotic modulation components
        self.modulation_coeffs = np.random.uniform(-1.0, 1.0, (dim, 4))
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic sinusoidal component with exponential decay
        sin_sum = 0.0
        for i in range(self.dim):
            sin_sum += self.amps[i] * np.sin(self.freqs[i] * x_norm[i]) * np.exp(-0.15 * x_norm[i]**2)
        
        # High-order polynomial barrier with 5th degree terms
        poly_sum = 0.0
        for i in range(self.dim):
            coeffs = self.barrier_coeffs[i]
            poly_val = (coeffs[0] + coeffs[1] * x_norm[i] + coeffs[2] * x_norm[i]**2 + 
                       coeffs[3] * x_norm[i]**3 + coeffs[4] * x_norm[i]**4 + coeffs[5] * x_norm[i]**5)
            poly_sum += poly_val * np.exp(-0.25 * x_norm[i]**2)
        
        # Non-linear coupling with cross-dimensional interaction (modified interaction)
        coupling_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling = self.coupling_weights[i, j] * np.sin(x_norm[i] * x_norm[j]) * (x_norm[i]**3 + x_norm[j]**3)
                    coupling_sum += coupling * np.exp(-0.3 * (x_norm[i]**2 + x_norm[j]**2))
        
        # Dynamic noise with time-varying frequencies and amplitude scaling
        noise_sum = 0.0
        for i in range(self.dim):
            noise_sum += self.noise_scales[i] * np.sin(self.noise_freqs[i] * x_norm[i]) * np.cos(self.noise_freqs[i] * x_norm[i])
        
        # Additional chaotic modulation components
        mod_sum = 0.0
        for i in range(self.dim):
            mod_val = (self.modulation_coeffs[i, 0] * np.sin(x_norm[i]**2) + 
                      self.modulation_coeffs[i, 1] * np.cos(x_norm[i]**3) +
                      self.modulation_coeffs[i, 2] * np.tan(x_norm[i]) +
                      self.modulation_coeffs[i, 3] * np.log(np.abs(x_norm[i]) + 1.0))
            mod_sum += mod_val * np.exp(-0.1 * x_norm[i]**2)
        
        # Combined landscape with enhanced non-linearity
        result = 0.25 * sin_sum + 0.35 * poly_sum + 0.2 * coupling_sum + 0.2 * noise_sum + 0.05 * mod_sum
        
        # Dynamic conditioning with exponential scaling and global penalty (modified penalty)
        condition_factor = 1.0
        for i in range(self.dim):
            freq_factor = 1.0 + 0.7 * np.abs(np.sin(self.freqs[i]))
            mag_factor = 1.0 + 0.3 * np.abs(x_norm[i])
            cond_val = freq_factor * mag_factor * self.condition_factors[i]
            condition_factor *= cond_val
        
        # Global penalty with higher-order terms (modified penalty)
        penalty = 0.2 * np.sum(np.abs(x_norm)**6)
        return result * condition_factor + penalty + 0.03 * np.sum(x_norm**8)