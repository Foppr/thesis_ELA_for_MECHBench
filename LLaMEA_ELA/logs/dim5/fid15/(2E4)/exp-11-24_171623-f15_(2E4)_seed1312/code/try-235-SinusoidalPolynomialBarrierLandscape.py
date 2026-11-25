import numpy as np

class SinusoidalPolynomialBarrierLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute sinusoidal wave parameters with higher frequency variation
        self.freqs = 1.0 + 4.0 * np.random.rand(dim)
        self.amps = 0.5 + 2.5 * np.random.rand(dim)
        # Precompute polynomial barrier coefficients with stronger nonlinearity
        self.barrier_coeffs = np.random.uniform(-2, 2, (dim, 5))
        # Precompute adaptive noise parameters with chaotic modulation
        self.noise_scales = 0.3 + 1.7 * np.random.rand(dim)
        # Precompute coupling weights with stronger interaction terms
        self.coupling_weights = np.random.uniform(-0.5, 0.5, (dim, dim))
        # Add phase shifts for enhanced complexity
        self.phase_shifts = np.random.uniform(0, 2*np.pi, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced sinusoidal wave component with phase shifts
        sin_sum = 0.0
        for i in range(self.dim):
            sin_sum += self.amps[i] * np.sin(self.freqs[i] * x_norm[i] + self.phase_shifts[i]) * np.exp(-0.15 * x_norm[i]**2)
        
        # Enhanced polynomial barrier component with higher degree terms
        poly_sum = 0.0
        for i in range(self.dim):
            coeffs = self.barrier_coeffs[i]
            poly_val = coeffs[0] + coeffs[1] * x_norm[i] + coeffs[2] * x_norm[i]**2 + coeffs[3] * x_norm[i]**3 + coeffs[4] * x_norm[i]**4
            poly_sum += poly_val * np.exp(-0.25 * x_norm[i]**2)
        
        # Enhanced coupling interaction component with cross-dimensional dependencies
        coupling_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling = self.coupling_weights[i, j] * (x_norm[i] - x_norm[j])**3
                    coupling_sum += coupling * np.exp(-0.3 * np.abs(coupling))
        
        # Enhanced noise component with chaotic interference patterns
        noise_sum = 0.0
        for i in range(self.dim):
            noise_sum += self.noise_scales[i] * np.sin(4 * x_norm[i]) * np.cos(3 * x_norm[i]) * np.exp(-0.1 * x_norm[i]**2)
        
        # Combined landscape with enhanced dynamic weighting
        result = 0.25 * sin_sum + 0.35 * poly_sum + 0.25 * coupling_sum + 0.15 * noise_sum
        
        # Improved dynamic conditioning based on input magnitude and frequency characteristics
        condition_factor = 1.0
        for i in range(self.dim):
            freq_factor = 1.0 + 0.6 * np.abs(np.sin(self.freqs[i]))
            mag_factor = 1.0 + 0.3 * np.abs(x_norm[i])
            nonlin_factor = 1.0 + 0.2 * np.abs(x_norm[i])**3
            condition_factor *= (freq_factor * mag_factor + 0.4 * nonlin_factor)
        
        # Final transformation with enhanced penalty and global scaling
        penalty = 0.15 * np.sum(np.abs(x_norm)**5)
        return result * condition_factor + penalty + 0.02 * np.sum(x_norm**7) - 0.05 * np.prod(np.abs(x_norm))