import numpy as np

class SinusoidalPolynomialBarrierLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic sinusoidal wave parameters with logarithmic scaling
        self.freqs = np.log(2.0 + 3.0 * np.random.rand(dim))
        self.amps = 1.5 + 4.0 * np.random.rand(dim)
        # Modified higher-order polynomial barrier coefficients (degree 6)
        self.barrier_coeffs = np.random.uniform(-1.5, 1.5, (dim, 7))
        # Improved cross-dimensional coupling with trigonometric interaction weights
        self.coupling_weights = np.random.uniform(-0.3, 0.3, (dim, dim))
        # Adaptive noise parameters with multi-frequency components
        self.noise_scales = 0.5 + 2.5 * np.random.rand(dim)
        self.noise_freqs = 0.2 + 2.0 * np.random.rand(dim)
        # Enhanced conditioning factors with exponential decay
        self.condition_factors = 0.5 + 1.5 * np.random.rand(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced chaotic sinusoidal component with inverse scaling
        sin_sum = 0.0
        for i in range(self.dim):
            sin_sum += self.amps[i] * np.sin(self.freqs[i] * x_norm[i]) * np.exp(-0.2 * x_norm[i]**2)
        
        # Modified high-order polynomial barrier with 6th degree terms
        poly_sum = 0.0
        for i in range(self.dim):
            coeffs = self.barrier_coeffs[i]
            poly_val = (coeffs[0] + coeffs[1] * x_norm[i] + coeffs[2] * x_norm[i]**2 + 
                       coeffs[3] * x_norm[i]**3 + coeffs[4] * x_norm[i]**4 + coeffs[5] * x_norm[i]**5 + 
                       coeffs[6] * x_norm[i]**6)
            poly_sum += poly_val * np.exp(-0.15 * x_norm[i]**2)
        
        # Improved non-linear coupling with cross-dimensional interaction (enhanced interaction)
        coupling_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling = self.coupling_weights[i, j] * np.cos(x_norm[i] * x_norm[j]) * (x_norm[i]**2 + x_norm[j]**2)
                    coupling_sum += coupling * np.exp(-0.25 * (x_norm[i]**2 + x_norm[j]**2))
        
        # Enhanced dynamic noise with multi-frequency components
        noise_sum = 0.0
        for i in range(self.dim):
            noise_sum += self.noise_scales[i] * np.sin(self.noise_freqs[i] * x_norm[i]) * np.sin(2.0 * self.noise_freqs[i] * x_norm[i])
        
        # Combined landscape with balanced non-linearity
        result = 0.3 * sin_sum + 0.3 * poly_sum + 0.25 * coupling_sum + 0.15 * noise_sum
        
        # Enhanced conditioning with logarithmic scaling and global penalty (improved penalty)
        condition_factor = 1.0
        for i in range(self.dim):
            freq_factor = 1.0 + 0.5 * np.abs(np.cos(self.freqs[i]))
            mag_factor = 1.0 + 0.2 * np.abs(x_norm[i])
            cond_val = freq_factor * mag_factor * self.condition_factors[i]
            condition_factor *= cond_val
        
        # Improved global penalty with mixed norms (revised penalty)
        penalty = 0.15 * np.sum(np.abs(x_norm)**7) + 0.05 * np.sum(x_norm**9)
        return result * condition_factor + penalty + 0.02 * np.sum(np.abs(x_norm)**10)