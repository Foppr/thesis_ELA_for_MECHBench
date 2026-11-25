import numpy as np

class SinusoidalPolynomialBarrierLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic sinusoidal wave parameters with higher frequency modulation
        self.freqs = np.exp(1.0 + 4.0 * np.random.rand(dim))
        self.amps = 4.0 + 5.0 * np.random.rand(dim)
        # Higher-order polynomial barrier coefficients (degree 11) with increased complexity
        self.barrier_coeffs = np.random.uniform(-4.0, 4.0, (dim, 12))
        # Cross-dimensional coupling with non-linear interaction weights and added septic terms
        self.coupling_weights = np.random.uniform(-0.8, 0.8, (dim, dim))
        # Time-varying noise parameters with increased chaos and multi-frequency components
        self.noise_scales = 4.0 + 4.5 * np.random.rand(dim)
        self.noise_freqs = 3.0 + 4.0 * np.random.rand(dim)
        # Enhanced conditioning factors with greater variance
        self.condition_factors = 0.2 + 1.5 * np.random.rand(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced chaotic sinusoidal component with multiple frequency harmonics
        sin_sum = 0.0
        for i in range(self.dim):
            sin_sum += self.amps[i] * (np.sin(self.freqs[i] * x_norm[i]) + 
                                      0.5 * np.sin(2 * self.freqs[i] * x_norm[i]) + 
                                      0.3 * np.sin(3 * self.freqs[i] * x_norm[i]) +
                                      0.1 * np.sin(5 * self.freqs[i] * x_norm[i]) +
                                      0.05 * np.sin(7 * self.freqs[i] * x_norm[i])) * np.exp(-0.25 * x_norm[i]**2)
        
        # High-order polynomial barrier with 11th degree terms and increased complexity
        poly_sum = 0.0
        for i in range(self.dim):
            coeffs = self.barrier_coeffs[i]
            poly_val = (coeffs[0] + coeffs[1] * x_norm[i] + coeffs[2] * x_norm[i]**2 + 
                       coeffs[3] * x_norm[i]**3 + coeffs[4] * x_norm[i]**4 + coeffs[5] * x_norm[i]**5 +
                       coeffs[6] * x_norm[i]**6 + coeffs[7] * x_norm[i]**7 + coeffs[8] * x_norm[i]**8 + 
                       coeffs[9] * x_norm[i]**9 + coeffs[10] * x_norm[i]**10 + coeffs[11] * x_norm[i]**11)
            poly_sum += poly_val * np.exp(-0.35 * x_norm[i]**2)
        
        # Non-linear coupling with cross-dimensional interaction including septic terms
        coupling_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling = self.coupling_weights[i, j] * (np.sin(x_norm[i] * x_norm[j]) * 
                                                              (x_norm[i]**2 + x_norm[j]**2) + 
                                                              0.4 * x_norm[i]**5 * x_norm[j]**5 +
                                                              0.2 * x_norm[i]**6 * x_norm[j]**6 +
                                                              0.1 * x_norm[i]**7 * x_norm[j]**7)
                    coupling_sum += coupling * np.exp(-0.35 * (x_norm[i]**2 + x_norm[j]**2))
        
        # Enhanced dynamic noise with multi-frequency components and increased chaos
        noise_sum = 0.0
        for i in range(self.dim):
            noise_sum += self.noise_scales[i] * (np.sin(self.noise_freqs[i] * x_norm[i]) * 
                                                np.cos(self.noise_freqs[i] * x_norm[i]) * 
                                                np.sin(2 * x_norm[i]) + 
                                                0.7 * np.sin(3 * self.noise_freqs[i] * x_norm[i]) +
                                                0.3 * np.sin(4 * self.noise_freqs[i] * x_norm[i]) +
                                                0.1 * np.sin(6 * self.noise_freqs[i] * x_norm[i]))
        
        # Combined landscape with enhanced non-linearity
        result = 0.25 * sin_sum + 0.45 * poly_sum + 0.18 * coupling_sum + 0.12 * noise_sum
        
        # Enhanced dynamic conditioning with modified scaling and global penalty
        condition_factor = 1.0
        for i in range(self.dim):
            freq_factor = 1.0 + 0.9 * np.abs(np.sin(self.freqs[i]))
            mag_factor = 1.0 + 0.5 * np.abs(x_norm[i])
            cond_val = freq_factor * mag_factor * self.condition_factors[i]
            condition_factor *= cond_val
        
        # Enhanced global penalty with higher-order terms
        penalty = 0.4 * np.sum(np.abs(x_norm)**8)
        return result * condition_factor + penalty + 0.07 * np.sum(x_norm**10)