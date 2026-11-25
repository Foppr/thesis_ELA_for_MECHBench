import numpy as np

class ChaoticSineRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
        
        # Enhanced chaotic sine map parameters with fractal-like behavior
        self.chaotic_freqs = np.random.uniform(1.0, 3.0, dim)
        self.chaotic_ampls = np.random.uniform(0.2, 1.0, dim)
        self.fractal_params = np.random.uniform(0.1, 0.9, dim)
        
        # Enhanced radial basis function parameters with multi-scale centers
        self.rbf_centers = np.random.uniform(-4.0, 4.0, (dim, 5))
        self.rbf_widths = np.random.uniform(0.3, 3.0, (dim, 5))
        self.rbf_weights = np.random.uniform(-1.5, 1.5, (dim, 5))
        
        # Enhanced adaptive noise scaling with multiple frequency components
        self.noise_scales = np.random.uniform(0.1, 0.5, dim)
        self.noise_frequencies = np.random.uniform(2.0, 12.0, dim)
        self.noise_harmonics = np.random.uniform(0.5, 2.0, (dim, 3))
        
        # Cross-dimensional interaction with fractal coupling strength
        self.cross_strength = np.random.uniform(0.5, 2.0, dim)
        self.fractal_cross = np.random.uniform(0.1, 0.8, dim)
        
        # Additional fractal-like components
        self.fractal_exponents = np.random.uniform(1.5, 3.5, dim)
        self.fractal_amplitudes = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        x_norm = x / 5.0
        f_val = 0.0
        
        # Enhanced chaotic sine components with fractal behavior
        for i in range(self.dim):
            chaotic_term = 0.0
            phase = 0.0
            for _ in range(150):
                phase = np.sin(self.chaotic_freqs[i] * phase + self.chaotic_ampls[i])
            for _ in range(30):
                phase = np.sin(self.chaotic_freqs[i] * phase + self.chaotic_ampls[i])
                chaotic_term += np.sin(phase * x_norm[i]) * np.cos(phase * 0.5 * x_norm[i])
            f_val += 0.3 * chaotic_term**2
        
        # Enhanced radial basis function components
        for i in range(self.dim):
            rbf_sum = 0.0
            for j in range(5):
                rbf_sum += self.rbf_weights[i, j] * np.exp(-0.5 * ((x_norm[i] - self.rbf_centers[i, j]) / self.rbf_widths[i, j])**2)
            f_val += 0.4 * rbf_sum**2
        
        # Enhanced adaptive noise components with harmonics
        for i in range(self.dim):
            noise_term = 0.0
            for h in range(3):
                noise_term += self.noise_scales[i] * np.sin(self.noise_frequencies[i] * x_norm[i] + h * np.pi/4) * self.noise_harmonics[i, h]
            f_val += 0.2 * noise_term**2
        
        # Enhanced cross-dimensional coupling with fractal interaction
        for i in range(self.dim):
            cross_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    dist = np.abs(x_norm[i] - x_norm[j])
                    cross_sum += np.exp(-dist**2) * np.sin(x_norm[i] * x_norm[j]) * np.cos(dist * self.fractal_cross[i])
            f_val += self.cross_strength[i] * cross_sum**2
        
        # Fractal-like multi-scale periodic components
        for scale in [0.1, 0.2, 0.4, 0.6, 0.8, 1.0]:
            periodic_sum = 0.0
            for i in range(self.dim):
                periodic_sum += np.sin(scale * x_norm[i]) * np.cos(scale * 2 * x_norm[i]) * np.sin(scale * 3 * x_norm[i])
            f_val += 0.3 * periodic_sum**2
        
        # Fractal shaping components
        for i in range(self.dim):
            fractal_term = self.fractal_amplitudes[i] * np.abs(x_norm[i])**self.fractal_exponents[i]
            f_val += 0.15 * fractal_term**2
        
        # Global shaping with polynomial terms and enhanced conditioning
        f_val += 0.15 * np.sum(np.abs(x_norm)**4)
        
        return f_val