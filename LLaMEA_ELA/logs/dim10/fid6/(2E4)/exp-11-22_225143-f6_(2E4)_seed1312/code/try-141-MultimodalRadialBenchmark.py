import numpy as np

class MultimodalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic sine wave parameters with altered frequency variability
        self.chaos_factors = np.random.uniform(0.3, 2.0, dim)
        self.chaos_freqs = np.random.uniform(10.0, 30.0, dim)
        # Adaptive conditioning with modified scaling and exponents
        self.conditioning_factors = np.random.uniform(0.1, 1.5, dim)
        self.conditioning_exponents = np.random.uniform(3.0, 8.0, dim)
        # Radial basis function centers and widths with altered fractal-like distribution
        self.rbf_centers = np.random.uniform(-4.0, 4.0, (25, dim))
        self.rbf_widths = np.random.uniform(0.1, 3.0, 25)
        # Multi-scale sinusoidal components with phase shifts and amplitude modulation
        self.sin_frequencies = np.random.uniform(2.0, 18.0, dim)
        self.sin_amplitudes = np.random.uniform(0.5, 6.0, dim)
        self.sin_phases = np.random.uniform(0, 2*np.pi, dim)
        
    def f(self, x):
        x_norm = x / 5.0
        f_val = 0.0
        
        # Chaotic sine wave components with enhanced non-linearity
        for i in range(self.dim):
            f_val += self.chaos_factors[i] * np.sin(self.chaos_freqs[i] * x_norm[i]) * \
                     np.cos(self.chaos_freqs[i] * x_norm[i]) * \
                     np.exp(-x_norm[i]**2) * (1.0 + 0.4 * np.sin(8 * x_norm[i]))
        
        # Enhanced radial basis function components with altered scaling
        for i in range(25):
            rbf_sum = 0.0
            for j in range(self.dim):
                rbf_sum += (x_norm[j] - self.rbf_centers[i, j])**2
            f_val += np.exp(-rbf_sum / (2 * self.rbf_widths[i]**2)) * \
                     np.sin(rbf_sum) * np.cos(rbf_sum) * \
                     (1.0 + 0.3 * np.cos(6 * rbf_sum))
        
        # Adaptive conditioning with exponential terms and dynamic scaling
        for i in range(self.dim):
            f_val += self.conditioning_factors[i] * np.abs(x_norm[i])**self.conditioning_exponents[i] * \
                     (1.0 + 0.2 * np.sin(4 * x_norm[i]))
        
        # Cross-dimension coupling with altered interaction and coupling strength
        for i in range(self.dim):
            coupling_strength = 0.3 + 0.7 * np.sin(i * 0.5)
            for j in range(i+1, min(i+6, self.dim)):  # Increased coupling range
                dist = np.sqrt((x_norm[i] - x_norm[j])**2 + 0.001)
                f_val += coupling_strength * np.exp(-dist**2 / (2 * 0.3**2)) * \
                         np.sin(9 * dist) * np.cos(5 * dist) * \
                         (1.0 + 0.2 * np.cos(4 * dist))
        
        # Multi-scale periodic components with phase modulation and self-similarity
        for scale in [0.03, 0.07, 0.15, 0.3, 0.6, 1.2]:
            periodic_sum = 0.0
            for i in range(self.dim):
                periodic_sum += np.sin(scale * x_norm[i] + self.sin_phases[i]) * \
                               np.cos(scale * x_norm[i] + self.sin_phases[i])
            f_val += 0.4 * periodic_sum**3 * (1.0 + 0.3 * np.sin(6 * periodic_sum))
        
        # Add fractal-like noise perturbations
        noise_perturbation = 0.2 * np.sum(np.sin(31 * x_norm) * np.cos(25 * x_norm) * \
                                          np.sin(19 * x_norm))
        f_val += noise_perturbation
        
        # Add a global scaling factor to increase difficulty and non-separability
        f_val *= (1.0 + 0.7 * np.sum(np.sin(x_norm)**4))
        
        return f_val