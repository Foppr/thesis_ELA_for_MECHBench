import numpy as np

class MultimodalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Ultra-chaotic sine wave parameters with fractal-like frequency modulation
        self.chaos_factors = np.random.uniform(0.5, 3.0, dim)
        self.chaos_freqs = np.random.uniform(15.0, 50.0, dim)
        # Super-conditioning with hyper-exponential scaling and dynamic exponents
        self.conditioning_factors = np.random.uniform(0.2, 2.0, dim)
        self.conditioning_exponents = np.random.uniform(5.0, 12.0, dim)
        # Fractal-like radial basis function centers with self-similar distribution
        self.rbf_centers = np.random.uniform(-4.5, 4.5, (40, dim))
        self.rbf_widths = np.random.uniform(0.05, 4.0, 40)
        # Multi-scale sinusoidal components with dynamic phase shifts and amplitude modulation
        self.sin_frequencies = np.random.uniform(3.0, 25.0, dim)
        self.sin_amplitudes = np.random.uniform(0.8, 8.0, dim)
        self.sin_phases = np.random.uniform(0, 4*np.pi, dim)
        
    def f(self, x):
        x_norm = x / 5.0
        f_val = 0.0
        
        # Ultra-chaotic sine wave components with hyper-non-linearity
        for i in range(self.dim):
            f_val += self.chaos_factors[i] * np.sin(self.chaos_freqs[i] * x_norm[i]) * \
                     np.cos(self.chaos_freqs[i] * x_norm[i]) * \
                     np.exp(-x_norm[i]**2) * (1.0 + 0.6 * np.sin(12 * x_norm[i]) * np.cos(8 * x_norm[i]))
        
        # Fractal-based radial basis function components with self-similar scaling
        for i in range(40):
            rbf_sum = 0.0
            for j in range(self.dim):
                rbf_sum += (x_norm[j] - self.rbf_centers[i, j])**2
            f_val += np.exp(-rbf_sum / (2 * self.rbf_widths[i]**2)) * \
                     np.sin(rbf_sum) * np.cos(rbf_sum) * \
                     (1.0 + 0.5 * np.cos(10 * rbf_sum) * np.sin(6 * rbf_sum))
        
        # Super-conditioning with hyper-exponential terms and dynamic scaling
        for i in range(self.dim):
            f_val += self.conditioning_factors[i] * np.abs(x_norm[i])**self.conditioning_exponents[i] * \
                     (1.0 + 0.3 * np.sin(6 * x_norm[i]) * np.cos(4 * x_norm[i]))
        
        # Multi-scale cross-dimension coupling with fractal-like interaction
        for i in range(self.dim):
            coupling_strength = 0.5 + 0.5 * np.sin(i * 0.8)
            for j in range(i+1, min(i+8, self.dim)):  # Extended coupling range
                dist = np.sqrt((x_norm[i] - x_norm[j])**2 + 0.001)
                f_val += coupling_strength * np.exp(-dist**2 / (2 * 0.4**2)) * \
                         np.sin(12 * dist) * np.cos(8 * dist) * \
                         (1.0 + 0.4 * np.cos(6 * dist) * np.sin(4 * dist))
        
        # Multi-scale periodic components with fractal self-similarity and phase modulation
        for scale in [0.02, 0.05, 0.1, 0.2, 0.4, 0.8, 1.6]:
            periodic_sum = 0.0
            for i in range(self.dim):
                periodic_sum += np.sin(scale * x_norm[i] + self.sin_phases[i]) * \
                               np.cos(scale * x_norm[i] + self.sin_phases[i])
            f_val += 0.5 * periodic_sum**4 * (1.0 + 0.4 * np.sin(8 * periodic_sum) * np.cos(6 * periodic_sum))
        
        # Add fractal-like noise perturbations with higher frequency components
        noise_perturbation = 0.3 * np.sum(np.sin(41 * x_norm) * np.cos(37 * x_norm) * \
                                          np.sin(29 * x_norm) * np.cos(23 * x_norm))
        f_val += noise_perturbation
        
        # Add a global scaling factor with ultra-high non-separability
        f_val *= (1.0 + 0.9 * np.sum(np.sin(x_norm)**5 + np.cos(x_norm)**5))
        
        return f_val