import numpy as np

class ChaoticRadialPolynomialLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic sine wave components with higher frequency variations
        self.sine_amplitudes = 3.0 + 7.0 * np.random.rand(dim)
        self.sine_frequencies = 15.0 + 20.0 * np.random.rand(dim)
        self.sine_phases = 2.0 * np.pi * np.random.rand(dim)
        # Modified radial polynomial components with mixed orders
        self.poly_orders = 3.0 + 6.0 * np.random.rand(dim)
        self.poly_coefficients = 0.3 + 2.5 * np.random.rand(dim)
        # Improved adaptive conditioning with logarithmic scaling
        self.conditioning_factors = 1.5 + 6.0 * np.random.rand(dim)
        self.conditioning_exponents = 0.8 + 3.5 * np.random.rand(dim)
        # Refined local minima structure with varying depths and radii
        self.minima_centers = 4.5 * np.random.rand(dim, 20) - 2.5
        self.minima_depths = 1.2 + 3.8 * np.random.rand(20)
        self.minima_radii = 0.1 + 0.8 * np.random.rand(20)
        # Enhanced coupling interactions with asymmetric terms
        self.coupling_strengths = 1.5 + 5.0 * np.random.rand(dim, dim)
        self.coupling_exponents = 0.4 + 2.5 * np.random.rand(dim, dim)
        # Fractal-like self-similarity components
        self.fractal_amplitudes = 2.0 + 4.0 * np.random.rand(dim)
        self.fractal_frequencies = 8.0 + 12.0 * np.random.rand(dim)
        # Cross-dimensional interaction terms with higher-order coupling
        self.cross_coupling_strengths = 1.0 + 3.0 * np.random.rand(dim, dim)
        self.cross_coupling_orders = 2.0 + 4.0 * np.random.rand(dim, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced chaotic sine wave component
        sine_sum = 0.0
        for i in range(self.dim):
            sine_sum += self.sine_amplitudes[i] * np.sin(self.sine_frequencies[i] * x_norm[i] + self.sine_phases[i])
        
        # Modified radial polynomial component
        poly_sum = 0.0
        for i in range(self.dim):
            poly_sum += self.poly_coefficients[i] * np.power(np.abs(x_norm[i]), self.poly_orders[i])
        
        # Improved adaptive conditioning component
        cond_sum = 0.0
        for i in range(self.dim):
            cond_sum += self.conditioning_factors[i] * np.log(1.0 + np.abs(x_norm[i]) ** self.conditioning_exponents[i])
        
        # Refined local minima structure
        minima_sum = 0.0
        for k in range(20):
            dist = 0.0
            for i in range(self.dim):
                dist += (x_norm[i] - self.minima_centers[i, k])**2
            minima_sum += self.minima_depths[k] * np.exp(-dist / (2.0 * self.minima_radii[k]**2))
        
        # Enhanced coupling interactions with asymmetric terms
        coupling_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_sum += self.coupling_strengths[i, j] * np.power(np.abs(x_norm[i] - x_norm[j]), self.coupling_exponents[i, j])
        
        # Fractal-like self-similarity component
        fractal_sum = 0.0
        for i in range(self.dim):
            fractal_sum += self.fractal_amplitudes[i] * np.sin(self.fractal_frequencies[i] * x_norm[i]) * (1.0 + 0.3 * np.sin(5.0 * x_norm[i]))
        
        # Cross-dimensional interaction terms
        cross_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    cross_sum += self.cross_coupling_strengths[i, j] * np.power(x_norm[i], self.cross_coupling_orders[i, j]) * x_norm[j]
        
        # Combine all components with adjusted weights
        result = 0.25 * sine_sum + 0.20 * poly_sum + 0.15 * cond_sum + 0.15 * minima_sum + 0.10 * coupling_sum + 0.10 * fractal_sum + 0.05 * cross_sum
        
        # Mutated penalty term with better scaling and reduced bias - improved version
        penalty = 0.25 * np.sum(np.abs(x_norm)**8) + 0.15 * np.sum(np.sin(10.0 * x_norm)) + 0.10 * np.sum(x_norm**6) + 0.05 * np.sum(np.cos(7.0 * x_norm))
        
        return result + penalty