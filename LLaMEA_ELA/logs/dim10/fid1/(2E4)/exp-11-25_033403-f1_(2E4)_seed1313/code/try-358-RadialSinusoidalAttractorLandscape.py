import numpy as np

class RadialSinusoidalAttractorLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize radial basis function centers and widths
        self.rbf_centers = np.random.uniform(-4.0, 4.0, (12, dim))
        self.rbf_widths = np.random.uniform(0.5, 3.0, 12)
        self.rbf_weights = np.random.uniform(0.5, 2.5, 12)
        # Initialize sinusoidal potential parameters
        self.sin_freqs = np.random.uniform(1.0, 8.0, dim)
        self.sin_amplitudes = np.random.uniform(1.0, 4.0, dim)
        # Initialize gradient attraction forces
        self.attraction_magnitudes = np.random.uniform(0.5, 3.0, dim)
        self.attraction_centers = np.random.uniform(-3.0, 3.0, (6, dim))
        self.attraction_strengths = np.random.uniform(0.1, 1.5, 6)
        # Initialize adaptive noise parameters
        self.noise_amplitudes = np.random.uniform(0.1, 1.0, dim)
        self.noise_frequencies = np.random.uniform(0.5, 3.0, dim)
        # Initialize coupling terms between dimensions
        self.coupling_strengths = np.random.uniform(-0.5, 0.5, (dim, dim))
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Compute radial basis function potential
        rbf_potential = 0.0
        for i in range(12):
            dist_sq = np.sum((x - self.rbf_centers[i]) ** 2)
            rbf_potential += self.rbf_weights[i] * np.exp(-dist_sq / (2 * self.rbf_widths[i]**2))
        
        # Compute sinusoidal potential
        sin_potential = 0.0
        for j in range(self.dim):
            sin_potential += self.sin_amplitudes[j] * np.sin(self.sin_freqs[j] * x[j])
        
        # Compute gradient attraction forces
        attraction_force = 0.0
        for i in range(6):
            dist_sq = np.sum((x - self.attraction_centers[i]) ** 2)
            attraction_force += self.attraction_strengths[i] / (1.0 + dist_sq)
        
        # Compute coupling terms between dimensions
        coupling_terms = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_terms += self.coupling_strengths[i, j] * x[i] * x[j]
        
        # Compute adaptive noise modulation
        noise_modulation = 0.0
        for j in range(self.dim):
            noise_modulation += self.noise_amplitudes[j] * np.sin(self.noise_frequencies[j] * x[j])
        
        # Combine all components with adjusted weights
        total = 1.2 * rbf_potential + 0.8 * sin_potential + 0.5 * attraction_force + 0.3 * coupling_terms + 0.2 * noise_modulation
        
        # Add a novel component: hybrid polynomial-sinusoidal interaction
        hybrid_interaction = 0.0
        for j in range(self.dim):
            hybrid_interaction += 0.6 * x[j]**3 * np.sin(0.5 * x[j]) + 0.4 * np.cos(x[j])**2
        
        # Final combination with refined weights
        total = 1.0 * rbf_potential + 0.7 * sin_potential + 0.4 * attraction_force + 0.3 * coupling_terms + 0.2 * noise_modulation + 0.3 * hybrid_interaction
        
        return total