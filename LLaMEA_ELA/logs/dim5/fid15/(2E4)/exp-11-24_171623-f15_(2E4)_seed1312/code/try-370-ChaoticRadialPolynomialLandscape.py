import numpy as np

class ChaoticRadialPolynomialLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic sine wave parameters with higher frequency variations
        self.chaotic_freqs = 2.0 + 18.0 * np.random.rand(dim)
        self.chaotic_amps = 0.5 + 3.0 * np.random.rand(dim)
        # Modified radial polynomial components with logarithmic exponents
        self.poly_exponents = 0.5 + 9.0 * np.random.rand(dim)
        # Enhanced adaptive conditioning factors
        self.conditioning_factors = 0.5 + 5.0 * np.random.rand(dim)
        # Increased cross-dimensional coupling coefficients with asymmetric interactions
        self.coupling_coeffs = 0.5 + 4.0 * np.random.rand(dim, dim)
        # Modified radial barrier parameters with multiple peaks
        self.barrier_centers = -2.5 + 5.0 * np.random.rand(dim)
        self.barrier_widths = 0.2 + 3.0 * np.random.rand(dim)
        # Expanded local minima positions for higher multimodality
        self.minima_positions = 5.0 * np.random.rand(dim, 15) - 2.5
        # Enhanced noise modulation with phase shifts
        self.noise_amplitudes = 0.1 + 1.5 * np.random.rand(dim)
        self.noise_frequencies = 1.0 + 8.0 * np.random.rand(dim)
        self.noise_phases = 2.0 * np.pi * np.random.rand(dim)
        # Additional quartic and quintic polynomial components for increased complexity
        self.quartic_coeffs = 0.05 + 1.0 * np.random.rand(dim)
        self.quintic_coeffs = 0.02 + 0.8 * np.random.rand(dim)
        # New interaction terms between dimensions
        self.interaction_coeffs = 0.2 + 2.5 * np.random.rand(dim, dim, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced chaotic sine wave component with amplitude modulation
        chaotic_sum = 0.0
        for i in range(self.dim):
            chaotic_sum += self.chaotic_amps[i] * np.sin(self.chaotic_freqs[i] * x_norm[i]) * (1.0 + 0.3 * np.cos(2.0 * x_norm[i]))
        
        # Modified radial polynomial component with logarithmic scaling
        radial_sum = 0.0
        for i in range(self.dim):
            radial_sum += np.log(1.0 + np.abs(x_norm[i])) * self.poly_exponents[i] * (1.0 + 0.4 * np.sin(3.0 * x_norm[i]))
        
        # Enhanced cross-dimensional coupling with asymmetric interaction
        coupling_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_sum += self.coupling_coeffs[i, j] * np.cos(x_norm[i]) * np.sin(x_norm[j]) * (1.0 + 0.2 * np.sin(2.0 * x_norm[i]))
        
        # Modified radial barrier component with multi-peak Gaussian kernels
        barrier_sum = 0.0
        for i in range(self.dim):
            dist = np.abs(x_norm[i] - self.barrier_centers[i])
            barrier_sum += np.exp(-0.5 * (dist / (self.barrier_widths[i] * 0.3))**2) * (1.0 + 0.5 * np.sin(4.0 * x_norm[i]))
        
        # Enhanced local minima attraction with weighted distance metrics
        minima_sum = 0.0
        for i in range(self.dim):
            min_dist = np.min(np.abs(x_norm[i] - self.minima_positions[i, :]))
            if min_dist > 0:
                minima_sum += 1.0 / (min_dist**1.5)
            else:
                minima_sum += 15.0
        
        # Enhanced noise modulation with phase shifts and frequency mixing
        noise_sum = 0.0
        for i in range(self.dim):
            noise_sum += self.noise_amplitudes[i] * np.cos(self.noise_frequencies[i] * x_norm[i] + self.noise_phases[i]) * (1.0 + 0.25 * np.sin(3.0 * x_norm[i]))
        
        # Additional quartic and quintic terms with modified weights
        quartic_sum = 0.0
        quintic_sum = 0.0
        for i in range(self.dim):
            quartic_sum += self.quartic_coeffs[i] * x_norm[i]**4 * (1.0 + 0.2 * np.cos(4.0 * x_norm[i]))
            quintic_sum += self.quintic_coeffs[i] * x_norm[i]**5 * (1.0 + 0.15 * np.sin(5.0 * x_norm[i]))
        
        # New interaction terms between dimensions
        interaction_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                for k in range(self.dim):
                    if i != j and j != k:
                        interaction_sum += self.interaction_coeffs[i, j, k] * np.sin(x_norm[i]) * np.cos(x_norm[j]) * np.tan(x_norm[k])
        
        # Combine components with adaptive weights
        result = 0.25 * chaotic_sum + 0.2 * radial_sum + 0.18 * coupling_sum + 0.12 * barrier_sum + 0.09 * minima_sum + 0.07 * noise_sum + 0.06 * quartic_sum + 0.04 * quintic_sum + 0.03 * interaction_sum
        
        # Apply enhanced adaptive conditioning with modified exponent
        condition_factor = 1.0
        for i in range(self.dim):
            condition_factor *= (1.0 + self.conditioning_factors[i] * np.abs(x_norm[i])**5)
        
        # Add global penalty term with stronger influence and additional cubic component
        penalty = 0.3 * np.sum(np.abs(x_norm)**6) + 0.1 * np.sum(x_norm**3)
        
        return result * condition_factor + penalty