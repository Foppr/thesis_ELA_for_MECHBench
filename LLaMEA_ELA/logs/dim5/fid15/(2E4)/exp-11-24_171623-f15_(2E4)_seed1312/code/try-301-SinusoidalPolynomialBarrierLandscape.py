import numpy as np

class SinusoidalPolynomialBarrierLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic sinusoidal wave parameters with higher frequency modulation and additional harmonics
        self.freqs = np.exp(1.5 + 3.0 * np.random.rand(dim))
        self.amps = 3.0 + 4.0 * np.random.rand(dim)
        # Higher-order polynomial barrier coefficients (degree 9) with increased complexity and non-uniform terms
        self.barrier_coeffs = np.random.uniform(-3.0, 3.0, (dim, 10))
        # Cross-dimensional coupling with non-linear interaction weights including quintic and septic terms
        self.coupling_weights = np.random.uniform(-0.7, 0.7, (dim, dim))
        # Time-varying noise parameters with increased chaos, multi-frequency components, and phase shifts
        self.noise_scales = 3.0 + 3.5 * np.random.rand(dim)
        self.noise_freqs = 1.5 + 3.0 * np.random.rand(dim)
        self.noise_phases = 2 * np.pi * np.random.rand(dim)
        # Enhanced conditioning factors with greater variance and exponential scaling
        self.condition_factors = 0.3 + 1.2 * np.random.rand(dim)
        # Additional interaction terms with cubic and quartic coupling components
        self.cubic_coupling = np.random.uniform(-0.3, 0.3, (dim, dim))
        self.quartic_coupling = np.random.uniform(-0.2, 0.2, (dim, dim))
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced chaotic sinusoidal component with multiple frequency harmonics and phase shifts
        sin_sum = 0.0
        for i in range(self.dim):
            sin_sum += self.amps[i] * (np.sin(self.freqs[i] * x_norm[i]) + 
                                      0.4 * np.sin(2 * self.freqs[i] * x_norm[i]) + 
                                      0.15 * np.sin(3 * self.freqs[i] * x_norm[i]) +
                                      0.05 * np.sin(4 * self.freqs[i] * x_norm[i])) * np.exp(-0.2 * x_norm[i]**2)
        
        # High-order polynomial barrier with 9th degree terms and increased complexity
        poly_sum = 0.0
        for i in range(self.dim):
            coeffs = self.barrier_coeffs[i]
            poly_val = (coeffs[0] + coeffs[1] * x_norm[i] + coeffs[2] * x_norm[i]**2 + 
                       coeffs[3] * x_norm[i]**3 + coeffs[4] * x_norm[i]**4 + coeffs[5] * x_norm[i]**5 +
                       coeffs[6] * x_norm[i]**6 + coeffs[7] * x_norm[i]**7 + coeffs[8] * x_norm[i]**8 + coeffs[9] * x_norm[i]**9)
            poly_sum += poly_val * np.exp(-0.4 * x_norm[i]**2)
        
        # Non-linear coupling with cross-dimensional interaction including cubic and quartic terms
        coupling_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling = (self.coupling_weights[i, j] * (np.sin(x_norm[i] * x_norm[j]) * 
                                                              (x_norm[i]**2 + x_norm[j]**2) + 
                                                              0.3 * x_norm[i]**3 * x_norm[j]**3 +
                                                              0.1 * x_norm[i]**4 * x_norm[j]**4) +
                               self.cubic_coupling[i, j] * x_norm[i]**3 * x_norm[j] +
                               self.quartic_coupling[i, j] * x_norm[i]**2 * x_norm[j]**2)
                    coupling_sum += coupling * np.exp(-0.4 * (x_norm[i]**2 + x_norm[j]**2))
        
        # Enhanced dynamic noise with multi-frequency components, phase shifts, and increased chaos
        noise_sum = 0.0
        for i in range(self.dim):
            noise_sum += self.noise_scales[i] * (np.sin(self.noise_freqs[i] * x_norm[i] + self.noise_phases[i]) * 
                                                np.cos(self.noise_freqs[i] * x_norm[i] + self.noise_phases[i]) * 
                                                np.sin(2 * x_norm[i]) + 
                                                0.6 * np.sin(3 * self.noise_freqs[i] * x_norm[i] + self.noise_phases[i]))
        
        # Combined landscape with enhanced non-linearity
        result = 0.3 * sin_sum + 0.4 * poly_sum + 0.15 * coupling_sum + 0.15 * noise_sum
        
        # Enhanced dynamic conditioning with modified scaling and global penalty
        condition_factor = 1.0
        for i in range(self.dim):
            freq_factor = 1.0 + 0.8 * np.abs(np.sin(self.freqs[i]))
            mag_factor = 1.0 + 0.4 * np.abs(x_norm[i])
            cond_val = freq_factor * mag_factor * self.condition_factors[i]
            condition_factor *= cond_val
        
        # Enhanced global penalty with higher-order terms and additional complexity
        penalty = 0.3 * np.sum(np.abs(x_norm)**7)
        return result * condition_factor + penalty + 0.05 * np.sum(x_norm**10)