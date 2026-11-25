import numpy as np

class ChaoticRadialPolynomialLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic sine wave parameters with varying frequencies and amplitudes
        self.chaotic_freqs = 2.0 + 8.0 * np.random.rand(dim)
        self.chaotic_amps = 0.5 + 2.0 * np.random.rand(dim)
        # Radial polynomial components with varying exponents
        self.poly_exponents = 2.0 + 6.0 * np.random.rand(dim)
        # Adaptive conditioning factors
        self.conditioning_factors = 0.1 + 3.0 * np.random.rand(dim)
        # Cross-dimensional coupling coefficients
        self.coupling_coeffs = 0.5 + 2.5 * np.random.rand(dim, dim)
        # Radial barrier parameters
        self.barrier_centers = -2.0 + 4.0 * np.random.rand(dim)
        self.barrier_widths = 0.5 + 2.0 * np.random.rand(dim)
        # Local minima positions for enhanced multimodality
        self.minima_positions = 4.0 * np.random.rand(dim, 10) - 2.0
        # Noise modulation parameters
        self.noise_amplitudes = 0.1 + 0.9 * np.random.rand(dim)
        self.noise_frequencies = 1.0 + 5.0 * np.random.rand(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic sine wave component
        chaotic_sum = 0.0
        for i in range(self.dim):
            chaotic_sum += self.chaotic_amps[i] * np.sin(self.chaotic_freqs[i] * x_norm[i])
        
        # Radial polynomial component
        radial_sum = 0.0
        for i in range(self.dim):
            radial_sum += np.power(np.abs(x_norm[i]), self.poly_exponents[i])
        
        # Cross-dimensional coupling
        coupling_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_sum += self.coupling_coeffs[i, j] * np.sin(x_norm[i]) * np.cos(x_norm[j])
        
        # Radial barrier component
        barrier_sum = 0.0
        for i in range(self.dim):
            dist = np.abs(x_norm[i] - self.barrier_centers[i])
            barrier_sum += np.exp(-0.5 * (dist / self.barrier_widths[i])**2)
        
        # Local minima attraction
        minima_sum = 0.0
        for i in range(self.dim):
            min_dist = np.min(np.abs(x_norm[i] - self.minima_positions[i, :]))
            minima_sum += min_dist
        
        # Noise modulation
        noise_sum = 0.0
        for i in range(self.dim):
            noise_sum += self.noise_amplitudes[i] * np.sin(self.noise_frequencies[i] * x_norm[i])
        
        # Combine components with adaptive weights
        result = 0.3 * chaotic_sum + 0.25 * radial_sum + 0.2 * coupling_sum + 0.15 * barrier_sum + 0.05 * minima_sum + 0.05 * noise_sum
        
        # Apply adaptive conditioning
        condition_factor = 1.0
        for i in range(self.dim):
            condition_factor *= (1.0 + self.conditioning_factors[i] * np.abs(x_norm[i])**3)
        
        # Add global penalty term
        penalty = 0.1 * np.sum(np.abs(x_norm)**4)
        
        return result * condition_factor + penalty