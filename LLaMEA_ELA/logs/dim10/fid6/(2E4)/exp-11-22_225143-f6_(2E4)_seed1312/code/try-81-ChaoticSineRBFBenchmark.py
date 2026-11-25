import numpy as np

class ChaoticSineRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
        
        # Chaotic sine map parameters with increased complexity
        self.chaotic_freqs = np.random.uniform(1.0, 3.0, dim)
        self.chaotic_ampls = np.random.uniform(0.2, 1.0, dim)
        self.chaotic_dampings = np.random.uniform(0.8, 1.2, dim)
        
        # Enhanced radial basis function parameters
        self.rbf_centers = np.random.uniform(-4.0, 4.0, (dim, 5))
        self.rbf_widths = np.random.uniform(0.3, 3.0, (dim, 5))
        self.rbf_weights = np.random.uniform(-1.5, 1.5, (dim, 5))
        
        # Adaptive noise scaling with frequency modulation
        self.noise_scales = np.random.uniform(0.08, 0.4, dim)
        self.noise_frequencies = np.random.uniform(2.0, 12.0, dim)
        self.noise_modulations = np.random.uniform(0.5, 2.0, dim)
        
        # Enhanced cross-dimensional interaction
        self.cross_strength = np.random.uniform(0.5, 2.0, dim)
        self.cross_decay = np.random.uniform(0.1, 0.5, dim)
        
        # Additional polynomial shaping terms for better conditioning
        self.poly_weights = np.random.uniform(-0.5, 0.5, 4)
        
    def f(self, x):
        x_norm = x / 5.0
        f_val = 0.0
        
        # Enhanced chaotic sine components with damping
        for i in range(self.dim):
            chaotic_term = 0.0
            phase = 0.0
            for _ in range(150):
                phase = np.sin(self.chaotic_freqs[i] * phase + self.chaotic_ampls[i]) * self.chaotic_dampings[i]
            for _ in range(30):
                phase = np.sin(self.chaotic_freqs[i] * phase + self.chaotic_ampls[i]) * self.chaotic_dampings[i]
                chaotic_term += np.sin(phase * x_norm[i])
            f_val += 0.25 * chaotic_term**2
        
        # Enhanced radial basis function components with more centers
        for i in range(self.dim):
            rbf_sum = 0.0
            for j in range(5):
                rbf_sum += self.rbf_weights[i, j] * np.exp(-0.5 * ((x_norm[i] - self.rbf_centers[i, j]) / self.rbf_widths[i, j])**2)
            f_val += 0.4 * rbf_sum**2
        
        # Enhanced adaptive noise components with modulation
        for i in range(self.dim):
            noise_term = self.noise_scales[i] * np.sin(self.noise_frequencies[i] * x_norm[i]) * np.cos(self.noise_modulations[i] * x_norm[i])
            f_val += 0.2 * noise_term**2
        
        # Enhanced cross-dimensional coupling with exponential decay
        for i in range(self.dim):
            cross_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    dist = np.abs(x_norm[i] - x_norm[j])
                    weight = np.exp(-self.cross_decay[i] * dist)
                    cross_sum += weight * np.sin(x_norm[i] * x_norm[j])
            f_val += self.cross_strength[i] * cross_sum**2
        
        # Multi-scale periodic components with additional harmonics
        for scale in [0.1, 0.25, 0.5, 0.75, 1.0]:
            periodic_sum = 0.0
            for i in range(self.dim):
                periodic_sum += np.sin(scale * x_norm[i]) * np.cos(scale * 2 * x_norm[i]) + 0.3 * np.sin(scale * 3 * x_norm[i])
            f_val += 0.3 * periodic_sum**2
        
        # Enhanced global shaping with polynomial terms
        f_val += self.poly_weights[0] * np.sum(x_norm**4) + \
                 self.poly_weights[1] * np.sum(x_norm**6) + \
                 self.poly_weights[2] * np.sum(np.abs(x_norm)**3) + \
                 self.poly_weights[3] * np.sum(np.abs(x_norm)**5)
        
        return f_val