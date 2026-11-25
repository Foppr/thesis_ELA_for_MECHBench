import numpy as np

class ChaoticSineRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
        
        # Chaotic sine map parameters with increased complexity
        self.chaotic_freqs = np.random.uniform(1.2, 3.5, dim)
        self.chaotic_ampls = np.random.uniform(0.3, 1.2, dim)
        
        # Radial basis function parameters with altered weights and widths
        self.rbf_centers = np.random.uniform(-4.0, 4.0, (dim, 4))
        self.rbf_widths = np.random.uniform(0.3, 3.0, (dim, 4))
        self.rbf_weights = np.random.uniform(-1.5, 1.5, (dim, 4))
        
        # Adaptive noise scaling with modified parameters
        self.noise_scales = np.random.uniform(0.1, 0.5, dim)
        self.noise_frequencies = np.random.uniform(2.0, 12.0, dim)
        
        # Cross-dimensional interaction strength with increased coupling
        self.cross_strength = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        x_norm = x / 5.0
        f_val = 0.0
        
        # Chaotic sine components with higher iteration count
        for i in range(self.dim):
            chaotic_term = 0.0
            phase = 0.0
            for _ in range(150):
                phase = np.sin(self.chaotic_freqs[i] * phase + self.chaotic_ampls[i])
            for _ in range(30):
                phase = np.sin(self.chaotic_freqs[i] * phase + self.chaotic_ampls[i])
                chaotic_term += np.sin(phase * x_norm[i])
            f_val += 0.3 * chaotic_term**2
        
        # Radial basis function components with increased number of RBFs
        for i in range(self.dim):
            rbf_sum = 0.0
            for j in range(4):
                rbf_sum += self.rbf_weights[i, j] * np.exp(-0.5 * ((x_norm[i] - self.rbf_centers[i, j]) / self.rbf_widths[i, j])**2)
            f_val += 0.4 * rbf_sum**2
        
        # Adaptive noise components with higher frequency
        for i in range(self.dim):
            noise_term = self.noise_scales[i] * np.sin(self.noise_frequencies[i] * x_norm[i])
            f_val += 0.2 * noise_term**2
        
        # Cross-dimensional coupling with enhanced interaction
        for i in range(self.dim):
            cross_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    dist = np.abs(x_norm[i] - x_norm[j])
                    cross_sum += np.exp(-dist**2) * np.sin(x_norm[i] * x_norm[j]) * np.cos(x_norm[i] + x_norm[j])
            f_val += self.cross_strength[i] * cross_sum**2
        
        # Multi-scale periodic components with additional harmonics
        for scale in [0.15, 0.25, 0.4, 0.6, 0.8]:
            periodic_sum = 0.0
            for i in range(self.dim):
                periodic_sum += np.sin(scale * x_norm[i]) * np.cos(scale * 3 * x_norm[i]) + np.sin(scale * 2 * x_norm[i])
            f_val += 0.3 * periodic_sum**2
        
        # Global shaping with polynomial terms and additional quartic component
        f_val += 0.15 * np.sum(x_norm**4) + 0.05 * np.sum(x_norm**6)
        
        return f_val