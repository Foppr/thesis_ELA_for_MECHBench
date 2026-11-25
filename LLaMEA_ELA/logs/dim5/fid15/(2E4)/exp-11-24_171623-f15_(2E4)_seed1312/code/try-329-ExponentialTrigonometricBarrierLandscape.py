import numpy as np

class ExponentialTrigonometricBarrierLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic attractor parameters with nested dynamics
        self.attractor_params = 0.5 + 3.0 * np.random.rand(dim, 3)
        self.nested_coefficients = 1.0 + 4.0 * np.random.rand(dim, dim)
        # Dynamic polynomial coupling with varying degrees
        self.poly_coupling_orders = 2 + np.random.randint(4, size=(dim, dim))
        self.poly_coupling_weights = 0.5 + 3.0 * np.random.rand(dim, dim)
        # Adaptive spectral noise with multiple frequency bands
        self.noise_bands = 3 + np.random.randint(3, size=dim)
        self.noise_band_weights = 0.1 + 2.0 * np.random.rand(dim, 3)
        # Dynamic conditioning factors with time-like dependencies
        self.conditioning_time_factors = 0.5 + 2.5 * np.random.rand(dim)
        self.conditioning_amplitudes = 0.2 + 1.8 * np.random.rand(dim)
        # Enhanced barrier system with fractal-like structures
        self.fractal_barrier_rates = 1.0 + 5.0 * np.random.rand(dim)
        self.fractal_barrier_heights = 2.0 + 4.0 * np.random.rand(dim)
        self.fractal_barrier_exponents = 1.5 + 3.0 * np.random.rand(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Fractal barrier component with nested exponential structures
        fractal_barrier_sum = 0.0
        for i in range(self.dim):
            barrier_term = 0.0
            for j in range(self.dim):
                if i != j:
                    barrier_term += self.fractal_barrier_heights[i] * np.exp(-self.fractal_barrier_rates[i] * 
                                                                            np.abs(x_norm[i] - x_norm[j])**self.fractal_barrier_exponents[i])
            fractal_barrier_sum += barrier_term
        
        # Nested chaotic attractor component
        attractor_sum = 0.0
        for i in range(self.dim):
            attractor_val = 0.0
            for j in range(3):
                coeff = self.attractor_params[i, j]
                attractor_val += coeff * np.sin(coeff * x_norm[i] + j)
            attractor_sum += attractor_val**2
        
        # Dynamic polynomial coupling between dimensions
        poly_coupling_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    poly_coupling_sum += (self.poly_coupling_weights[i, j] * 
                                        x_norm[i]**self.poly_coupling_orders[i, j] * 
                                        x_norm[j]**self.poly_coupling_orders[i, j])
        
        # Spectral noise with multiple frequency bands
        spectral_noise_sum = 0.0
        for i in range(self.dim):
            noise_val = 0.0
            for band in range(self.noise_bands[i]):
                freq = (band + 1) * np.pi * (1.0 + 0.5 * np.sin(x_norm[i]))
                noise_val += self.noise_band_weights[i, band] * np.sin(freq * x_norm[i])
            spectral_noise_sum += noise_val
        
        # Combined chaotic and coupling components
        result = 0.3 * fractal_barrier_sum + 0.25 * attractor_sum + 0.25 * poly_coupling_sum + 0.2 * spectral_noise_sum
        
        # Dynamic conditioning with time-like variations
        condition_factor = 1.0
        for i in range(self.dim):
            time_factor = np.sin(self.conditioning_time_factors[i] * x_norm[i])
            condition_factor *= (1.0 + self.conditioning_amplitudes[i] * np.abs(time_factor))
        
        # Add complex penalty term with multiple components
        penalty = 0.5 * np.sum(np.abs(x_norm)**4) + 0.3 * np.sum(np.sin(2 * x_norm)**2)
        
        return result * condition_factor + penalty