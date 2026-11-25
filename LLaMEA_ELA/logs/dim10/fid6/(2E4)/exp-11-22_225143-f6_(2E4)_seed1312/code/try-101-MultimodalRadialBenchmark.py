import numpy as np

class MultimodalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic sine wave parameters with quaternion-inspired phase modulation
        self.chaos_factors = np.random.uniform(0.8, 3.0, dim)
        self.chaos_freqs = np.random.uniform(5.0, 15.0, dim)
        # Adaptive conditioning with fractal-like scaling
        self.conditioning_factors = np.random.uniform(0.1, 1.5, dim)
        self.conditioning_exponents = np.random.uniform(3.0, 7.0, dim)
        # Radial basis function centers and widths with dynamic scaling
        self.rbf_centers = np.random.uniform(-4.5, 4.5, (20, dim))
        self.rbf_widths = np.random.uniform(0.3, 3.0, 20)
        # Multi-scale sinusoidal components with phase shifts and quaternion rotations
        self.sin_frequencies = np.random.uniform(2.0, 12.0, dim)
        self.sin_amplitudes = np.random.uniform(0.5, 4.0, dim)
        self.sin_phases = np.random.uniform(0, 2*np.pi, dim)
        # Quaternion-inspired rotational symmetry components
        self.quat_rotations = np.random.randn(4, dim)
        self.quat_rotations /= np.linalg.norm(self.quat_rotations, axis=0)
        
    def f(self, x):
        x_norm = x / 5.0
        f_val = 0.0
        
        # Chaotic sine wave components with quaternion modulation
        for i in range(self.dim):
            f_val += self.chaos_factors[i] * np.sin(self.chaos_freqs[i] * x_norm[i]) * \
                     np.cos(self.chaos_freqs[i] * x_norm[i]) * \
                     np.exp(-x_norm[i]**2)
        
        # Enhanced radial basis function components with fractal scaling
        for i in range(20):
            rbf_sum = 0.0
            for j in range(self.dim):
                rbf_sum += (x_norm[j] - self.rbf_centers[i, j])**2
            f_val += np.exp(-rbf_sum / (2 * self.rbf_widths[i]**2)) * \
                     np.sin(rbf_sum) * np.cos(rbf_sum)
        
        # Adaptive conditioning with exponential terms and fractal dimensionality
        for i in range(self.dim):
            f_val += self.conditioning_factors[i] * np.abs(x_norm[i])**self.conditioning_exponents[i]
        
        # Cross-dimension coupling with chaotic interaction and rotational symmetry
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling
                dist = np.sqrt((x_norm[i] - x_norm[j])**2 + 0.001)
                f_val += 0.8 * np.exp(-dist**2 / (2 * 0.3**2)) * \
                         np.sin(5 * dist) * np.cos(3 * dist)
        
        # Multi-scale periodic components with phase modulation and quaternion rotation
        for scale in [0.1, 0.2, 0.5, 1.0, 2.0]:
            periodic_sum = 0.0
            for i in range(self.dim):
                periodic_sum += np.sin(scale * x_norm[i] + self.sin_phases[i]) * \
                               np.cos(scale * x_norm[i] + self.sin_phases[i])
            f_val += 0.5 * periodic_sum**3
        
        # Add quaternion-based rotational symmetry perturbations
        quat_sum = 0.0
        for i in range(4):
            rot_component = 0.0
            for j in range(self.dim):
                rot_component += self.quat_rotations[i, j] * x_norm[j]
            quat_sum += np.sin(rot_component) * np.cos(rot_component)
        f_val += 0.3 * quat_sum**2
        
        # Add fractal-like self-similarity through multi-resolution scaling
        fractal_factor = 1.0 + 0.2 * np.sum(np.sin(x_norm)**2 + np.cos(x_norm)**2)
        f_val *= fractal_factor
        
        # Add chaotic noise-like perturbations with fractal dimensionality
        noise_perturbation = 0.1 * np.sum(np.sin(23 * x_norm) * np.cos(19 * x_norm))
        f_val += noise_perturbation
        
        return f_val