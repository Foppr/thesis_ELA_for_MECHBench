import numpy as np

class ChaoticRadialPolynomialLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic sine wave parameters with frequency modulation
        self.chaotic_freqs = 3.0 + 12.0 * np.random.rand(dim)
        self.chaotic_amps = 1.0 + 4.0 * np.random.rand(dim)
        # Radial polynomial components with exponential scaling
        self.poly_exponents = 3.0 + 8.0 * np.random.rand(dim)
        # Adaptive conditioning factors with logarithmic scaling
        self.conditioning_factors = 0.2 + 5.0 * np.random.rand(dim)
        # Cross-dimensional coupling with tensor interactions
        self.coupling_coeffs = 1.0 + 4.0 * np.random.rand(dim, dim, dim)
        # Enhanced radial barrier parameters with multiple peaks
        self.barrier_centers = -3.0 + 6.0 * np.random.rand(dim)
        self.barrier_widths = 0.2 + 3.0 * np.random.rand(dim)
        # Multiple local minima positions for increased multimodality
        self.minima_positions = 5.0 * np.random.rand(dim, 15) - 2.5
        # Noise modulation with time-varying frequencies
        self.noise_amplitudes = 0.2 + 1.5 * np.random.rand(dim)
        self.noise_frequencies = 2.0 + 8.0 * np.random.rand(dim)
        # Novel tensor-based coupling terms
        self.tensor_couplings = 0.5 + 3.0 * np.random.rand(dim, dim, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced chaotic sine wave component
        chaotic_sum = 0.0
        for i in range(self.dim):
            chaotic_sum += self.chaotic_amps[i] * np.sin(self.chaotic_freqs[i] * x_norm[i]) * np.cos(0.5 * self.chaotic_freqs[i] * x_norm[i])
        
        # Enhanced radial polynomial component
        radial_sum = 0.0
        for i in range(self.dim):
            radial_sum += np.power(np.abs(x_norm[i]), self.poly_exponents[i]) * np.log(1.0 + np.abs(x_norm[i]))
        
        # Tensor-based cross-dimensional coupling
        coupling_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                for k in range(self.dim):
                    if i != j and j != k:
                        coupling_sum += self.tensor_couplings[i, j, k] * np.sin(x_norm[i]) * np.cos(x_norm[j]) * np.tan(x_norm[k])
        
        # Enhanced radial barrier component
        barrier_sum = 0.0
        for i in range(self.dim):
            dist = np.abs(x_norm[i] - self.barrier_centers[i])
            barrier_sum += np.exp(-0.5 * (dist / self.barrier_widths[i])**3)
        
        # Multiple local minima attraction
        minima_sum = 0.0
        for i in range(self.dim):
            dists = np.abs(x_norm[i] - self.minima_positions[i, :])
            sorted_dists = np.sort(dists)
            minima_sum += sorted_dists[0] + 0.5 * sorted_dists[1] + 0.25 * sorted_dists[2]
        
        # Enhanced noise modulation
        noise_sum = 0.0
        for i in range(self.dim):
            noise_sum += self.noise_amplitudes[i] * np.sin(self.noise_frequencies[i] * x_norm[i]) * np.cos(2.0 * self.noise_frequencies[i] * x_norm[i])
        
        # Combine components with enhanced weights
        result = 0.25 * chaotic_sum + 0.3 * radial_sum + 0.15 * coupling_sum + 0.2 * barrier_sum + 0.08 * minima_sum + 0.07 * noise_sum
        
        # Enhanced adaptive conditioning with multiplicative factors
        condition_factor = 1.0
        for i in range(self.dim):
            condition_factor *= (1.0 + self.conditioning_factors[i] * np.abs(x_norm[i])**4)
        
        # Add enhanced global penalty term
        penalty = 0.2 * np.sum(np.abs(x_norm)**5)
        
        return result * condition_factor + penalty