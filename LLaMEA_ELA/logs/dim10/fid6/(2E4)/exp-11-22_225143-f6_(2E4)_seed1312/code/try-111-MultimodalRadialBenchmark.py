import numpy as np

class MultimodalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic sine wave parameters with higher frequency variation
        self.chaos_factors = np.random.uniform(1.0, 4.0, dim)
        self.chaos_freqs = np.random.uniform(8.0, 25.0, dim)
        # Enhanced adaptive conditioning with logarithmic scaling
        self.conditioning_factors = np.random.uniform(0.2, 2.0, dim)
        self.conditioning_exponents = np.random.uniform(4.0, 10.0, dim)
        # Radial basis function centers and widths with fractal-like distribution
        self.rbf_centers = np.random.uniform(-4.8, 4.8, (25, dim))
        self.rbf_widths = np.random.uniform(0.2, 4.0, 25)
        # Multi-scale sinusoidal components with quaternion-inspired phase shifts
        self.sin_frequencies = np.random.uniform(3.0, 20.0, dim)
        self.sin_amplitudes = np.random.uniform(1.0, 6.0, dim)
        self.sin_phases = np.random.uniform(0, 4*np.pi, dim)
        # Quaternion-inspired rotational symmetry components
        self.rotation_angles = np.random.uniform(0, 2*np.pi, dim//2 + 1) if dim % 2 == 0 else np.random.uniform(0, 2*np.pi, dim//2)
        
    def f(self, x):
        x_norm = x / 5.0
        f_val = 0.0
        
        # Chaotic sine wave components with enhanced nonlinearity
        for i in range(self.dim):
            f_val += self.chaos_factors[i] * np.sin(self.chaos_freqs[i] * x_norm[i]) * \
                     np.cos(self.chaos_freqs[i] * x_norm[i]) * \
                     np.exp(-x_norm[i]**2) * np.sin(7 * x_norm[i])
        
        # Enhanced radial basis function components with fractal scaling
        for i in range(25):
            rbf_sum = 0.0
            for j in range(self.dim):
                rbf_sum += (x_norm[j] - self.rbf_centers[i, j])**2
            f_val += np.exp(-rbf_sum / (2 * self.rbf_widths[i]**2)) * \
                     np.sin(rbf_sum) * np.cos(rbf_sum) * \
                     (1 + 0.3 * np.sin(3 * rbf_sum))
        
        # Adaptive conditioning with exponential terms and logarithmic scaling
        for i in range(self.dim):
            f_val += self.conditioning_factors[i] * np.log(1 + np.abs(x_norm[i]))**self.conditioning_exponents[i]
        
        # Cross-dimension coupling with chaotic interaction and rotational symmetry
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Increased coupling range
                dist = np.sqrt((x_norm[i] - x_norm[j])**2 + 0.001)
                rotation_term = np.sin(self.rotation_angles[i % len(self.rotation_angles)] * dist)
                f_val += 1.2 * np.exp(-dist**2 / (2 * 0.4**2)) * \
                         np.sin(7 * dist) * np.cos(5 * dist) * rotation_term
        
        # Multi-scale periodic components with quaternion-inspired modulation
        for scale in [0.05, 0.1, 0.2, 0.4, 0.8, 1.6]:
            periodic_sum = 0.0
            for i in range(self.dim):
                periodic_sum += np.sin(scale * x_norm[i] + self.sin_phases[i]) * \
                               np.cos(scale * x_norm[i] + self.sin_phases[i])
            f_val += 0.8 * periodic_sum**5
        
        # Add chaotic noise-like perturbations with higher frequency
        noise_perturbation = 0.2 * np.sum(np.sin(31 * x_norm) * np.cos(29 * x_norm))
        f_val += noise_perturbation
        
        # Add a global scaling factor to increase difficulty with fractal characteristics
        f_val *= (1.0 + 0.8 * np.sum(np.sin(x_norm)**4))
        
        return f_val