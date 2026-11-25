import numpy as np

class MultimodalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Significantly amplified chaotic sine wave parameters for higher complexity
        self.chaos_factors = np.random.uniform(1.5, 6.0, dim)
        self.chaos_freqs = np.random.uniform(20.0, 50.0, dim)
        # Increased conditioning exponents and altered factors for greater non-separability
        self.conditioning_factors = np.random.uniform(0.5, 4.0, dim)
        self.conditioning_exponents = np.random.uniform(5.0, 15.0, dim)
        # Expanded RBF centers with tighter clustering and modified widths
        self.rbf_centers = np.random.uniform(-4.5, 4.5, (50, dim))
        self.rbf_widths = np.random.uniform(0.1, 1.8, 50)
        # Enhanced sinusoidal components with higher frequencies and amplitudes
        self.sin_frequencies = np.random.uniform(5.0, 30.0, dim)
        self.sin_amplitudes = np.random.uniform(1.0, 8.0, dim)
        self.sin_phases = np.random.uniform(0, 2*np.pi, dim)
        # Increased quaternion-like rotation angles for stronger coupling
        self.rotation_angles = np.random.uniform(0, np.pi/3, dim)
        
    def f(self, x):
        x_norm = x / 5.0
        f_val = 0.0
        
        # Enhanced chaotic sine wave components with increased non-linearity
        for i in range(self.dim):
            rotated_x = x_norm[i] * np.cos(self.rotation_angles[i]) - x_norm[(i+1)%self.dim] * np.sin(self.rotation_angles[i])
            f_val += self.chaos_factors[i] * np.sin(self.chaos_freqs[i] * rotated_x) * \
                     np.cos(self.chaos_freqs[i] * rotated_x) * \
                     np.exp(-rotated_x**2) * (1.0 + 0.5 * np.sin(13 * rotated_x)) * \
                     (1.0 + 0.3 * np.cos(9 * rotated_x))
        
        # Enhanced radial basis function components with stronger interactions
        for i in range(50):
            rbf_sum = 0.0
            for j in range(self.dim):
                rbf_sum += (x_norm[j] - self.rbf_centers[i, j])**2
            f_val += np.exp(-rbf_sum / (2 * self.rbf_widths[i]**2)) * \
                     np.sin(rbf_sum) * np.cos(rbf_sum) * \
                     (1.0 + 0.4 * np.cos(7 * rbf_sum)) * \
                     (1.0 + 0.2 * np.sin(5 * rbf_sum))
        
        # Stronger adaptive conditioning with higher exponents
        for i in range(self.dim):
            f_val += self.conditioning_factors[i] * np.abs(x_norm[i])**self.conditioning_exponents[i] * \
                     (1.0 + 0.3 * np.sin(5 * x_norm[i])) * \
                     (1.0 + 0.2 * np.cos(3 * x_norm[i]))
        
        # Intensified cross-dimension coupling with extended range
        for i in range(self.dim):
            coupling_strength = 0.8 + 0.4 * np.sin(i * 0.7)
            for j in range(max(0, i-5), min(i+6, self.dim)):  # Extended coupling range
                if i != j:
                    dist = np.sqrt((x_norm[i] - x_norm[j])**2 + 0.001)
                    f_val += coupling_strength * np.exp(-dist**2 / (2 * 0.2**2)) * \
                             np.sin(11 * dist) * np.cos(7 * dist) * \
                             (1.0 + 0.3 * np.cos(5 * dist)) * \
                             (1.0 + 0.2 * np.sin(9 * dist))
        
        # Multi-scale periodic components with stronger interference
        for scale in [0.01, 0.03, 0.07, 0.15, 0.3, 0.6, 1.2, 2.4]:
            periodic_sum = 0.0
            for i in range(self.dim):
                periodic_sum += np.sin(scale * x_norm[i] + self.sin_phases[i]) * \
                               np.cos(scale * x_norm[i] + self.sin_phases[i])
            f_val += 0.5 * periodic_sum**5 * (1.0 + 0.4 * np.sin(7 * periodic_sum)) * \
                     (1.0 + 0.3 * np.cos(4 * periodic_sum))
        
        # Stronger noise perturbations with more complex interactions
        noise_perturbation = 0.3 * np.sum(np.sin(31 * x_norm) * np.cos(29 * x_norm) * \
                                          np.sin(19 * x_norm) * np.cos(13 * x_norm))
        f_val += noise_perturbation
        
        # Enhanced global scaling factor with higher non-linearity
        f_val *= (1.0 + 0.8 * np.sum(np.sin(x_norm)**4))
        
        return f_val