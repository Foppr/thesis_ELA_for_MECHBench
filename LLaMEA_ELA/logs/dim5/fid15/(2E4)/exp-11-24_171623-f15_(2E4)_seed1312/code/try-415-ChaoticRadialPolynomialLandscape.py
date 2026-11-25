import numpy as np

class ChaoticRadialPolynomialLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic sine wave components with higher frequency variations and dynamic phases
        self.sine_amplitudes = 3.0 + 7.0 * np.random.rand(dim)
        self.sine_frequencies = 15.0 + 25.0 * np.random.rand(dim)
        self.sine_phases = 2.0 * np.pi * np.random.rand(dim)
        # Modified radial polynomial components with mixed orders and dynamic coefficients
        self.poly_orders = 2.0 + 8.0 * np.random.rand(dim)
        self.poly_coefficients = 0.5 + 3.0 * np.random.rand(dim)
        # Improved adaptive conditioning with logarithmic scaling and dynamic exponents
        self.conditioning_factors = 2.0 + 7.0 * np.random.rand(dim)
        self.conditioning_exponents = 1.0 + 4.0 * np.random.rand(dim)
        # Refined local minima structure with varying depths, radii, and dynamic centers
        self.minima_centers = 5.0 * np.random.rand(dim, 20) - 2.5
        self.minima_depths = 1.0 + 4.0 * np.random.rand(20)
        self.minima_radii = 0.05 + 1.0 * np.random.rand(20)
        # Enhanced coupling interactions with asymmetric terms and dynamic strengths
        self.coupling_strengths = 2.0 + 6.0 * np.random.rand(dim, dim)
        self.coupling_exponents = 0.5 + 3.5 * np.random.rand(dim, dim)  # Mutated coupling exponents
        # Dynamic rotation matrix with multiple transformation layers
        angles = np.pi * np.random.rand(3)
        self.rotation_matrix_1 = np.array([[np.cos(angles[0]), -np.sin(angles[0])], [np.sin(angles[0]), np.cos(angles[0])]])
        self.rotation_matrix_2 = np.array([[np.cos(angles[1]), -np.sin(angles[1])], [np.sin(angles[1]), np.cos(angles[1])]])
        # Dynamic scaling factors for coupling terms
        self.scaling_factors = 1.0 + 3.0 * np.random.rand(dim)
        # Fractal noise component for increased complexity
        self.fractal_amplitudes = 0.5 + 2.0 * np.random.rand(dim)
        self.fractal_frequencies = 1.0 + 5.0 * np.random.rand(dim)
        # Hypercomplex coupling terms with higher-order interactions
        self.hypercoupling_strengths = 1.0 + 4.0 * np.random.rand(dim, dim, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced chaotic sine wave component with dynamic phase shifts
        sine_sum = 0.0
        for i in range(self.dim):
            sine_sum += self.sine_amplitudes[i] * np.sin(self.sine_frequencies[i] * x_norm[i] + self.sine_phases[i])
        
        # Modified radial polynomial component with dynamic coefficients and orders
        poly_sum = 0.0
        for i in range(self.dim):
            poly_sum += self.poly_coefficients[i] * np.power(np.abs(x_norm[i]), self.poly_orders[i])
        
        # Improved adaptive conditioning component with dynamic exponents
        cond_sum = 0.0
        for i in range(self.dim):
            cond_sum += self.conditioning_factors[i] * np.log(1.0 + np.abs(x_norm[i]) ** self.conditioning_exponents[i])
        
        # Refined local minima structure with dynamic centers and radii
        minima_sum = 0.0
        for k in range(20):
            dist = 0.0
            for i in range(self.dim):
                dist += (x_norm[i] - self.minima_centers[i, k])**2
            minima_sum += self.minima_depths[k] * np.exp(-dist / (2.0 * self.minima_radii[k]**2))
        
        # Enhanced coupling interactions with dynamic strengths and asymmetric terms
        coupling_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_sum += self.coupling_strengths[i, j] * np.power(np.abs(x_norm[i] - x_norm[j]), self.coupling_exponents[i, j]) * self.scaling_factors[i]
        
        # Hypercomplex coupling terms with third-order interactions
        hypercoupling_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                for k in range(self.dim):
                    if i != j and j != k:
                        hypercoupling_sum += self.hypercoupling_strengths[i, j, k] * np.power(np.abs(x_norm[i] - x_norm[j]), 2.0) * np.power(np.abs(x_norm[j] - x_norm[k]), 2.0)
        
        # Combine all components with adjusted weights
        result = 0.15 * sine_sum + 0.15 * poly_sum + 0.10 * cond_sum + 0.25 * minima_sum + 0.15 * coupling_sum + 0.20 * hypercoupling_sum
        
        # Add multi-layer rotation and conditioning effects
        if self.dim >= 2:
            rotated_1 = np.dot(self.rotation_matrix_1, x_norm[:2])
            rotated_2 = np.dot(self.rotation_matrix_2, x_norm[:2])
            result += 0.10 * (rotated_1[0]**4 + rotated_1[1]**4 + rotated_2[0]**3 + rotated_2[1]**3)
        
        # Fractal noise component
        fractal_sum = 0.0
        for i in range(self.dim):
            fractal_sum += self.fractal_amplitudes[i] * np.sin(self.fractal_frequencies[i] * x_norm[i]) * np.cos(self.fractal_frequencies[i] * x_norm[i])
        
        # Mutated penalty term with altered scaling and enhanced bias reduction
        penalty = 0.30 * np.sum(np.abs(x_norm)**7) + 0.10 * np.sum(np.sin(10.0 * x_norm)) + 0.05 * fractal_sum
        
        return result + penalty