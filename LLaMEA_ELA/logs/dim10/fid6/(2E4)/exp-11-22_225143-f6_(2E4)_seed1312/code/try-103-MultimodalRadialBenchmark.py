import numpy as np

class MultimodalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic sine wave parameters
        self.chaos_factors = np.random.uniform(0.8, 3.0, dim)
        self.chaos_freqs = np.random.uniform(5.0, 15.0, dim)
        # Adaptive conditioning with exponential scaling
        self.conditioning_factors = np.random.uniform(0.1, 1.5, dim)
        self.conditioning_exponents = np.random.uniform(3.0, 7.0, dim)
        # Radial basis function centers and widths with dynamic scaling
        self.rbf_centers = np.random.uniform(-4.5, 4.5, (15, dim))
        self.rbf_widths = np.random.uniform(0.3, 3.0, 15)
        # Multi-scale sinusoidal components with phase shifts
        self.sin_frequencies = np.random.uniform(2.0, 12.0, dim)
        self.sin_amplitudes = np.random.uniform(0.5, 4.0, dim)
        self.sin_phases = np.random.uniform(0, 2*np.pi, dim)
        
    def f(self, x):
        x_norm = x / 5.0
        f_val = 0.0
        
        # Chaotic sine wave components
        for i in range(self.dim):
            f_val += self.chaos_factors[i] * np.sin(self.chaos_freqs[i] * x_norm[i]) * \
                     np.cos(self.chaos_freqs[i] * x_norm[i]) * \
                     np.exp(-x_norm[i]**2)
        
        # Enhanced radial basis function components
        for i in range(15):
            rbf_sum = 0.0
            for j in range(self.dim):
                rbf_sum += (x_norm[j] - self.rbf_centers[i, j])**2
            f_val += np.exp(-rbf_sum / (2 * self.rbf_widths[i]**2)) * \
                     np.sin(rbf_sum) * np.cos(rbf_sum)
        
        # Adaptive conditioning with exponential terms
        for i in range(self.dim):
            f_val += self.conditioning_factors[i] * np.abs(x_norm[i])**self.conditioning_exponents[i]
        
        # Cross-dimension coupling with chaotic interaction (modified strength and range)
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Reduced coupling range
                dist = np.sqrt((x_norm[i] - x_norm[j])**2 + 0.001)
                f_val += 1.2 * np.exp(-dist**2 / (2 * 0.25**2)) * \
                         np.sin(7 * dist) * np.cos(4 * dist)  # Increased frequency and amplitude
        
        # Multi-scale periodic components with phase modulation
        for scale in [0.1, 0.2, 0.5, 1.0, 2.0]:
            periodic_sum = 0.0
            for i in range(self.dim):
                periodic_sum += np.sin(scale * x_norm[i] + self.sin_phases[i]) * \
                               np.cos(scale * x_norm[i] + self.sin_phases[i])
            f_val += 0.7 * periodic_sum**3  # Increased weight
        
        # Add chaotic noise-like perturbations
        noise_perturbation = 0.15 * np.sum(np.sin(23 * x_norm) * np.cos(19 * x_norm))
        f_val += noise_perturbation
        
        # Add a global scaling factor to increase difficulty
        f_val *= (1.0 + 0.6 * np.sum(np.sin(x_norm)**2))  # Increased scaling
        
        return f_val