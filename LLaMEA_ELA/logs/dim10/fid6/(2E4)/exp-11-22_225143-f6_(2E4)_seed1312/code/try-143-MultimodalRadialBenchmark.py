import numpy as np

class MultimodalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic sine wave parameters for greater non-linearity
        self.chaos_factors = np.random.uniform(1.0, 4.0, dim)
        self.chaos_freqs = np.random.uniform(15.0, 40.0, dim)
        # Increased conditioning exponents and altered scaling for higher difficulty
        self.conditioning_factors = np.random.uniform(0.2, 3.0, dim)
        self.conditioning_exponents = np.random.uniform(5.0, 15.0, dim)
        # Expanded RBF centers with greater diversity and modified widths
        self.rbf_centers = np.random.uniform(-4.5, 4.5, (30, dim))
        self.rbf_widths = np.random.uniform(0.1, 3.0, 30)
        # Modified sinusoidal components with higher frequencies and amplitudes
        self.sin_frequencies = np.random.uniform(5.0, 25.0, dim)
        self.sin_amplitudes = np.random.uniform(1.0, 8.0, dim)
        self.sin_phases = np.random.uniform(0, 2*np.pi, dim)
        # Increased rotation angles for stronger dimension coupling
        self.rotation_angles = np.random.uniform(0, np.pi/3, dim)
        
    def f(self, x):
        x_norm = x / 5.0
        f_val = 0.0
        
        # Enhanced chaotic sine wave components with higher non-linearity
        for i in range(self.dim):
            rotated_x = x_norm[i] * np.cos(self.rotation_angles[i]) - x_norm[(i+1)%self.dim] * np.sin(self.rotation_angles[i])
            f_val += self.chaos_factors[i] * np.sin(self.chaos_freqs[i] * rotated_x)**3 * \
                     np.cos(self.chaos_freqs[i] * rotated_x)**2 * \
                     np.exp(-rotated_x**2) * (1.0 + 0.5 * np.sin(9 * rotated_x))
        
        # Expanded radial basis function components with stronger interactions
        for i in range(30):
            rbf_sum = 0.0
            for j in range(self.dim):
                rbf_sum += (x_norm[j] - self.rbf_centers[i, j])**2
            f_val += np.exp(-rbf_sum / (2 * self.rbf_widths[i]**2)) * \
                     np.sin(rbf_sum)**2 * np.cos(rbf_sum)**3 * \
                     (1.0 + 0.3 * np.cos(7 * rbf_sum))
        
        # Stronger adaptive conditioning with higher exponents
        for i in range(self.dim):
            f_val += self.conditioning_factors[i] * np.abs(x_norm[i])**self.conditioning_exponents[i] * \
                     (1.0 + 0.2 * np.sin(5 * x_norm[i]))
        
        # Increased cross-dimension coupling with wider interaction range
        for i in range(self.dim):
            coupling_strength = 0.8 + 0.4 * np.sin(i * 0.7)
            for j in range(i+1, min(i+6, self.dim)):  # Extended coupling range
                dist = np.sqrt((x_norm[i] - x_norm[j])**2 + 0.001)
                f_val += coupling_strength * np.exp(-dist**2 / (2 * 0.4**2)) * \
                         np.sin(9 * dist) * np.cos(5 * dist) * \
                         (1.0 + 0.2 * np.cos(5 * dist))
        
        # Multi-scale periodic components with increased complexity
        for scale in [0.01, 0.03, 0.07, 0.15, 0.3, 0.6, 1.2, 2.4]:
            periodic_sum = 0.0
            for i in range(self.dim):
                periodic_sum += np.sin(scale * x_norm[i] + self.sin_phases[i]) * \
                               np.cos(scale * x_norm[i] + self.sin_phases[i])
            f_val += 0.5 * periodic_sum**5 * (1.0 + 0.3 * np.sin(7 * periodic_sum))
        
        # Increased noise perturbations
        noise_perturbation = 0.3 * np.sum(np.sin(31 * x_norm) * np.cos(29 * x_norm) * \
                                          np.sin(19 * x_norm) * np.cos(13 * x_norm))
        f_val += noise_perturbation
        
        # Stronger global scaling factor
        f_val *= (1.0 + 0.7 * np.sum(np.sin(x_norm)**4))
        
        return f_val