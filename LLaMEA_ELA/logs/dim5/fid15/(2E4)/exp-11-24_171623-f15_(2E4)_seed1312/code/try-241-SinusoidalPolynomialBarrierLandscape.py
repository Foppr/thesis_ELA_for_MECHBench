import numpy as np

class SinusoidalPolynomialBarrierLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Precompute sinusoidal wave parameters with chaotic frequency modulation
        self.freqs = 2.0 + 8.0 * np.random.rand(dim)
        self.amps = 1.0 + 4.0 * np.random.rand(dim)
        # Precompute polynomial barrier coefficients with even stronger nonlinearity
        self.barrier_coeffs = np.random.uniform(-3, 3, (dim, 7))
        # Precompute adaptive noise parameters with chaotic modulation and temporal coupling
        self.noise_scales = 0.5 + 2.0 * np.random.rand(dim)
        # Precompute coupling weights with stronger interaction terms and directional bias
        self.coupling_weights = np.random.uniform(-1.0, 1.0, (dim, dim))
        # Add phase shifts for enhanced complexity with time-varying components
        self.phase_shifts = np.random.uniform(0, 4*np.pi, dim)
        # Enhanced conditioning parameters to improve discrimination
        self.condition_factors = 1.5 + 1.0 * np.random.rand(dim)
        # Add temporal modulation factors for dynamic noise
        self.temporal_factors = 0.8 + 0.4 * np.random.rand(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic sinusoidal wave component with phase shifts and enhanced modulation
        sin_sum = 0.0
        for i in range(self.dim):
            # Add temporal factor to frequency for dynamic behavior
            freq_mod = self.freqs[i] * (1.0 + 0.3 * np.sin(0.5 * x_norm[i]))
            sin_sum += self.amps[i] * np.sin(freq_mod * x_norm[i] + self.phase_shifts[i]) * np.exp(-0.2 * x_norm[i]**2)
        
        # Enhanced polynomial barrier component with higher degree terms and nonlinearity
        poly_sum = 0.0
        for i in range(self.dim):
            coeffs = self.barrier_coeffs[i]
            poly_val = (coeffs[0] + coeffs[1] * x_norm[i] + coeffs[2] * x_norm[i]**2 + 
                       coeffs[3] * x_norm[i]**3 + coeffs[4] * x_norm[i]**4 + 
                       coeffs[5] * x_norm[i]**5 + coeffs[6] * x_norm[i]**6)
            poly_sum += poly_val * np.exp(-0.3 * x_norm[i]**2)
        
        # Enhanced coupling interaction component with cross-dimensional dependencies, improved scaling, and directional bias
        coupling_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling = self.coupling_weights[i, j] * (x_norm[i] - x_norm[j])**4
                    coupling_sum += coupling * np.exp(-0.3 * np.abs(coupling))
        
        # Enhanced noise component with chaotic interference patterns, additional modulation, and temporal coupling
        noise_sum = 0.0
        for i in range(self.dim):
            noise_sum += self.noise_scales[i] * np.sin(6 * x_norm[i]) * np.cos(5 * x_norm[i]) * np.exp(-0.2 * x_norm[i]**2) * self.temporal_factors[i]
        
        # Combined landscape with enhanced dynamic weighting and improved scaling
        result = 0.25 * sin_sum + 0.35 * poly_sum + 0.2 * coupling_sum + 0.2 * noise_sum
        
        # Improved dynamic conditioning based on input magnitude, frequency characteristics, condition factors, and temporal components
        condition_factor = 1.0
        for i in range(self.dim):
            freq_factor = 1.0 + 0.7 * np.abs(np.sin(self.freqs[i]))
            mag_factor = 1.0 + 0.5 * np.abs(x_norm[i])
            nonlin_factor = 1.0 + 0.4 * np.abs(x_norm[i])**4
            temporal_factor = 1.0 + 0.2 * np.abs(np.sin(self.temporal_factors[i] * x_norm[i]))
            condition_factor *= (freq_factor * mag_factor + 0.4 * nonlin_factor) * self.condition_factors[i] * temporal_factor
        
        # Final transformation with enhanced penalty and global scaling to improve benchmark discrimination
        penalty = 0.3 * np.sum(np.abs(x_norm)**7)
        return result * condition_factor + penalty + 0.02 * np.sum(x_norm**9)