import numpy as np

class ChaoticRadialPolynomialLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic sine wave parameters with varying frequencies and amplitudes
        self.chaotic_freqs = 1.0 + 9.0 * np.random.rand(dim)
        self.chaotic_amps = 0.3 + 2.5 * np.random.rand(dim)
        # Radial polynomial components with varying exponents
        self.poly_exponents = 1.5 + 7.0 * np.random.rand(dim)
        # Adaptive conditioning factors
        self.conditioning_factors = 0.2 + 4.0 * np.random.rand(dim)
        # Cross-dimensional coupling coefficients
        self.coupling_coeffs = 0.3 + 3.0 * np.random.rand(dim, dim)
        # Radial barrier parameters
        self.barrier_centers = -2.5 + 5.0 * np.random.rand(dim)
        self.barrier_widths = 0.3 + 2.5 * np.random.rand(dim)
        # Local minima positions for enhanced multimodality
        self.minima_positions = 4.5 * np.random.rand(dim, 12) - 2.5
        # Noise modulation parameters
        self.noise_amplitudes = 0.05 + 1.0 * np.random.rand(dim)
        self.noise_frequencies = 0.5 + 6.0 * np.random.rand(dim)
        # Additional quadratic and cubic components for increased complexity
        self.quad_coeffs = 0.1 + 1.5 * np.random.rand(dim)
        self.cubic_coeffs = 0.05 + 1.2 * np.random.rand(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic sine wave component with modified amplitude scaling
        chaotic_sum = 0.0
        for i in range(self.dim):
            chaotic_sum += self.chaotic_amps[i] * np.sin(self.chaotic_freqs[i] * x_norm[i])
        
        # Radial polynomial component with exponential weighting
        radial_sum = 0.0
        for i in range(self.dim):
            radial_sum += np.power(np.abs(x_norm[i]), self.poly_exponents[i]) * (1.0 + 0.5 * np.sin(2.0 * x_norm[i]))
        
        # Cross-dimensional coupling with cosine interaction
        coupling_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_sum += self.coupling_coeffs[i, j] * np.cos(x_norm[i]) * np.sin(x_norm[j])
        
        # Radial barrier component with Gaussian kernel and modified width
        barrier_sum = 0.0
        for i in range(self.dim):
            dist = np.abs(x_norm[i] - self.barrier_centers[i])
            barrier_sum += np.exp(-0.5 * (dist / (self.barrier_widths[i] * 0.5))**2)
        
        # Local minima attraction with inverse distance weighting
        minima_sum = 0.0
        for i in range(self.dim):
            min_dist = np.min(np.abs(x_norm[i] - self.minima_positions[i, :]))
            if min_dist > 0:
                minima_sum += 1.0 / min_dist
            else:
                minima_sum += 10.0
        
        # Noise modulation with frequency scaling
        noise_sum = 0.0
        for i in range(self.dim):
            noise_sum += self.noise_amplitudes[i] * np.cos(self.noise_frequencies[i] * x_norm[i])
        
        # Additional quadratic and cubic terms with modified weights
        quad_sum = 0.0
        cubic_sum = 0.0
        for i in range(self.dim):
            quad_sum += self.quad_coeffs[i] * x_norm[i]**2 * (1.0 + 0.3 * np.cos(3.0 * x_norm[i]))
            cubic_sum += self.cubic_coeffs[i] * x_norm[i]**3 * (1.0 + 0.2 * np.sin(4.0 * x_norm[i]))
        
        # Combine components with adaptive weights
        result = 0.3 * chaotic_sum + 0.25 * radial_sum + 0.15 * coupling_sum + 0.1 * barrier_sum + 0.08 * minima_sum + 0.07 * noise_sum + 0.06 * quad_sum + 0.04 * cubic_sum
        
        # Apply adaptive conditioning with modified exponent
        condition_factor = 1.0
        for i in range(self.dim):
            condition_factor *= (1.0 + self.conditioning_factors[i] * np.abs(x_norm[i])**4)
        
        # Add global penalty term with stronger influence
        penalty = 0.2 * np.sum(np.abs(x_norm)**5)
        
        return result * condition_factor + penalty