import numpy as np

class MultimodalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic sine wave parameters for increased complexity
        self.chaos_factors = np.random.uniform(0.5, 3.0, dim)
        self.chaos_freqs = np.random.uniform(10.0, 30.0, dim)
        # Adjusted conditioning with modified exponents for better separability
        self.conditioning_factors = np.random.uniform(0.2, 2.5, dim)
        self.conditioning_exponents = np.random.uniform(1.5, 7.0, dim)
        # Modified RBF centers and widths with improved distribution
        self.rbf_centers = np.random.uniform(-4.5, 4.5, (25, dim))
        self.rbf_widths = np.random.uniform(0.3, 3.0, 25)
        # Updated sinusoidal components with different frequencies and amplitudes
        self.sin_frequencies = np.random.uniform(2.0, 20.0, dim)
        self.sin_amplitudes = np.random.uniform(0.5, 6.0, dim)
        self.sin_phases = np.random.uniform(0, 2*np.pi, dim)
        # Reduced quaternion-like rotation angles
        self.rotation_angles = np.random.uniform(0, np.pi/8, dim)
        
    def f(self, x):
        x_norm = x / 5.0
        f_val = 0.0
        
        # Enhanced chaotic sine wave components with increased non-linearity
        for i in range(self.dim):
            rotated_x = x_norm[i] * np.cos(self.rotation_angles[i]) - x_norm[(i+1)%self.dim] * np.sin(self.rotation_angles[i])
            f_val += self.chaos_factors[i] * np.sin(self.chaos_freqs[i] * rotated_x) * \
                     np.cos(self.chaos_freqs[i] * rotated_x) * \
                     np.exp(-rotated_x**2) * (1.0 + 0.4 * np.sin(8 * rotated_x))
        
        # Enhanced radial basis function components with modified scaling
        for i in range(25):
            rbf_sum = 0.0
            for j in range(self.dim):
                rbf_sum += (x_norm[j] - self.rbf_centers[i, j])**2
            f_val += np.exp(-rbf_sum / (2 * self.rbf_widths[i]**2)) * \
                     np.sin(rbf_sum) * np.cos(rbf_sum) * \
                     (1.0 + 0.3 * np.cos(6 * rbf_sum))
        
        # Adaptive conditioning with modified exponents
        for i in range(self.dim):
            f_val += self.conditioning_factors[i] * np.abs(x_norm[i])**self.conditioning_exponents[i] * \
                     (1.0 + 0.2 * np.sin(4 * x_norm[i]))
        
        # Cross-dimension coupling with modified strength and range
        for i in range(self.dim):
            coupling_strength = 0.6 + 0.2 * np.sin(i * 0.7)
            for j in range(i+1, min(i+5, self.dim)):  # Slightly increased coupling range
                dist = np.sqrt((x_norm[i] - x_norm[j])**2 + 0.001)
                f_val += coupling_strength * np.exp(-dist**2 / (2 * 0.4**2)) * \
                         np.sin(8 * dist) * np.cos(4 * dist) * \
                         (1.0 + 0.2 * np.cos(4 * dist))
        
        # Multi-scale periodic components with altered scaling
        for scale in [0.03, 0.06, 0.12, 0.24, 0.48, 1.2, 2.4]:
            periodic_sum = 0.0
            for i in range(self.dim):
                periodic_sum += np.sin(scale * x_norm[i] + self.sin_phases[i]) * \
                               np.cos(scale * x_norm[i] + self.sin_phases[i])
            f_val += 0.4 * periodic_sum**3 * (1.0 + 0.3 * np.sin(6 * periodic_sum))
        
        # Enhanced noise perturbations
        noise_perturbation = 0.2 * np.sum(np.sin(31 * x_norm) * np.cos(25 * x_norm) * \
                                          np.sin(19 * x_norm) * np.cos(13 * x_norm))
        f_val += noise_perturbation
        
        # Modified global scaling factor
        f_val *= (1.0 + 0.6 * np.sum(np.sin(x_norm)**4))
        
        return f_val