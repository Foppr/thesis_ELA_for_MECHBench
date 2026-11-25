import numpy as np

class SinusoidalPolynomialBarrierLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Fractal-inspired chaotic sinusoidal parameters with power-law distribution
        self.freqs = np.power(2.0, 1.0 + 3.0 * np.random.rand(dim))
        self.amps = 3.0 + 4.0 * np.random.rand(dim)
        # Higher-order polynomial barrier coefficients (degree 7) with fractal-like patterns
        self.barrier_coeffs = np.random.uniform(-3, 3, (dim, 8))
        # Cross-dimensional coupling with fractal interaction weights
        self.coupling_weights = np.random.uniform(-1.0, 1.0, (dim, dim))
        # Multi-scale dynamic noise with fractal characteristics
        self.noise_scales = 2.0 + 3.0 * np.random.rand(dim)
        self.noise_freqs = 1.0 + 2.0 * np.random.rand(dim)
        # Fractal conditioning factors with self-similar patterns
        self.condition_factors = 1.5 + 1.0 * np.random.rand(dim)
        # Fractal dimensionality scaling factor
        self.fractal_dim = 0.5 + 0.5 * np.random.rand()
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Fractal sinusoidal component with power-law decay
        sin_sum = 0.0
        for i in range(self.dim):
            sin_sum += self.amps[i] * np.sin(self.freqs[i] * x_norm[i]) * np.power(1.0 + np.abs(x_norm[i]), -2.0)
        
        # High-order polynomial barrier with 7th degree terms and fractal coefficients
        poly_sum = 0.0
        for i in range(self.dim):
            coeffs = self.barrier_coeffs[i]
            poly_val = (coeffs[0] + coeffs[1] * x_norm[i] + coeffs[2] * x_norm[i]**2 + 
                       coeffs[3] * x_norm[i]**3 + coeffs[4] * x_norm[i]**4 + coeffs[5] * x_norm[i]**5 +
                       coeffs[6] * x_norm[i]**6 + coeffs[7] * x_norm[i]**7)
            poly_sum += poly_val * np.power(1.0 + np.abs(x_norm[i]), -1.5)
        
        # Fractal coupling with multi-scale interaction
        coupling_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling = self.coupling_weights[i, j] * np.sin(x_norm[i] * x_norm[j]) * (x_norm[i]**4 + x_norm[j]**4)
                    coupling_sum += coupling * np.power(1.0 + x_norm[i]**2 + x_norm[j]**2, -1.0)
        
        # Multi-scale fractal noise
        noise_sum = 0.0
        for i in range(self.dim):
            noise_sum += self.noise_scales[i] * np.sin(self.noise_freqs[i] * x_norm[i]) * np.cos(self.noise_freqs[i] * x_norm[i]) * np.exp(-0.5 * x_norm[i]**2)
        
        # Combined landscape with fractal non-linearity
        result = 0.3 * sin_sum + 0.4 * poly_sum + 0.2 * coupling_sum + 0.1 * noise_sum
        
        # Fractal conditioning with self-similar scaling
        condition_factor = 1.0
        for i in range(self.dim):
            freq_factor = 1.0 + 0.5 * np.abs(np.sin(self.freqs[i]))
            mag_factor = 1.0 + 0.4 * np.abs(x_norm[i])
            cond_val = freq_factor * mag_factor * self.condition_factors[i]
            condition_factor *= np.power(cond_val, self.fractal_dim)
        
        # Fractal global penalty with multi-scale terms
        penalty = 0.3 * np.sum(np.abs(x_norm)**8)
        return result * condition_factor + penalty + 0.05 * np.sum(np.abs(x_norm)**10)