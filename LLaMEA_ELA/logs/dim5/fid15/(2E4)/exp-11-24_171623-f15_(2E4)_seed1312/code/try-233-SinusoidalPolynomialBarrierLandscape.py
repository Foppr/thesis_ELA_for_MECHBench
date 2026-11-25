import numpy as np

class SinusoidalPolynomialBarrierLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute sinusoidal wave parameters
        self.freqs = 1.5 + 4.0 * np.random.rand(dim)
        self.amps = 0.5 + 2.5 * np.random.rand(dim)
        # Precompute polynomial barrier coefficients
        self.barrier_coeffs = np.random.uniform(-1.5, 1.5, (dim, 4))
        # Precompute adaptive noise parameters
        self.noise_scales = 0.3 + 1.7 * np.random.rand(dim)
        # Precompute coupling weights between dimensions
        self.coupling_weights = np.random.uniform(-0.5, 0.5, (dim, dim))
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Sinusoidal wave component with varying frequencies and amplitudes
        sin_sum = 0.0
        for i in range(self.dim):
            sin_sum += self.amps[i] * np.sin(self.freqs[i] * x_norm[i]) * np.exp(-0.15 * x_norm[i]**2)
        
        # Polynomial barrier component with dynamic coefficients
        poly_sum = 0.0
        for i in range(self.dim):
            coeffs = self.barrier_coeffs[i]
            poly_val = coeffs[0] + coeffs[1] * x_norm[i] + coeffs[2] * x_norm[i]**2 + coeffs[3] * x_norm[i]**3
            poly_sum += poly_val * np.exp(-0.25 * x_norm[i]**2)
        
        # Coupling interaction component with gradient-based weights
        coupling_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling = self.coupling_weights[i, j] * (x_norm[i] - x_norm[j])**3
                    coupling_sum += coupling * np.exp(-0.3 * np.abs(coupling))
        
        # Adaptive noise component with dimension-specific scaling
        noise_sum = 0.0
        for i in range(self.dim):
            noise_sum += self.noise_scales[i] * np.sin(4 * x_norm[i]) * np.cos(3 * x_norm[i])
        
        # Combined landscape with dynamic weighting
        result = 0.25 * sin_sum + 0.35 * poly_sum + 0.25 * coupling_sum + 0.15 * noise_sum
        
        # Dynamic conditioning based on input magnitude and frequency characteristics
        condition_factor = 1.0
        for i in range(self.dim):
            freq_factor = 1.0 + 0.6 * np.abs(np.sin(self.freqs[i]))
            mag_factor = 1.0 + 0.3 * np.abs(x_norm[i])
            condition_factor *= (freq_factor + 0.4 * mag_factor)
        
        # Final transformation with global scaling and penalty for large values
        penalty = 0.15 * np.sum(np.abs(x_norm)**5)
        return result * condition_factor + penalty + 0.02 * np.sum(x_norm**7)