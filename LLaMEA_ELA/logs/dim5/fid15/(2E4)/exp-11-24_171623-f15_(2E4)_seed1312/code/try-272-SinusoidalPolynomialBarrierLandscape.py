import numpy as np

class SinusoidalPolynomialBarrierLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic sinusoidal wave parameters with modified exponential growth
        self.freqs = np.exp(0.8 + 1.5 * np.random.rand(dim))
        self.amps = 1.5 + 2.5 * np.random.rand(dim)
        # Higher-order polynomial barrier coefficients (degree 5) with altered coefficients
        self.barrier_coeffs = np.random.uniform(-1.5, 1.5, (dim, 6))
        # Cross-dimensional coupling with modified non-linear interaction weights
        self.coupling_weights = np.random.uniform(-0.3, 0.3, (dim, dim))
        # Time-varying noise parameters with different scaling
        self.noise_scales = 0.8 + 1.2 * np.random.rand(dim)
        self.noise_freqs = 0.3 + 1.0 * np.random.rand(dim)
        # Adaptive conditioning factors with modified variance
        self.condition_factors = 0.8 + 0.4 * np.random.rand(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic sinusoidal component with modified exponential decay
        sin_sum = 0.0
        for i in range(self.dim):
            sin_sum += self.amps[i] * np.sin(self.freqs[i] * x_norm[i]) * np.exp(-0.1 * x_norm[i]**2)
        
        # High-order polynomial barrier with 5th degree terms and modified coefficients
        poly_sum = 0.0
        for i in range(self.dim):
            coeffs = self.barrier_coeffs[i]
            poly_val = (coeffs[0] + coeffs[1] * x_norm[i] + coeffs[2] * x_norm[i]**2 + 
                       coeffs[3] * x_norm[i]**3 + coeffs[4] * x_norm[i]**4 + coeffs[5] * x_norm[i]**5)
            poly_sum += poly_val * np.exp(-0.2 * x_norm[i]**2)
        
        # Non-linear coupling with cross-dimensional interaction (modified interaction)
        coupling_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling = self.coupling_weights[i, j] * np.sin(x_norm[i] * x_norm[j]) * (x_norm[i]**2 + x_norm[j]**2)
                    coupling_sum += coupling * np.exp(-0.25 * (x_norm[i]**2 + x_norm[j]**2))
        
        # Dynamic noise with time-varying frequencies and amplitude scaling
        noise_sum = 0.0
        for i in range(self.dim):
            noise_sum += self.noise_scales[i] * np.sin(self.noise_freqs[i] * x_norm[i]) * np.cos(self.noise_freqs[i] * x_norm[i])
        
        # Combined landscape with modified non-linearity
        result = 0.3 * sin_sum + 0.3 * poly_sum + 0.25 * coupling_sum + 0.15 * noise_sum
        
        # Dynamic conditioning with modified scaling and global penalty
        condition_factor = 1.0
        for i in range(self.dim):
            freq_factor = 1.0 + 0.5 * np.abs(np.sin(self.freqs[i]))
            mag_factor = 1.0 + 0.2 * np.abs(x_norm[i])
            cond_val = freq_factor * mag_factor * self.condition_factors[i]
            condition_factor *= cond_val
        
        # Global penalty with modified higher-order terms
        penalty = 0.15 * np.sum(np.abs(x_norm)**5)
        return result * condition_factor + penalty + 0.02 * np.sum(x_norm**7)