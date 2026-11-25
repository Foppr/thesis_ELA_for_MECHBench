import numpy as np

class ChaoticRadialPolynomialLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic sine wave parameters with exponential modulation
        self.chaotic_freqs = 2.0 + 8.0 * np.random.rand(dim)
        self.chaotic_amps = 1.0 + 2.0 * np.random.rand(dim)
        self.chaotic_phases = 2 * np.pi * np.random.rand(dim)
        # Modified radial polynomial components with logarithmic exponents
        self.poly_exponents = 0.5 + 6.0 * np.random.rand(dim)
        # Adaptive conditioning with exponential scaling
        self.conditioning_factors = 0.1 + 3.0 * np.random.rand(dim)
        # Novel hybrid coupling coefficients with cross-dimensional interaction terms
        self.coupling_coeffs = 0.2 + 3.0 * np.random.rand(dim, dim)
        self.cross_coupling = 0.5 + 2.5 * np.random.rand(dim, dim)
        # Radial barrier parameters with Gaussian mixture components
        self.barrier_centers = -2.0 + 4.0 * np.random.rand(dim)
        self.barrier_widths = 0.2 + 2.0 * np.random.rand(dim)
        self.barrier_weights = 0.5 + 1.5 * np.random.rand(dim)
        # Enhanced local minima with multiple attraction points
        self.minima_positions = 4.0 * np.random.rand(dim, 15) - 2.0
        self.minima_strengths = 0.3 + 1.2 * np.random.rand(15)
        # Novel noise modulation with frequency-dependent components
        self.noise_amplitudes = 0.2 + 1.0 * np.random.rand(dim)
        self.noise_frequencies = 0.5 + 5.0 * np.random.rand(dim)
        self.noise_phase = 2 * np.pi * np.random.rand(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced chaotic sine wave component with phase modulation
        chaotic_sum = 0.0
        for i in range(self.dim):
            chaotic_sum += self.chaotic_amps[i] * np.sin(self.chaotic_freqs[i] * x_norm[i] + self.chaotic_phases[i])
        
        # Modified radial polynomial component with logarithmic scaling
        radial_sum = 0.0
        for i in range(self.dim):
            radial_sum += np.log(1.0 + np.power(np.abs(x_norm[i]), self.poly_exponents[i]))
        
        # Hybrid cross-dimensional coupling
        coupling_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_sum += (self.coupling_coeffs[i, j] * np.sin(x_norm[i]) * np.cos(x_norm[j]) + 
                                   self.cross_coupling[i, j] * np.cos(2 * x_norm[i]) * np.sin(2 * x_norm[j]))
        
        # Gaussian mixture radial barrier component
        barrier_sum = 0.0
        for i in range(self.dim):
            barrier_component = 0.0
            for k in range(3):  # Three Gaussian components per dimension
                center = self.barrier_centers[i] + (k - 1) * 0.5
                barrier_component += self.barrier_weights[i] * np.exp(-0.5 * ((x_norm[i] - center) / self.barrier_widths[i])**2)
            barrier_sum += barrier_component
        
        # Enhanced local minima attraction with multiple strengths
        minima_sum = 0.0
        for i in range(self.dim):
            min_distances = np.abs(x_norm[i] - self.minima_positions[i, :])
            weighted_distances = min_distances * self.minima_strengths
            minima_sum += np.min(weighted_distances)
        
        # Novel noise modulation with phase shifts
        noise_sum = 0.0
        for i in range(self.dim):
            noise_sum += self.noise_amplitudes[i] * np.sin(self.noise_frequencies[i] * x_norm[i] + self.noise_phase[i])
        
        # Combine components with updated weights
        result = 0.30 * chaotic_sum + 0.25 * radial_sum + 0.20 * coupling_sum + 0.15 * barrier_sum + 0.08 * minima_sum + 0.02 * noise_sum
        
        # Enhanced adaptive conditioning with exponential scaling
        condition_factor = 1.0
        for i in range(self.dim):
            condition_factor *= np.exp(self.conditioning_factors[i] * np.abs(x_norm[i])**3)
        
        # Add enhanced global penalty term
        penalty = 0.20 * np.sum(np.abs(x_norm)**6)
        
        return result * condition_factor + penalty