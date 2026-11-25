import numpy as np

class ChaoticSineRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
        
        # Chaotic sine map parameters
        self.chaotic_freqs = np.random.uniform(0.5, 2.0, dim)
        self.chaotic_ampls = np.random.uniform(0.1, 0.8, dim)
        
        # Radial basis function parameters
        self.rbf_centers = np.random.uniform(-3.0, 3.0, (dim, 3))
        self.rbf_widths = np.random.uniform(0.5, 2.5, (dim, 3))
        self.rbf_weights = np.random.uniform(-1.0, 1.0, (dim, 3))
        
        # Adaptive noise scaling
        self.noise_scales = np.random.uniform(0.05, 0.3, dim)
        self.noise_frequencies = np.random.uniform(1.0, 8.0, dim)
        
        # Cross-dimensional interaction strength
        self.cross_strength = np.random.uniform(0.2, 1.5, dim)
        
    def f(self, x):
        x_norm = x / 5.0
        f_val = 0.0
        
        # Chaotic sine components
        for i in range(self.dim):
            chaotic_term = 0.0
            phase = 0.0
            for _ in range(100):
                phase = np.sin(self.chaotic_freqs[i] * phase + self.chaotic_ampls[i])
            for _ in range(20):
                phase = np.sin(self.chaotic_freqs[i] * phase + self.chaotic_ampls[i])
                chaotic_term += np.sin(phase * x_norm[i])
            f_val += 0.2 * chaotic_term**2
        
        # Radial basis function components
        for i in range(self.dim):
            rbf_sum = 0.0
            for j in range(3):
                rbf_sum += self.rbf_weights[i, j] * np.exp(-0.5 * ((x_norm[i] - self.rbf_centers[i, j]) / self.rbf_widths[i, j])**2)
            f_val += 0.3 * rbf_sum**2
        
        # Adaptive noise components
        for i in range(self.dim):
            noise_term = self.noise_scales[i] * np.sin(self.noise_frequencies[i] * x_norm[i])
            f_val += 0.15 * noise_term**2
        
        # Cross-dimensional coupling with RBF interaction
        for i in range(self.dim):
            cross_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    dist = np.abs(x_norm[i] - x_norm[j])
                    cross_sum += np.exp(-dist**2) * np.sin(x_norm[i] * x_norm[j])
            f_val += self.cross_strength[i] * cross_sum**2
        
        # Multi-scale periodic components
        for scale in [0.1, 0.3, 0.7, 1.0]:
            periodic_sum = 0.0
            for i in range(self.dim):
                periodic_sum += np.sin(scale * x_norm[i]) * np.cos(scale * 2 * x_norm[i])
            f_val += 0.25 * periodic_sum**2
        
        # Global shaping with polynomial terms
        f_val += 0.1 * np.sum(x_norm**4)
        
        return f_val