import numpy as np

class ChaoticRadialPolynomialLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic sine wave parameters with higher frequencies and amplitudes
        self.chaotic_freqs = 5.0 + 15.0 * np.random.rand(dim)
        self.chaotic_amps = 1.0 + 4.0 * np.random.rand(dim)
        # Stronger radial polynomial components with varying exponents
        self.poly_exponents = 3.0 + 8.0 * np.random.rand(dim)
        # Enhanced adaptive conditioning factors
        self.conditioning_factors = 0.5 + 5.0 * np.random.rand(dim)
        # Increased cross-dimensional coupling coefficients
        self.coupling_coeffs = 1.0 + 4.0 * np.random.rand(dim, dim)
        # Extended radial barrier parameters
        self.barrier_centers = -3.0 + 6.0 * np.random.rand(dim)
        self.barrier_widths = 0.2 + 1.5 * np.random.rand(dim)
        # Additional local minima positions for enhanced multimodality
        self.minima_positions = 6.0 * np.random.rand(dim, 15) - 3.0
        # Enhanced noise modulation parameters
        self.noise_amplitudes = 0.2 + 1.8 * np.random.rand(dim)
        self.noise_frequencies = 2.0 + 8.0 * np.random.rand(dim)
        # Global structure parameters
        self.global_structure_coeffs = 0.5 + 3.0 * np.random.rand(dim)
        self.global_structure_exponents = 1.5 + 4.0 * np.random.rand(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced chaotic sine wave component
        chaotic_sum = 0.0
        for i in range(self.dim):
            chaotic_sum += self.chaotic_amps[i] * np.sin(self.chaotic_freqs[i] * x_norm[i]) * np.cos(self.chaotic_freqs[i] * x_norm[i])
        
        # Stronger radial polynomial component
        radial_sum = 0.0
        for i in range(self.dim):
            radial_sum += np.power(np.abs(x_norm[i]), self.poly_exponents[i])
        
        # Enhanced cross-dimensional coupling
        coupling_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_sum += self.coupling_coeffs[i, j] * np.sin(x_norm[i]) * np.sin(x_norm[j]) * np.cos(x_norm[i] - x_norm[j])
        
        # Extended radial barrier component
        barrier_sum = 0.0
        for i in range(self.dim):
            dist = np.abs(x_norm[i] - self.barrier_centers[i])
            barrier_sum += np.exp(-0.5 * (dist / self.barrier_widths[i])**3)
        
        # Enhanced local minima attraction
        minima_sum = 0.0
        for i in range(self.dim):
            min_dist = np.min(np.abs(x_norm[i] - self.minima_positions[i, :]))
            minima_sum += min_dist**2
        
        # Enhanced noise modulation
        noise_sum = 0.0
        for i in range(self.dim):
            noise_sum += self.noise_amplitudes[i] * np.sin(self.noise_frequencies[i] * x_norm[i]) * np.cos(self.noise_frequencies[i] * x_norm[i])
        
        # Global structure component
        global_sum = 0.0
        for i in range(self.dim):
            global_sum += self.global_structure_coeffs[i] * np.sin(self.global_structure_exponents[i] * x_norm[i])**2
        
        # Combine components with enhanced weights
        result = 0.25 * chaotic_sum + 0.3 * radial_sum + 0.15 * coupling_sum + 0.1 * barrier_sum + 0.08 * minima_sum + 0.07 * noise_sum + 0.05 * global_sum
        
        # Enhanced adaptive conditioning
        condition_factor = 1.0
        for i in range(self.dim):
            condition_factor *= (1.0 + self.conditioning_factors[i] * np.abs(x_norm[i])**4)
        
        # Additional global penalty term
        penalty = 0.2 * np.sum(np.abs(x_norm)**5)
        
        return result * condition_factor + penalty