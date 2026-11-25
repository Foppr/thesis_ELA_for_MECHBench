import numpy as np

class ChaoticRadialPolynomialLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic sine wave components with varying frequencies and amplitudes
        self.sin_frequencies = 5.0 + 15.0 * np.random.rand(dim)
        self.sin_amplitudes = 1.0 + 3.0 * np.random.rand(dim)
        # Radial polynomial terms with high-order exponents and variable coefficients
        self.poly_exponents = 3.0 + 8.0 * np.random.rand(dim)
        self.poly_coefficients = 0.5 + 4.0 * np.random.rand(dim)
        # Adaptive conditioning parameters with dynamic scaling factors
        self.conditioning_factors = 2.0 + 8.0 * np.random.rand(dim)
        # Enhanced local minima structure with multiple nested peaks
        self.minima_centers = 4.0 * np.random.rand(dim, 20) - 2.0
        self.minima_heights = 1.0 + 5.0 * np.random.rand(20)
        self.minima_widths = 0.1 + 1.5 * np.random.rand(20)
        # Cross-dimensional coupling with non-linear interaction terms
        self.coupling_strengths = 1.5 + 6.0 * np.random.rand(dim, dim)
        self.coupling_exponents = 1.0 + 4.0 * np.random.rand(dim, dim)
        # Global rotation matrix with complex transformation
        angle = np.pi * np.random.rand()
        cos_angle, sin_angle = np.cos(angle), np.sin(angle)
        self.rotation_matrix = np.array([[cos_angle, -sin_angle], [sin_angle, cos_angle]])
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic sine wave component with multiple frequencies and amplitudes
        sin_sum = 0.0
        for i in range(self.dim):
            sin_sum += self.sin_amplitudes[i] * np.sin(self.sin_frequencies[i] * x_norm[i])
        
        # Radial polynomial component with high-order terms and variable coefficients
        poly_sum = 0.0
        for i in range(self.dim):
            poly_sum += self.poly_coefficients[i] * np.power(np.abs(x_norm[i]), self.poly_exponents[i])
        
        # Adaptive conditioning with dynamic scaling
        cond_sum = 0.0
        for i in range(self.dim):
            cond_sum += self.conditioning_factors[i] * x_norm[i]**2
        
        # Enhanced local minima structure with multiple nested peaks
        minima_sum = 0.0
        for k in range(20):
            dist = 0.0
            for i in range(self.dim):
                dist += (x_norm[i] - self.minima_centers[i, k])**2
            minima_sum += self.minima_heights[k] * np.exp(-dist / (2.0 * self.minima_widths[k]**2))
        
        # Cross-dimensional coupling with non-linear interaction terms
        coupling_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_sum += self.coupling_strengths[i, j] * np.power(np.abs(x_norm[i] - x_norm[j]), self.coupling_exponents[i, j])
        
        # Combine all components with optimized weights
        result = 0.20 * sin_sum + 0.25 * poly_sum + 0.20 * cond_sum + 0.20 * minima_sum + 0.15 * coupling_sum
        
        # Add rotation and conditioning effects with more complex transformation
        if self.dim >= 2:
            rotated = np.dot(self.rotation_matrix, x_norm[:2])
            result += 0.10 * (rotated[0]**4 + rotated[1]**4)
        
        # Improved penalty term with higher-order polynomial and adaptive scaling
        penalty = 0.15 * np.sum(np.abs(x_norm)**6)
        
        return result + penalty