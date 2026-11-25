import numpy as np

class MultimodalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Slightly modified chaotic sine wave parameters for better balance
        self.chaos_factors = np.random.uniform(0.3, 2.5, dim)
        self.chaos_freqs = np.random.uniform(8.0, 25.0, dim)
        # Adjusted conditioning with reduced exponents for improved separability
        self.conditioning_factors = np.random.uniform(0.1, 2.0, dim)
        self.conditioning_exponents = np.random.uniform(2.0, 8.0, dim)
        # Modified RBF centers and widths with more uniform distribution
        self.rbf_centers = np.random.uniform(-4.0, 4.0, (20, dim))
        self.rbf_widths = np.random.uniform(0.2, 2.5, 20)
        # Updated sinusoidal components with different frequencies and amplitudes
        self.sin_frequencies = np.random.uniform(1.5, 18.0, dim)
        self.sin_amplitudes = np.random.uniform(0.3, 5.0, dim)
        self.sin_phases = np.random.uniform(0, 2*np.pi, dim)
        # Reduced quaternion-like rotation angles
        self.rotation_angles = np.random.uniform(0, np.pi/6, dim)
        
    def f(self, x):
        x_norm = x / 5.0
        f_val = 0.0
        
        # Chaotic sine wave components with modified non-linearity
        for i in range(self.dim):
            rotated_x = x_norm[i] * np.cos(self.rotation_angles[i]) - x_norm[(i+1)%self.dim] * np.sin(self.rotation_angles[i])
            f_val += self.chaos_factors[i] * np.sin(self.chaos_freqs[i] * rotated_x) * \
                     np.cos(self.chaos_freqs[i] * rotated_x) * \
                     np.exp(-rotated_x**2) * (1.0 + 0.3 * np.sin(7 * rotated_x))
        
        # Radial basis function components with modified scaling
        for i in range(20):
            rbf_sum = 0.0
            for j in range(self.dim):
                rbf_sum += (x_norm[j] - self.rbf_centers[i, j])**2
            f_val += np.exp(-rbf_sum / (2 * self.rbf_widths[i]**2)) * \
                     np.sin(rbf_sum) * np.cos(rbf_sum) * \
                     (1.0 + 0.2 * np.cos(5 * rbf_sum))
        
        # Adaptive conditioning with modified exponents
        for i in range(self.dim):
            f_val += self.conditioning_factors[i] * np.abs(x_norm[i])**self.conditioning_exponents[i] * \
                     (1.0 + 0.1 * np.sin(3 * x_norm[i]))
        
        # Cross-dimension coupling with modified strength and range
        for i in range(self.dim):
            coupling_strength = 0.5 + 0.3 * np.sin(i * 0.5)
            for j in range(i+1, min(i+4, self.dim)):  # Reduced coupling range
                dist = np.sqrt((x_norm[i] - x_norm[j])**2 + 0.001)
                f_val += coupling_strength * np.exp(-dist**2 / (2 * 0.3**2)) * \
                         np.sin(7 * dist) * np.cos(3 * dist) * \
                         (1.0 + 0.15 * np.cos(3 * dist))
        
        # Multi-scale periodic components with altered scaling
        for scale in [0.02, 0.05, 0.1, 0.2, 0.4, 0.8, 1.6]:
            periodic_sum = 0.0
            for i in range(self.dim):
                periodic_sum += np.sin(scale * x_norm[i] + self.sin_phases[i]) * \
                               np.cos(scale * x_norm[i] + self.sin_phases[i])
            f_val += 0.3 * periodic_sum**4 * (1.0 + 0.25 * np.sin(5 * periodic_sum))
        
        # Reduced noise perturbations
        noise_perturbation = 0.15 * np.sum(np.sin(29 * x_norm) * np.cos(23 * x_norm) * \
                                           np.sin(17 * x_norm) * np.cos(11 * x_norm))
        f_val += noise_perturbation
        
        # Modified global scaling factor
        f_val *= (1.0 + 0.5 * np.sum(np.sin(x_norm)**3))
        
        return f_val