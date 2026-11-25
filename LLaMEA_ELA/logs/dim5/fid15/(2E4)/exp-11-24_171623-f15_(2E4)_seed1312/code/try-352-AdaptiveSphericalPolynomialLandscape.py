import numpy as np

class AdaptiveSphericalPolynomialLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Polynomial exponents for varying curvature
        self.poly_exponents = 2.0 + 4.0 * np.random.rand(dim)
        # Spherical component coefficients
        self.sphere_coeffs = 1.0 + 3.0 * np.random.rand(dim)
        # Exponential decay rates with sinusoidal modulation for added complexity
        self.exp_rates = 0.5 + 2.5 * np.random.rand(dim)
        # Cross-dimensional coupling strengths with sinusoidal variation
        self.coupling_strengths = 0.5 + 2.0 * np.random.rand(dim, dim)
        # Adaptive conditioning factors
        self.conditioning_factors = 0.1 + 1.9 * np.random.rand(dim)
        # Noise parameters for added complexity
        self.noise_amplitudes = 0.1 + 0.9 * np.random.rand(dim)
        self.noise_frequencies = 1.0 + 3.0 * np.random.rand(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Spherical component
        sphere_term = 0.0
        for i in range(self.dim):
            sphere_term += self.sphere_coeffs[i] * np.power(x_norm[i], 2)
        
        # Polynomial component
        poly_term = 0.0
        for i in range(self.dim):
            poly_term += np.power(np.abs(x_norm[i]), self.poly_exponents[i])
        
        # Modified exponential barrier component with sinusoidal modulation
        exp_term = 0.0
        for i in range(self.dim):
            exp_term += np.exp(-self.exp_rates[i] * np.abs(x_norm[i])) * (1.0 + 0.3 * np.sin(2.0 * np.pi * x_norm[i]))
        
        # Cross-dimensional coupling with sinusoidal variation
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_term += self.coupling_strengths[i, j] * x_norm[i] * x_norm[j] * (1.0 + 0.2 * np.cos(3.0 * np.pi * x_norm[i]))
        
        # Adaptive conditioning
        condition_factor = 1.0
        for i in range(self.dim):
            condition_factor *= (1.0 + self.conditioning_factors[i] * np.abs(x_norm[i]))
        
        # Noise component
        noise_term = 0.0
        for i in range(self.dim):
            noise_term += self.noise_amplitudes[i] * np.sin(self.noise_frequencies[i] * x_norm[i])
        
        # Combine all terms with appropriate weights
        result = 0.3 * sphere_term + 0.25 * poly_term + 0.2 * exp_term + 0.15 * coupling_term + 0.1 * noise_term
        
        # Add global penalty for large values
        penalty = 0.05 * np.sum(np.power(x_norm, 4))
        
        return result * condition_factor + penalty