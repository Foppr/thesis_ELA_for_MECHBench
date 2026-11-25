import numpy as np

class ChaoticSineRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
        
        # Chaotic sine map parameters with increased complexity and irregularity
        self.chaotic_freqs = np.random.uniform(1.5, 4.0, dim)
        self.chaotic_ampls = np.random.uniform(0.3, 1.5, dim)
        self.chaotic_dampings = np.random.uniform(0.7, 1.3, dim)
        
        # Enhanced radial basis function parameters with irregular spacing
        self.rbf_centers = np.random.uniform(-4.5, 4.5, (dim, 8))
        self.rbf_widths = np.random.uniform(0.2, 3.5, (dim, 8))
        self.rbf_weights = np.random.uniform(-2.0, 2.0, (dim, 8))
        
        # Adaptive noise scaling with frequency modulation and phase shifts
        self.noise_scales = np.random.uniform(0.1, 0.6, dim)
        self.noise_frequencies = np.random.uniform(3.0, 15.0, dim)
        self.noise_modulations = np.random.uniform(0.3, 2.5, dim)
        self.noise_phases = np.random.uniform(0, 2*np.pi, dim)
        
        # Enhanced cross-dimensional interaction with dynamic coupling
        self.cross_strength = np.random.uniform(0.4, 2.5, dim)
        self.cross_decay = np.random.uniform(0.05, 0.6, dim)
        self.cross_exponents = np.random.uniform(1.0, 3.0, dim)
        
        # Additional polynomial shaping terms for better conditioning
        self.poly_weights = np.random.uniform(-0.7, 0.7, 6)
        
        # Additional chaotic coupling terms between dimensions
        self.coupling_strengths = np.random.uniform(0.2, 1.0, (dim, dim))
        np.fill_diagonal(self.coupling_strengths, 0.0)
        
    def f(self, x):
        x_norm = x / 5.0
        f_val = 0.0
        
        # Enhanced chaotic sine components with damping and multiple iterations
        for i in range(self.dim):
            chaotic_term = 0.0
            phase = 0.0
            for _ in range(200):
                phase = np.sin(self.chaotic_freqs[i] * phase + self.chaotic_ampls[i]) * self.chaotic_dampings[i]
            for _ in range(50):
                phase = np.sin(self.chaotic_freqs[i] * phase + self.chaotic_ampls[i]) * self.chaotic_dampings[i]
                chaotic_term += np.sin(phase * x_norm[i])
            f_val += 0.3 * chaotic_term**2
        
        # Enhanced radial basis function components with more centers and irregular weights
        for i in range(self.dim):
            rbf_sum = 0.0
            for j in range(8):
                rbf_sum += self.rbf_weights[i, j] * np.exp(-0.5 * ((x_norm[i] - self.rbf_centers[i, j]) / self.rbf_widths[i, j])**2)
            f_val += 0.5 * rbf_sum**2
        
        # Enhanced adaptive noise components with phase shifts and modulation
        for i in range(self.dim):
            noise_term = self.noise_scales[i] * np.sin(self.noise_frequencies[i] * x_norm[i] + self.noise_phases[i]) * np.cos(self.noise_modulations[i] * x_norm[i])
            f_val += 0.25 * noise_term**2
        
        # Enhanced cross-dimensional coupling with exponential decay and power laws
        for i in range(self.dim):
            cross_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    dist = np.abs(x_norm[i] - x_norm[j])
                    weight = np.exp(-self.cross_decay[i] * (dist ** self.cross_exponents[i]))
                    cross_sum += weight * np.sin(x_norm[i] * x_norm[j])
            f_val += self.cross_strength[i] * cross_sum**2
        
        # Additional chaotic coupling between dimensions
        for i in range(self.dim):
            coupling_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling_sum += self.coupling_strengths[i, j] * np.sin(x_norm[i] + x_norm[j])
            f_val += 0.15 * coupling_sum**2
        
        # Multi-scale periodic components with additional harmonics and phase shifts
        for scale in [0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]:
            periodic_sum = 0.0
            for i in range(self.dim):
                periodic_sum += np.sin(scale * x_norm[i]) * np.cos(scale * 2 * x_norm[i]) + 0.3 * np.sin(scale * 3 * x_norm[i])
            f_val += 0.35 * periodic_sum**2
        
        # Enhanced global shaping with polynomial terms
        f_val += self.poly_weights[0] * np.sum(x_norm**4) + \
                 self.poly_weights[1] * np.sum(x_norm**6) + \
                 self.poly_weights[2] * np.sum(np.abs(x_norm)**3) + \
                 self.poly_weights[3] * np.sum(np.abs(x_norm)**5) + \
                 self.poly_weights[4] * np.sum(x_norm**8) + \
                 self.poly_weights[5] * np.sum(np.abs(x_norm)**7)
        
        return f_val