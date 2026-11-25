import numpy as np

class ChaoticRadialPolynomialLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic sine wave components with varying frequencies and amplitudes
        self.sine_amplitudes = 5.0 + 10.0 * np.random.rand(dim)
        self.sine_frequencies = 8.0 + 20.0 * np.random.rand(dim)
        self.sine_phases = 2.0 * np.pi * np.random.rand(dim)
        # Radial polynomial components with high-order terms
        self.poly_orders = 6.0 + 12.0 * np.random.rand(dim)
        self.poly_coefficients = 1.0 + 5.0 * np.random.rand(dim)
        # Adaptive conditioning parameters with exponential scaling
        self.conditioning_factors = 3.0 + 10.0 * np.random.rand(dim)
        self.conditioning_exponents = 2.0 + 6.0 * np.random.rand(dim)
        # Enhanced local minima structure with multiple nested basins
        self.minima_centers = 5.0 * np.random.rand(dim, 30) - 2.5
        self.minima_depths = 2.0 + 6.0 * np.random.rand(30)
        self.minima_radii = 0.1 + 1.5 * np.random.rand(30)
        # Modified coupling interactions with non-linear terms
        self.coupling_strengths = 3.0 + 8.0 * np.random.rand(dim, dim)
        self.coupling_exponents = 1.5 + 4.0 * np.random.rand(dim, dim)
        # Global rotation matrix with complex transformation
        angle = np.pi * np.random.rand()
        self.rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic sine wave component
        sine_sum = 0.0
        for i in range(self.dim):
            sine_sum += self.sine_amplitudes[i] * np.sin(self.sine_frequencies[i] * x_norm[i] + self.sine_phases[i])
        
        # Radial polynomial component
        poly_sum = 0.0
        for i in range(self.dim):
            poly_sum += self.poly_coefficients[i] * np.power(np.abs(x_norm[i]), self.poly_orders[i])
        
        # Adaptive conditioning component
        cond_sum = 0.0
        for i in range(self.dim):
            cond_sum += self.conditioning_factors[i] * np.power(np.abs(x_norm[i]), self.conditioning_exponents[i])
        
        # Enhanced local minima structure
        minima_sum = 0.0
        for k in range(30):
            dist = 0.0
            for i in range(self.dim):
                dist += (x_norm[i] - self.minima_centers[i, k])**2
            minima_sum += self.minima_depths[k] * np.exp(-dist / (2.0 * self.minima_radii[k]**2))
        
        # Modified coupling interactions
        coupling_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_sum += self.coupling_strengths[i, j] * np.power(np.abs(x_norm[i] - x_norm[j]), self.coupling_exponents[i, j])
        
        # Combine all components with varying weights
        result = 0.20 * sine_sum + 0.15 * poly_sum + 0.10 * cond_sum + 0.25 * minima_sum + 0.30 * coupling_sum
        
        # Add rotation and conditioning effects
        if self.dim >= 2:
            rotated = np.dot(self.rotation_matrix, x_norm[:2])
            result += 0.15 * (rotated[0]**4 + rotated[1]**4)
        
        # Global penalty term with higher degree and chaotic scaling
        penalty = 0.25 * np.sum(np.abs(x_norm)**6) + 0.15 * np.sum(np.sin(15.0 * x_norm))
        
        return result + penalty