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
        self.noise_scales = 0.5 + 1.5 * np.random.rand(dim)
        # Precompute coupling weights with stronger interaction terms
        self.coupling_weights = np.random.uniform(-0.7, 0.7, (dim, dim))
        # Add phase shifts for enhanced complexity
        self.phase_shifts = np.random.uniform(0, 2*np.pi, dim)
        # Enhanced conditioning parameters to improve discrimination
        self.condition_factors = 1.2 + 0.3 * np.random.rand(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced sinusoidal wave component with phase shifts and enhanced modulation
        sin_sum = 0.0
        for i in range(self.dim):
            sin_sum += self.amps[i] * np.sin(self.freqs[i] * x_norm[i] + self.phase_shifts[i]) * np.exp(-0.1 * x_norm[i]**2)
        
        # Enhanced polynomial barrier component with higher degree terms and nonlinearity
        poly_sum = 0.0
        for i in range(self.dim):
            coeffs = self.barrier_coeffs[i]
            poly_val = coeffs[0] + coeffs[1] * x_norm[i] + coeffs[2] * x_norm[i]**2 + coeffs[3] * x_norm[i]**3 + coeffs[4] * x_norm[i]**4
            poly_sum += poly_val * np.exp(-0.2 * x_norm[i]**2)
        
        # Enhanced coupling interaction component with cross-dimensional dependencies and improved scaling
        coupling_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling = self.coupling_weights[i, j] * (x_norm[i] - x_norm[j])**3
                    coupling_sum += coupling * np.exp(-0.25 * np.abs(coupling))
        
        # Enhanced noise component with chaotic interference patterns and additional modulation
        noise_sum = 0.0
        for i in range(self.dim):
            noise_sum += self.noise_scales[i] * np.sin(4 * x_norm[i]) * np.cos(3 * x_norm[i]) * np.exp(-0.15 * x_norm[i]**2)
        
        # Combined landscape with enhanced dynamic weighting and improved scaling
        result = 0.3 * sin_sum + 0.3 * poly_sum + 0.2 * coupling_sum + 0.2 * noise_sum
        
        # Improved dynamic conditioning based on input magnitude, frequency characteristics, and condition factors
        condition_factor = 1.0
        for i in range(self.dim):
            freq_factor = 1.0 + 0.5 * np.abs(np.sin(self.freqs[i]))
            mag_factor = 1.0 + 0.4 * np.abs(x_norm[i])
            nonlin_factor = 1.0 + 0.3 * np.abs(x_norm[i])**3
            condition_factor *= (freq_factor * mag_factor + 0.3 * nonlin_factor) * self.condition_factors[i]
        
        # Final transformation with enhanced penalty and global scaling to improve benchmark discrimination
        penalty = 0.2 * np.sum(np.abs(x_norm)**6)
        return result * condition_factor + penalty + 0.01 * np.sum(x_norm**8)