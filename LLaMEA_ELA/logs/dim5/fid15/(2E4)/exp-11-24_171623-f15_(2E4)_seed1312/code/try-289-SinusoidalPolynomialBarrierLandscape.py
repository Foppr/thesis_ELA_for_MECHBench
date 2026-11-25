import numpy as np

class SinusoidalPolynomialBarrierLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Fractal sinusoidal wave parameters with self-similar frequency patterns
        self.freqs = 3.0 * np.random.rand(dim) + 1.0
        self.amps = 1.5 + 2.5 * np.random.rand(dim)
        # Quantum-inspired polynomial barrier coefficients with complex phase interactions
        self.barrier_coeffs = np.random.uniform(-3.0, 3.0, (dim, 9))
        # Adaptive coupling weights with dynamic interaction strengths
        self.coupling_weights = np.random.uniform(-1.0, 1.0, (dim, dim))
        # Stochastic resonance noise parameters with adaptive frequency modulation
        self.noise_scales = 1.0 + 3.0 * np.random.rand(dim)
        self.noise_freqs = 2.0 + 4.0 * np.random.rand(dim)
        # Fractal conditioning factors with multi-scale variance
        self.condition_factors = 0.2 + 1.5 * np.random.rand(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Fractal sinusoidal component with recursive frequency modulation
        sin_sum = 0.0
        for i in range(self.dim):
            freq_mod = np.sin(np.pi * x_norm[i]) + 0.5 * np.sin(2 * np.pi * x_norm[i])
            sin_sum += self.amps[i] * (np.sin(self.freqs[i] * x_norm[i]) + 
                                      0.4 * np.sin(3 * self.freqs[i] * x_norm[i]) + 
                                      0.1 * np.sin(5 * self.freqs[i] * x_norm[i])) * np.exp(-0.2 * x_norm[i]**2) * (1 + 0.3 * freq_mod)
        
        # Quantum-inspired polynomial barrier with complex phase terms
        poly_sum = 0.0
        for i in range(self.dim):
            coeffs = self.barrier_coeffs[i]
            # Add quantum phase factor to polynomial
            phase_factor = np.cos(0.5 * x_norm[i]) + 0.3 * np.sin(2 * x_norm[i])
            poly_val = (coeffs[0] + coeffs[1] * x_norm[i] + coeffs[2] * x_norm[i]**2 + 
                       coeffs[3] * x_norm[i]**3 + coeffs[4] * x_norm[i]**4 + coeffs[5] * x_norm[i]**5 +
                       coeffs[6] * x_norm[i]**6 + coeffs[7] * x_norm[i]**7 + coeffs[8] * x_norm[i]**8)
            poly_sum += poly_val * np.exp(-0.25 * x_norm[i]**2) * phase_factor
        
        # Adaptive coupling with quantum-like interaction terms
        coupling_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling = self.coupling_weights[i, j] * (np.sin(x_norm[i] * x_norm[j]) * 
                                                              np.cos(x_norm[i] + x_norm[j]) + 
                                                              0.3 * np.sin(2 * x_norm[i]) * np.cos(2 * x_norm[j]))
                    coupling_sum += coupling * np.exp(-0.2 * (x_norm[i]**2 + x_norm[j]**2))
        
        # Stochastic resonance noise with adaptive frequency components
        noise_sum = 0.0
        for i in range(self.dim):
            noise_sum += self.noise_scales[i] * (np.sin(self.noise_freqs[i] * x_norm[i]) * 
                                                np.cos(self.noise_freqs[i] * x_norm[i]) * 
                                                np.sin(3 * x_norm[i]) + 
                                                0.4 * np.sin(2 * self.noise_freqs[i] * x_norm[i]) * 
                                                np.cos(2 * self.noise_freqs[i] * x_norm[i]))
        
        # Combined landscape with quantum-enhanced non-linearity
        result = 0.3 * sin_sum + 0.4 * poly_sum + 0.15 * coupling_sum + 0.15 * noise_sum
        
        # Fractal dynamic conditioning with multi-scale scaling factors
        condition_factor = 1.0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.5 * np.abs(np.sin(3 * x_norm[i])) + 0.2 * np.abs(np.cos(2 * x_norm[i]))
            mag_factor = 1.0 + 0.4 * np.abs(x_norm[i]) + 0.1 * np.abs(x_norm[i]**3)
            cond_val = scale_factor * mag_factor * self.condition_factors[i]
            condition_factor *= cond_val
        
        # Fractal global penalty with multi-scale terms
        penalty = 0.15 * np.sum(np.abs(x_norm)**7) + 0.05 * np.sum(np.abs(x_norm)**9)
        return result * condition_factor + penalty + 0.02 * np.sum(x_norm**10)