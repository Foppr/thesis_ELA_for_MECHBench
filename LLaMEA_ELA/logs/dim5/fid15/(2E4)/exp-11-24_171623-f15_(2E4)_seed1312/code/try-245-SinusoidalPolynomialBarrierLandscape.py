import numpy as np

class SinusoidalPolynomialBarrierLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic sinusoidal wave parameters with exponential growth
        self.freqs = np.exp(1.5 + 3.0 * np.random.rand(dim))
        self.amps = 3.0 + 4.0 * np.random.rand(dim)
        # Higher-order polynomial barrier coefficients (degree 7)
        self.barrier_coeffs = np.random.uniform(-3, 3, (dim, 8))
        # Cross-dimensional coupling with non-linear interaction weights
        self.coupling_weights = np.random.uniform(-0.8, 0.8, (dim, dim))
        # Time-varying noise parameters
        self.noise_scales = 2.0 + 3.0 * np.random.rand(dim)
        self.noise_freqs = 1.0 + 2.0 * np.random.rand(dim)
        # Adaptive conditioning factors
        self.condition_factors = 1.5 + 1.0 * np.random.rand(dim)
        # Additional chaotic modulation parameters
        self.modulation_freqs = 0.3 + 0.7 * np.random.rand(dim)
        self.modulation_amps = 1.0 + 2.0 * np.random.rand(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic sinusoidal component with exponential decay and modulation
        sin_sum = 0.0
        for i in range(self.dim):
            sin_component = self.amps[i] * np.sin(self.freqs[i] * x_norm[i]) * np.exp(-0.1 * x_norm[i]**2)
            modulation = self.modulation_amps[i] * np.cos(self.modulation_freqs[i] * x_norm[i])
            sin_sum += sin_component * (1.0 + 0.5 * modulation)
        
        # High-order polynomial barrier with 7th degree terms
        poly_sum = 0.0
        for i in range(self.dim):
            coeffs = self.barrier_coeffs[i]
            poly_val = (coeffs[0] + coeffs[1] * x_norm[i] + coeffs[2] * x_norm[i]**2 + 
                       coeffs[3] * x_norm[i]**3 + coeffs[4] * x_norm[i]**4 + coeffs[5] * x_norm[i]**5 +
                       coeffs[6] * x_norm[i]**6 + coeffs[7] * x_norm[i]**7)
            poly_sum += poly_val * np.exp(-0.15 * x_norm[i]**2)
        
        # Non-linear coupling with cross-dimensional interaction (modified interaction)
        coupling_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling = self.coupling_weights[i, j] * np.sin(x_norm[i] * x_norm[j]) * (x_norm[i]**4 + x_norm[j]**4)
                    coupling_sum += coupling * np.exp(-0.25 * (x_norm[i]**2 + x_norm[j]**2))
        
        # Dynamic noise with time-varying frequencies and amplitude scaling
        noise_sum = 0.0
        for i in range(self.dim):
            noise_component = self.noise_scales[i] * np.sin(self.noise_freqs[i] * x_norm[i]) * np.cos(self.noise_freqs[i] * x_norm[i])
            # Add additional chaotic modulation to noise
            noise_modulation = 0.5 * np.sin(2.0 * self.noise_freqs[i] * x_norm[i]) * np.cos(1.5 * self.noise_freqs[i] * x_norm[i])
            noise_sum += (noise_component + noise_modulation) * np.exp(-0.3 * x_norm[i]**2)
        
        # Combined landscape with enhanced non-linearity
        result = 0.3 * sin_sum + 0.4 * poly_sum + 0.15 * coupling_sum + 0.15 * noise_sum
        
        # Dynamic conditioning with exponential scaling and global penalty (modified penalty)
        condition_factor = 1.0
        for i in range(self.dim):
            freq_factor = 1.0 + 0.8 * np.abs(np.sin(self.freqs[i]))
            mag_factor = 1.0 + 0.4 * np.abs(x_norm[i])
            cond_val = freq_factor * mag_factor * self.condition_factors[i]
            condition_factor *= cond_val
        
        # Global penalty with higher-order terms (modified penalty)
        penalty = 0.3 * np.sum(np.abs(x_norm)**7)
        return result * condition_factor + penalty + 0.05 * np.sum(x_norm**9)