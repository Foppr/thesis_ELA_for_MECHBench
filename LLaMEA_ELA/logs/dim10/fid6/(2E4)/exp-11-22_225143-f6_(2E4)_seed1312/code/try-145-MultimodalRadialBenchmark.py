import numpy as np

class MultimodalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic sine wave parameters with higher frequency variability and non-linearity
        self.chaos_factors = np.random.uniform(0.5, 3.0, dim)
        self.chaos_freqs = np.random.uniform(15.0, 50.0, dim)
        # Stronger conditioning with power-law scaling and dynamic exponents
        self.conditioning_factors = np.random.uniform(0.2, 2.0, dim)
        self.conditioning_exponents = np.random.uniform(4.0, 12.0, dim)
        # Fractal-like RBF centers with self-similar distribution patterns
        self.rbf_centers = np.random.uniform(-4.5, 4.5, (40, dim))
        self.rbf_widths = np.random.uniform(0.05, 4.0, 40)
        # Multi-scale sinusoidal components with complex phase interactions and amplitude modulation
        self.sin_frequencies = np.random.uniform(3.0, 25.0, dim)
        self.sin_amplitudes = np.random.uniform(1.0, 8.0, dim)
        self.sin_phases = np.random.uniform(0, 4*np.pi, dim)
        
    def f(self, x):
        x_norm = x / 5.0
        f_val = 0.0
        
        # Enhanced chaotic sine wave components with higher-order non-linearity and frequency modulation
        for i in range(self.dim):
            f_val += self.chaos_factors[i] * np.sin(self.chaos_freqs[i] * x_norm[i]) * \
                     np.cos(self.chaos_freqs[i] * x_norm[i]) * \
                     np.exp(-x_norm[i]**2) * (1.0 + 0.5 * np.sin(12 * x_norm[i]) + 0.3 * np.cos(7 * x_norm[i]))
        
        # Fractal-like radial basis function components with increased complexity and self-similarity
        for i in range(40):
            rbf_sum = 0.0
            for j in range(self.dim):
                rbf_sum += (x_norm[j] - self.rbf_centers[i, j])**2
            f_val += np.exp(-rbf_sum / (2 * self.rbf_widths[i]**2)) * \
                     np.sin(rbf_sum) * np.cos(rbf_sum) * \
                     (1.0 + 0.4 * np.cos(8 * rbf_sum) + 0.2 * np.sin(5 * rbf_sum))
        
        # Enhanced adaptive conditioning with exponential and power-law terms
        for i in range(self.dim):
            f_val += self.conditioning_factors[i] * np.abs(x_norm[i])**self.conditioning_exponents[i] * \
                     (1.0 + 0.3 * np.sin(6 * x_norm[i]) + 0.2 * np.cos(9 * x_norm[i]))
        
        # Increased cross-dimension coupling with long-range interactions and enhanced coupling strength
        for i in range(self.dim):
            coupling_strength = 0.5 + 0.5 * np.sin(i * 0.7) * np.cos(i * 0.3)
            for j in range(i+1, min(i+10, self.dim)):  # Extended coupling range
                dist = np.sqrt((x_norm[i] - x_norm[j])**2 + 0.001)
                f_val += coupling_strength * np.exp(-dist**2 / (2 * 0.4**2)) * \
                         np.sin(12 * dist) * np.cos(8 * dist) * \
                         (1.0 + 0.3 * np.cos(6 * dist) + 0.1 * np.sin(10 * dist))
        
        # Multi-scale periodic components with self-similarity and fractal-like behavior
        for scale in [0.02, 0.05, 0.1, 0.2, 0.4, 0.8, 1.6]:
            periodic_sum = 0.0
            for i in range(self.dim):
                periodic_sum += np.sin(scale * x_norm[i] + self.sin_phases[i]) * \
                               np.cos(scale * x_norm[i] + self.sin_phases[i])
            f_val += 0.5 * periodic_sum**4 * (1.0 + 0.4 * np.sin(8 * periodic_sum) + 0.2 * np.cos(6 * periodic_sum))
        
        # Add fractal-like noise perturbations with increased complexity
        noise_perturbation = 0.3 * np.sum(np.sin(41 * x_norm) * np.cos(37 * x_norm) * \
                                          np.sin(29 * x_norm) * np.cos(23 * x_norm))
        f_val += noise_perturbation
        
        # Add global scaling factor with enhanced non-separability and complexity
        f_val *= (1.0 + 0.8 * np.sum(np.sin(x_norm)**5) + 0.3 * np.sum(np.cos(x_norm)**3))
        
        return f_val