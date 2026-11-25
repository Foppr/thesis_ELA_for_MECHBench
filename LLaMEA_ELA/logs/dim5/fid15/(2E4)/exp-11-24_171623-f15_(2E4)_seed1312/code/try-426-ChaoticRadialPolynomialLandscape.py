import numpy as np

class ChaoticRadialPolynomialLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic sine wave components with higher frequency variations and phase modulation
        self.sine_amplitudes = 4.0 + 8.0 * np.random.rand(dim)
        self.sine_frequencies = 20.0 + 30.0 * np.random.rand(dim)
        self.sine_phases = 2.0 * np.pi * np.random.rand(dim)
        # Modified radial polynomial components with mixed orders and variable exponents
        self.poly_orders = 4.0 + 8.0 * np.random.rand(dim)
        self.poly_coefficients = 0.5 + 3.0 * np.random.rand(dim)
        # Improved adaptive conditioning with logarithmic scaling and exponential factors
        self.conditioning_factors = 2.0 + 7.0 * np.random.rand(dim)
        self.conditioning_exponents = 1.0 + 4.0 * np.random.rand(dim)
        # Refined local minima structure with varying depths, radii, and density
        self.minima_centers = 4.0 * np.random.rand(dim, 30) - 2.0
        self.minima_depths = 1.5 + 4.5 * np.random.rand(30)
        self.minima_radii = 0.05 + 1.0 * np.random.rand(30)
        # Enhanced coupling interactions with asymmetric terms and dynamic scaling
        self.coupling_strengths = 2.0 + 6.0 * np.random.rand(dim, dim)
        self.coupling_exponents = 0.3 + 3.0 * np.random.rand(dim, dim)
        # Global rotation matrix with complex transformation and additional dimensionality
        angle = np.pi * np.random.rand()
        self.rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced chaotic sine wave component with phase modulation
        sine_sum = 0.0
        for i in range(self.dim):
            sine_sum += self.sine_amplitudes[i] * np.sin(self.sine_frequencies[i] * x_norm[i] + self.sine_phases[i])
        
        # Modified radial polynomial component with variable exponents and scaling
        poly_sum = 0.0
        for i in range(self.dim):
            poly_sum += self.poly_coefficients[i] * np.power(np.abs(x_norm[i]), self.poly_orders[i])
        
        # Improved adaptive conditioning component with exponential factors
        cond_sum = 0.0
        for i in range(self.dim):
            cond_sum += self.conditioning_factors[i] * np.exp(np.abs(x_norm[i]) ** self.conditioning_exponents[i])
        
        # Refined local minima structure with increased complexity and density
        minima_sum = 0.0
        for k in range(30):
            dist = 0.0
            for i in range(self.dim):
                dist += (x_norm[i] - self.minima_centers[i, k])**2
            minima_sum += self.minima_depths[k] * np.exp(-dist / (2.0 * self.minima_radii[k]**2))
        
        # Enhanced coupling interactions with asymmetric terms and dynamic scaling
        coupling_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_sum += self.coupling_strengths[i, j] * np.power(np.abs(x_norm[i] - x_norm[j]), self.coupling_exponents[i, j])
        
        # Combine all components with adjusted weights
        result = 0.30 * sine_sum + 0.20 * poly_sum + 0.15 * cond_sum + 0.15 * minima_sum + 0.20 * coupling_sum
        
        # Add rotation and conditioning effects with additional complexity
        if self.dim >= 2:
            rotated = np.dot(self.rotation_matrix, x_norm[:2])
            result += 0.15 * (rotated[0]**6 + rotated[1]**6)
        
        # Mutated penalty term with enhanced complexity and reduced bias
        penalty = 0.30 * np.sum(np.abs(x_norm)**9) + 0.20 * np.sum(np.sin(12.0 * x_norm)) + 0.15 * np.sum(x_norm**7)
        
        return result + penalty