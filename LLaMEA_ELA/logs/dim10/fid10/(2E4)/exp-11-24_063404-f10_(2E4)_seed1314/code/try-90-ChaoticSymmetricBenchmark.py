import numpy as np

class ChaoticSymmetricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters for frequency modulation with slight modifications
        self.freq_mod = 1.2 + 0.3 * np.sin(np.arange(dim) * np.pi / (dim + 3))
        self.decay_params = 0.15 + 0.35 * np.random.rand(dim)
        self.symmetry_break = 0.4 + 0.6 * np.random.rand(dim)
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Exponential decay component with modified parameters
        exp_decay = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            exp_decay += np.exp(-self.decay_params[i] * np.abs(xi)) * np.sin(self.freq_mod[i] * xi)
        
        # Trigonometric coupling with modified weights and symmetry breaking
        trig_coupling = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            for j in range(i+1, self.dim):
                xj = x_scaled[j]
                # Cross-dimensional trigonometric interaction with enhanced symmetry breaking
                angle = np.arctan2(xj, xi)
                coupling = np.sin(4 * angle) * np.cos(3 * angle) * (1 + self.symmetry_break[i] * xi**3)
                trig_coupling += 0.5 * coupling
        
        # Adaptive frequency modulation with chaotic behavior
        adaptive_freq = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            # Chaos-inducing component using sine and cosine with varying frequencies
            adaptive_freq += np.sin(6 * xi + self.freq_mod[i] * np.cos(xi)) * np.cos(4 * xi + self.freq_mod[i] * np.sin(xi))
        
        # Radial symmetry breaking with exponential modulation
        r = np.sqrt(np.sum(x_scaled**2))
        radial_symmetry = np.exp(-r**2) * np.sin(r * 3 * np.pi)
        
        # Additional chaotic high-frequency component
        chaos_component = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            chaos_component += np.sin(18 * xi + np.sin(8 * xi)) * np.cos(15 * xi + np.cos(6 * xi))
        
        # Combine all components with modified weights to form the final landscape
        return 0.25 * exp_decay + 0.3 * trig_coupling + 0.25 * adaptive_freq - 0.1 * radial_symmetry + 0.15 * chaos_component