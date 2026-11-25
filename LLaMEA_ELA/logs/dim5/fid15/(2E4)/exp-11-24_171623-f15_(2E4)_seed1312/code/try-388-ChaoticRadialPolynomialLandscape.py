import numpy as np

class ChaoticRadialPolynomialLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic sine wave components with higher frequency modulation and amplitude variation
        self.sine_amplitudes = 5.0 + 10.0 * np.random.rand(dim)
        self.sine_frequencies = 8.0 + 25.0 * np.random.rand(dim)
        self.sine_phases = 2.0 * np.pi * np.random.rand(dim)
        # Radial polynomial components with even higher-order terms and modified coefficients
        self.poly_orders = 6.0 + 12.0 * np.random.rand(dim)
        self.poly_coefficients = 1.0 + 5.0 * np.random.rand(dim)
        # Improved adaptive conditioning with exponential scaling and additional nonlinear terms
        self.conditioning_factors = 3.0 + 10.0 * np.random.rand(dim)
        self.conditioning_exponents = 2.0 + 6.0 * np.random.rand(dim)
        # Refined local minima structure with multiple nested basins and increased depth variability
        self.minima_centers = 6.0 * np.random.rand(dim, 30) - 3.0
        self.minima_depths = 2.0 + 6.0 * np.random.rand(30)
        self.minima_radii = 0.1 + 1.5 * np.random.rand(30)
        # Modified coupling interactions with non-linear terms and increased complexity
        self.coupling_strengths = 3.0 + 8.0 * np.random.rand(dim, dim)
        self.coupling_exponents = 2.0 + 4.0 * np.random.rand(dim, dim)
        # Global rotation matrix with complex transformation and additional rotational components
        angle = np.pi * np.random.rand()
        self.rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced chaotic sine wave component with additional harmonic terms
        sine_sum = 0.0
        for i in range(self.dim):
            sine_sum += self.sine_amplitudes[i] * np.sin(self.sine_frequencies[i] * x_norm[i] + self.sine_phases[i])
            sine_sum += 0.5 * self.sine_amplitudes[i] * np.sin(2.0 * self.sine_frequencies[i] * x_norm[i] + self.sine_phases[i])
        
        # Radial polynomial component with higher-order terms and modified coefficients
        poly_sum = 0.0
        for i in range(self.dim):
            poly_sum += self.poly_coefficients[i] * np.power(np.abs(x_norm[i]), self.poly_orders[i])
        
        # Improved adaptive conditioning component with additional nonlinear scaling
        cond_sum = 0.0
        for i in range(self.dim):
            cond_sum += self.conditioning_factors[i] * np.power(np.abs(x_norm[i]), self.conditioning_exponents[i])
            cond_sum += 0.3 * self.conditioning_factors[i] * np.sin(5.0 * x_norm[i])
        
        # Refined local minima structure with multiple nested basins and increased depth variability
        minima_sum = 0.0
        for k in range(30):
            dist = 0.0
            for i in range(self.dim):
                dist += (x_norm[i] - self.minima_centers[i, k])**2
            minima_sum += self.minima_depths[k] * np.exp(-dist / (2.0 * self.minima_radii[k]**2))
        
        # Modified coupling interactions with non-linear terms and increased complexity
        coupling_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_sum += self.coupling_strengths[i, j] * np.power(np.abs(x_norm[i] - x_norm[j]), self.coupling_exponents[i, j])
                    coupling_sum += 0.2 * self.coupling_strengths[i, j] * np.sin(3.0 * (x_norm[i] - x_norm[j]))
        
        # Combine all components with varying weights
        result = 0.20 * sine_sum + 0.18 * poly_sum + 0.17 * cond_sum + 0.23 * minima_sum + 0.22 * coupling_sum
        
        # Add rotation and conditioning effects with additional nonlinear terms
        if self.dim >= 2:
            rotated = np.dot(self.rotation_matrix, x_norm[:2])
            result += 0.12 * (rotated[0]**4 + rotated[1]**4)
            result += 0.08 * np.sin(7.0 * rotated[0]) * np.cos(7.0 * rotated[1])
        
        # Global penalty term with higher degree and chaotic scaling
        penalty = 0.30 * np.sum(np.abs(x_norm)**7) + 0.20 * np.sum(np.sin(15.0 * x_norm))
        penalty += 0.15 * np.sum(np.cos(8.0 * x_norm))
        
        return result + penalty