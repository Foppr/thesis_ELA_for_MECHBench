import numpy as np

class ChaoticSymmetricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters for frequency modulation
        self.freq_mod = 1.0 + 0.5 * np.sin(np.arange(dim) * np.pi / (dim + 2))
        self.decay_params = 0.1 + 0.4 * np.random.rand(dim)
        self.symmetry_break = 0.3 + 0.7 * np.random.rand(dim)
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Exponential decay component with chaotic frequency modulation
        exp_decay = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            exp_decay += np.exp(-self.decay_params[i] * np.abs(xi)) * np.sin(self.freq_mod[i] * xi)
        
        # Trigonometric coupling with symmetry breaking
        trig_coupling = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            for j in range(i+1, self.dim):
                xj = x_scaled[j]
                # Cross-dimensional trigonometric interaction with symmetry breaking
                angle = np.arctan2(xj, xi)
                coupling = np.sin(3 * angle) * np.cos(2 * angle) * (1 + self.symmetry_break[i] * xi**2)
                trig_coupling += coupling
        
        # Adaptive frequency modulation with chaotic behavior
        adaptive_freq = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            # Chaos-inducing component using sine and cosine with varying frequencies
            adaptive_freq += np.sin(5 * xi + self.freq_mod[i] * np.cos(xi)) * np.cos(3 * xi + self.freq_mod[i] * np.sin(xi))
        
        # Radial symmetry breaking with exponential modulation
        r = np.sqrt(np.sum(x_scaled**2))
        radial_symmetry = np.exp(-r**2) * np.sin(r * 2 * np.pi)
        
        # Additional chaotic high-frequency component
        chaos_component = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            chaos_component += np.sin(15 * xi + np.sin(7 * xi)) * np.cos(12 * xi + np.cos(5 * xi))
        
        # Combine all components with different weights to form the final landscape
        return 0.3 * exp_decay + 0.25 * trig_coupling + 0.2 * adaptive_freq - 0.15 * radial_symmetry + 0.1 * chaos_component