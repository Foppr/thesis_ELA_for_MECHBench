import numpy as np

class ChaoticRadialPolynomialLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic sine wave components with varying frequencies and amplitudes
        self.sine_amplitudes = 3.0 + 7.0 * np.random.rand(dim)
        self.sine_frequencies = 5.0 + 15.0 * np.random.rand(dim)
        self.sine_phases = 2.0 * np.pi * np.random.rand(dim)
        # Radial polynomial components with high-order terms
        self.poly_orders = 4.0 + 8.0 * np.random.rand(dim)
        self.poly_coefficients = 0.5 + 3.0 * np.random.rand(dim)
        # Adaptive conditioning parameters with exponential scaling
        self.conditioning_factors = 2.0 + 8.0 * np.random.rand(dim)
        self.conditioning_exponents = 1.5 + 4.0 * np.random.rand(dim)
        # Enhanced local minima structure with multiple nested basins
        self.minima_centers = 4.0 * np.random.rand(dim, 20) - 2.0
        self.minima_depths = 1.0 + 4.0 * np.random.rand(20)
        self.minima_radii = 0.2 + 1.0 * np.random.rand(20)
        # Modified coupling interactions with non-linear terms
        self.coupling_strengths = 2.0 + 6.0 * np.random.rand(dim, dim)
        self.coupling_exponents = 1.0 + 3.0 * np.random.rand(dim, dim)
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
        for k in range(20):
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
        result = 0.25 * sine_sum + 0.20 * poly_sum + 0.15 * cond_sum + 0.25 * minima_sum + 0.15 * coupling_sum
        
        # Add rotation and conditioning effects
        if self.dim >= 2:
            rotated = np.dot(self.rotation_matrix, x_norm[:2])
            result += 0.10 * (rotated[0]**3 + rotated[1]**3)
        
        # Global penalty term with higher degree and chaotic scaling
        penalty = 0.30 * np.sum(np.abs(x_norm)**7) + 0.20 * np.sum(np.sin(15.0 * x_norm))
        
        return result + penalty