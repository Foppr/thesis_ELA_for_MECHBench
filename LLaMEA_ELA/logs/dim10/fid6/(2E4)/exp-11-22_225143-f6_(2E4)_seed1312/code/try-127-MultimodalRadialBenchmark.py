import numpy as np

class MultimodalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic sine wave parameters with higher frequency variability and amplitude modulation
        self.chaos_factors = np.random.uniform(1.0, 3.0, dim)
        self.chaos_freqs = np.random.uniform(12.0, 35.0, dim)
        # Adaptive conditioning with exponential scaling, dynamic exponents, and additional noise
        self.conditioning_factors = np.random.uniform(0.3, 2.5, dim)
        self.conditioning_exponents = np.random.uniform(5.0, 12.0, dim)
        # Radial basis function centers and widths with fractal-like distribution and increased complexity
        self.rbf_centers = np.random.uniform(-4.5, 4.5, (30, dim))
        self.rbf_widths = np.random.uniform(0.1, 3.0, 30)
        # Multi-scale sinusoidal components with phase shifts, amplitude modulation, and added complexity
        self.sin_frequencies = np.random.uniform(4.0, 20.0, dim)
        self.sin_amplitudes = np.random.uniform(1.0, 6.0, dim)
        self.sin_phases = np.random.uniform(0, 2*np.pi, dim)
        # Additional quaternion-inspired rotational symmetry components
        self.rotation_angles = np.random.uniform(0, np.pi, dim)
        
    def f(self, x):
        x_norm = x / 5.0
        f_val = 0.0
        
        # Enhanced chaotic sine wave components with higher non-linearity and fractal-like behavior
        for i in range(self.dim):
            f_val += self.chaos_factors[i] * np.sin(self.chaos_freqs[i] * x_norm[i]) * \
                     np.cos(self.chaos_freqs[i] * x_norm[i]) * \
                     np.exp(-x_norm[i]**2) * (1.0 + 0.4 * np.sin(7 * x_norm[i])) * \
                     (1.0 + 0.1 * np.cos(13 * x_norm[i]))
        
        # Enhanced radial basis function components with fractal-like scaling and increased complexity
        for i in range(30):
            rbf_sum = 0.0
            for j in range(self.dim):
                rbf_sum += (x_norm[j] - self.rbf_centers[i, j])**2
            f_val += np.exp(-rbf_sum / (2 * self.rbf_widths[i]**2)) * \
                     np.sin(rbf_sum) * np.cos(rbf_sum) * \
                     (1.0 + 0.3 * np.cos(5 * rbf_sum)) * \
                     (1.0 + 0.1 * np.sin(9 * rbf_sum))
        
        # Enhanced adaptive conditioning with exponential terms, dynamic scaling, and noise
        for i in range(self.dim):
            f_val += self.conditioning_factors[i] * np.abs(x_norm[i])**self.conditioning_exponents[i] * \
                     (1.0 + 0.2 * np.sin(3 * x_norm[i])) * \
                     (1.0 + 0.1 * np.cos(7 * x_norm[i]))
        
        # Increased cross-dimension coupling with chaotic interaction, dynamic coupling strength, and rotational symmetry
        for i in range(self.dim):
            coupling_strength = 0.6 + 0.4 * np.sin(i * self.rotation_angles[i % len(self.rotation_angles)])
            for j in range(i+1, min(i+7, self.dim)):  # Increased coupling range
                dist = np.sqrt((x_norm[i] - x_norm[j])**2 + 0.001)
                f_val += coupling_strength * np.exp(-dist**2 / (2 * 0.3**2)) * \
                         np.sin(9 * dist) * np.cos(5 * dist) * \
                         (1.0 + 0.2 * np.cos(4 * dist)) * \
                         (1.0 + 0.1 * np.sin(6 * dist))
        
        # Enhanced multi-scale periodic components with phase modulation, self-similarity, and additional noise
        for scale in [0.03, 0.07, 0.15, 0.3, 0.6, 1.2, 2.4]:
            periodic_sum = 0.0
            for i in range(self.dim):
                periodic_sum += np.sin(scale * x_norm[i] + self.sin_phases[i]) * \
                               np.cos(scale * x_norm[i] + self.sin_phases[i])
            f_val += 0.4 * periodic_sum**5 * (1.0 + 0.3 * np.sin(5 * periodic_sum)) * \
                     (1.0 + 0.1 * np.cos(8 * periodic_sum))
        
        # Enhanced fractal-like noise perturbations with increased complexity
        noise_perturbation = 0.2 * np.sum(np.sin(31 * x_norm) * np.cos(29 * x_norm) * \
                                          np.sin(19 * x_norm) * np.cos(13 * x_norm))
        f_val += noise_perturbation
        
        # Add a global scaling factor to increase difficulty and non-separability
        f_val *= (1.0 + 0.8 * np.sum(np.sin(x_norm)**4)) * \
                 (1.0 + 0.2 * np.sum(np.cos(x_norm)**3))
        
        return f_val