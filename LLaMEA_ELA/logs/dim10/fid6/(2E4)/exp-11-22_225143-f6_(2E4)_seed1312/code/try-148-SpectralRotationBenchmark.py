import numpy as np

class SpectralRotationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize rotation matrices using quaternion-inspired approach
        self.rotation_matrices = []
        for _ in range(4):
            angle = np.random.uniform(0, np.pi/4)
            cos_a, sin_a = np.cos(angle), np.sin(angle)
            matrix = np.array([[cos_a, -sin_a], [sin_a, cos_a]])
            self.rotation_matrices.append(matrix)
        
        # Spectral frequency components with varying scales
        self.freq_scales = np.random.uniform(0.5, 3.0, dim)
        self.freq_offsets = np.random.uniform(-1.0, 1.0, dim)
        
        # Exponential decay parameters for interaction strength
        self.decay_rates = np.random.uniform(0.1, 2.0, dim)
        self.decay_centers = np.random.uniform(-3.0, 3.0, dim)
        
        # Multi-scale harmonic components with randomized phases
        self.harmonic_amplitudes = np.random.uniform(0.5, 3.0, dim)
        self.harmonic_frequencies = np.random.uniform(2.0, 15.0, dim)
        self.harmonic_phases = np.random.uniform(0, 2*np.pi, dim)
        
        # Coupling coefficients between dimensions
        self.coupling_strengths = np.random.uniform(0.1, 1.5, (dim, dim))
        np.fill_diagonal(self.coupling_strengths, 0.0)
        
    def f(self, x):
        x_norm = x / 5.0
        f_val = 0.0
        
        # Spectral harmonic components with varying frequencies and amplitudes
        for i in range(self.dim):
            harmonic_component = self.harmonic_amplitudes[i] * np.sin(
                self.harmonic_frequencies[i] * x_norm[i] + self.harmonic_phases[i]
            )
            f_val += harmonic_component**3
        
        # Exponential decay interactions with multiple centers
        for i in range(self.dim):
            decay_term = np.exp(-self.decay_rates[i] * (x_norm[i] - self.decay_centers[i])**2)
            f_val += decay_term * np.sin(5 * x_norm[i])
        
        # Rotation-based coupling between dimensions
        for i in range(self.dim):
            rot_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    rot_sum += self.coupling_strengths[i, j] * x_norm[j]
            f_val += np.sin(x_norm[i] + rot_sum) * np.cos(x_norm[i] - rot_sum)
        
        # Multi-scale frequency modulation
        for scale in [0.1, 0.3, 0.7, 1.0, 2.0]:
            modulated_sum = 0.0
            for i in range(self.dim):
                freq = self.freq_scales[i] * scale + self.freq_offsets[i]
                modulated_sum += np.sin(freq * x_norm[i])
            f_val += np.exp(-modulated_sum**2) * np.cos(modulated_sum)
        
        # Quaternion-inspired rotation effects
        for i in range(0, self.dim - 1, 2):
            if i + 1 < self.dim:
                rot_matrix = self.rotation_matrices[i % len(self.rotation_matrices)]
                x_rotated = rot_matrix @ np.array([x_norm[i], x_norm[i+1]])
                f_val += np.exp(-np.sum(x_rotated**2)) * np.sin(np.sum(x_rotated))
        
        # Final normalization and scaling
        f_val *= (1.0 + 0.3 * np.sum(np.cos(x_norm)**2))
        
        return f_val