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
        # Global rotation matrix with complex transformation
        angle = np.pi * np.random.rand()
        self.rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
        
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
        
        # Combine all components with adjusted weights
        result = 0.35 * sine_sum + 0.25 * poly_sum + 0.15 * cond_sum + 0.15 * minima_sum + 0.10 * coupling_sum
        
        # Add rotation and conditioning effects
        if self.dim >= 2:
            rotated = np.dot(self.rotation_matrix, x_norm[:2])
            result += 0.10 * (rotated[0]**5 + rotated[1]**5)
        
        # Mutated penalty term with better scaling and reduced bias
        penalty = 0.20 * np.sum(np.abs(x_norm)**7) + 0.10 * np.sum(np.sin(9.0 * x_norm))
        
        return result + penalty