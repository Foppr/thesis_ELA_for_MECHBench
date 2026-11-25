import numpy as np

class SinusoidalPolynomialBarrierLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute sinusoidal wave parameters with higher frequency variation
        self.freqs = 2.0 + 6.0 * np.random.rand(dim)
        self.amps = 1.0 + 3.0 * np.random.rand(dim)
        # Precompute polynomial barrier coefficients with stronger nonlinearity
        self.barrier_coeffs = np.random.uniform(-3, 3, (dim, 6))
        # Precompute adaptive noise parameters with chaotic modulation
        self.noise_scales = 0.5 + 2.0 * np.random.rand(dim)
        # Precompute coupling weights with stronger interaction terms
        self.coupling_weights = np.random.uniform(-0.8, 0.8, (dim, dim))
        # Add phase shifts for enhanced complexity
        self.phase_shifts = np.random.uniform(0, 2*np.pi, dim)
        # Enhanced conditioning parameters to improve discrimination
        self.condition_factors = 1.5 + 0.8 * np.random.rand(dim)
        # Additional harmonic components for increased complexity
        self.harm_coeffs = np.random.uniform(-0.5, 0.5, (dim, 3))
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced sinusoidal wave component with phase shifts and enhanced modulation
        sin_sum = 0.0
        for i in range(self.dim):
            sin_sum += self.amps[i] * np.sin(self.freqs[i] * x_norm[i] + self.phase_shifts[i]) * np.exp(-0.15 * x_norm[i]**2)
        
        # Enhanced polynomial barrier component with higher degree terms and nonlinearity
        poly_sum = 0.0
        for i in range(self.dim):
            coeffs = self.barrier_coeffs[i]
            poly_val = coeffs[0] + coeffs[1] * x_norm[i] + coeffs[2] * x_norm[i]**2 + coeffs[3] * x_norm[i]**3 + coeffs[4] * x_norm[i]**4 + coeffs[5] * x_norm[i]**5
            poly_sum += poly_val * np.exp(-0.3 * x_norm[i]**2)
        
        # Enhanced coupling interaction component with cross-dimensional dependencies and improved scaling
        coupling_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling = self.coupling_weights[i, j] * (x_norm[i] - x_norm[j])**4
                    coupling_sum += coupling * np.exp(-0.3 * np.abs(coupling))
        
        # Enhanced noise component with chaotic interference patterns and additional modulation
        noise_sum = 0.0
        for i in range(self.dim):
            noise_sum += self.noise_scales[i] * np.sin(5 * x_norm[i]) * np.cos(4 * x_norm[i]) * np.exp(-0.2 * x_norm[i]**2)
        
        # Harmonic interaction terms for increased multimodality
        harm_sum = 0.0
        for i in range(self.dim):
            harm_sum += self.harm_coeffs[i, 0] * np.sin(3 * x_norm[i])**2 + \
                       self.harm_coeffs[i, 1] * np.cos(2 * x_norm[i])**2 + \
                       self.harm_coeffs[i, 2] * np.sin(x_norm[i]) * np.cos(x_norm[i])
        
        # Combined landscape with enhanced dynamic weighting and improved scaling
        result = 0.25 * sin_sum + 0.3 * poly_sum + 0.2 * coupling_sum + 0.2 * noise_sum + 0.05 * harm_sum
        
        # Improved dynamic conditioning based on input magnitude, frequency characteristics, and condition factors
        condition_factor = 1.0
        for i in range(self.dim):
            freq_factor = 1.0 + 0.6 * np.abs(np.sin(self.freqs[i]))
            mag_factor = 1.0 + 0.5 * np.abs(x_norm[i])
            nonlin_factor = 1.0 + 0.4 * np.abs(x_norm[i])**4
            condition_factor *= (freq_factor * mag_factor + 0.4 * nonlin_factor) * self.condition_factors[i]
        
        # Final transformation with enhanced penalty and global scaling to improve benchmark discrimination
        penalty = 0.3 * np.sum(np.abs(x_norm)**7)
        return result * condition_factor + penalty + 0.02 * np.sum(x_norm**9)