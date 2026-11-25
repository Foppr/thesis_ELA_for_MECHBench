import numpy as np

class SinusoidalPolynomialBarrierLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute sinusoidal wave parameters with higher frequency variation
        self.freqs = 3.0 + 8.0 * np.random.rand(dim)
        self.amps = 1.5 + 4.0 * np.random.rand(dim)
        # Precompute polynomial barrier coefficients with stronger nonlinearity
        self.barrier_coeffs = np.random.uniform(-4, 4, (dim, 7))
        # Precompute adaptive noise parameters with chaotic modulation
        self.noise_scales = 0.8 + 3.0 * np.random.rand(dim)
        # Precompute coupling weights with stronger interaction terms
        self.coupling_weights = np.random.uniform(-1.2, 1.2, (dim, dim))
        # Add phase shifts for enhanced complexity
        self.phase_shifts = np.random.uniform(0, 3*np.pi, dim)
        # Enhanced conditioning parameters to improve discrimination
        self.condition_factors = 2.0 + 1.2 * np.random.rand(dim)
        # Additional harmonic components for increased complexity
        self.harm_coeffs = np.random.uniform(-0.7, 0.7, (dim, 4))
        # Add time-varying parameters for dynamic behavior
        self.time_factors = 1.0 + 0.5 * np.random.rand(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced sinusoidal wave component with phase shifts and enhanced modulation
        sin_sum = 0.0
        for i in range(self.dim):
            sin_sum += self.amps[i] * np.sin(self.freqs[i] * x_norm[i] + self.phase_shifts[i]) * np.exp(-0.2 * x_norm[i]**2)
        
        # Enhanced polynomial barrier component with higher degree terms and nonlinearity
        poly_sum = 0.0
        for i in range(self.dim):
            coeffs = self.barrier_coeffs[i]
            poly_val = coeffs[0] + coeffs[1] * x_norm[i] + coeffs[2] * x_norm[i]**2 + coeffs[3] * x_norm[i]**3 + coeffs[4] * x_norm[i]**4 + coeffs[5] * x_norm[i]**5 + coeffs[6] * x_norm[i]**6
            poly_sum += poly_val * np.exp(-0.35 * x_norm[i]**2)
        
        # Enhanced coupling interaction component with cross-dimensional dependencies and improved scaling
        coupling_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling = self.coupling_weights[i, j] * (x_norm[i] - x_norm[j])**5
                    coupling_sum += coupling * np.exp(-0.4 * np.abs(coupling))
        
        # Enhanced noise component with chaotic interference patterns and additional modulation
        noise_sum = 0.0
        for i in range(self.dim):
            noise_sum += self.noise_scales[i] * np.sin(6 * x_norm[i]) * np.cos(5 * x_norm[i]) * np.exp(-0.25 * x_norm[i]**2)
        
        # Harmonic interaction terms for increased multimodality
        harm_sum = 0.0
        for i in range(self.dim):
            harm_sum += self.harm_coeffs[i, 0] * np.sin(4 * x_norm[i])**2 + \
                       self.harm_coeffs[i, 1] * np.cos(3 * x_norm[i])**2 + \
                       self.harm_coeffs[i, 2] * np.sin(2 * x_norm[i]) * np.cos(x_norm[i]) + \
                       self.harm_coeffs[i, 3] * np.sin(x_norm[i])**3
        
        # Combined landscape with enhanced dynamic weighting and improved scaling
        result = 0.3 * sin_sum + 0.35 * poly_sum + 0.25 * coupling_sum + 0.25 * noise_sum + 0.1 * harm_sum
        
        # Improved dynamic conditioning based on input magnitude, frequency characteristics, and condition factors
        condition_factor = 1.0
        for i in range(self.dim):
            freq_factor = 1.0 + 0.8 * np.abs(np.sin(self.freqs[i]))
            mag_factor = 1.0 + 0.7 * np.abs(x_norm[i])
            nonlin_factor = 1.0 + 0.6 * np.abs(x_norm[i])**5
            time_factor = self.time_factors[i]
            condition_factor *= (freq_factor * mag_factor + 0.5 * nonlin_factor) * self.condition_factors[i] * time_factor
        
        # Final transformation with enhanced penalty and global scaling to improve benchmark discrimination
        penalty = 0.4 * np.sum(np.abs(x_norm)**8)
        return result * condition_factor + penalty + 0.03 * np.sum(x_norm**10)