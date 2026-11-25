import numpy as np

class MultimodalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic sine wave parameters with higher frequency variability and added quaternion-like interactions
        self.chaos_factors = np.random.uniform(0.5, 3.0, dim)
        self.chaos_freqs = np.random.uniform(10.0, 40.0, dim)
        # Adaptive conditioning with exponential scaling and dynamic exponents
        self.conditioning_factors = np.random.uniform(0.1, 3.0, dim)
        self.conditioning_exponents = np.random.uniform(2.0, 15.0, dim)
        # Radial basis function centers and widths with fractal-like distribution
        self.rbf_centers = np.random.uniform(-4.5, 4.5, (30, dim))
        self.rbf_widths = np.random.uniform(0.1, 4.0, 30)
        # Multi-scale sinusoidal components with phase shifts and amplitude modulation
        self.sin_frequencies = np.random.uniform(2.0, 25.0, dim)
        self.sin_amplitudes = np.random.uniform(0.5, 7.0, dim)
        self.sin_phases = np.random.uniform(0, 2*np.pi, dim)
        # Quaternion-inspired rotational symmetry components
        self.rotation_angles = np.random.uniform(0, np.pi/3, dim)
        # Additional chaotic coupling terms and higher-order polynomial interactions
        self.coupling_strengths = np.random.uniform(0.5, 1.5, dim)
        self.poly_exponents = np.random.uniform(1.5, 8.0, dim)
        
    def f(self, x):
        x_norm = x / 5.0
        f_val = 0.0
        
        # Chaotic sine wave components with enhanced non-linearity and quaternion rotation
        for i in range(self.dim):
            rotated_x = x_norm[i] * np.cos(self.rotation_angles[i]) - x_norm[(i+1)%self.dim] * np.sin(self.rotation_angles[i])
            f_val += self.chaos_factors[i] * np.sin(self.chaos_freqs[i] * rotated_x) * \
                     np.cos(self.chaos_freqs[i] * rotated_x) * \
                     np.exp(-rotated_x**2) * (1.0 + 0.4 * np.sin(9 * rotated_x))
        
        # Enhanced radial basis function components with fractal-like scaling
        for i in range(30):
            rbf_sum = 0.0
            for j in range(self.dim):
                rbf_sum += (x_norm[j] - self.rbf_centers[i, j])**2
            f_val += np.exp(-rbf_sum / (2 * self.rbf_widths[i]**2)) * \
                     np.sin(rbf_sum) * np.cos(rbf_sum) * \
                     (1.0 + 0.25 * np.cos(7 * rbf_sum))
        
        # Adaptive conditioning with exponential terms and dynamic scaling
        for i in range(self.dim):
            f_val += self.conditioning_factors[i] * np.abs(x_norm[i])**self.conditioning_exponents[i] * \
                     (1.0 + 0.15 * np.sin(4 * x_norm[i]))
        
        # Cross-dimension coupling with chaotic interaction and dynamic coupling strength
        for i in range(self.dim):
            coupling_strength = self.coupling_strengths[i]
            for j in range(i+1, min(i+8, self.dim)):  # Increased coupling range
                dist = np.sqrt((x_norm[i] - x_norm[j])**2 + 0.001)
                f_val += coupling_strength * np.exp(-dist**2 / (2 * 0.3**2)) * \
                         np.sin(11 * dist) * np.cos(6 * dist) * \
                         (1.0 + 0.2 * np.cos(5 * dist))
        
        # Multi-scale periodic components with phase modulation and self-similarity
        for scale in [0.02, 0.05, 0.1, 0.2, 0.4, 0.8, 1.6, 3.2]:
            periodic_sum = 0.0
            for i in range(self.dim):
                periodic_sum += np.sin(scale * x_norm[i] + self.sin_phases[i]) * \
                               np.cos(scale * x_norm[i] + self.sin_phases[i])
            f_val += 0.5 * periodic_sum**7 * (1.0 + 0.3 * np.sin(8 * periodic_sum))
        
        # Add fractal-like noise perturbations with higher frequency components
        noise_perturbation = 0.3 * np.sum(np.sin(37 * x_norm) * np.cos(31 * x_norm) * \
                                          np.sin(23 * x_norm) * np.cos(17 * x_norm))
        f_val += noise_perturbation
        
        # Add a global scaling factor to increase difficulty and non-separability
        f_val *= (1.0 + 0.8 * np.sum(np.sin(x_norm)**5))
        
        # Add higher-order polynomial terms for increased complexity
        poly_term = 0.0
        for i in range(self.dim):
            poly_term += self.poly_exponents[i] * x_norm[i]**6
        f_val += 0.1 * poly_term
        
        return f_val