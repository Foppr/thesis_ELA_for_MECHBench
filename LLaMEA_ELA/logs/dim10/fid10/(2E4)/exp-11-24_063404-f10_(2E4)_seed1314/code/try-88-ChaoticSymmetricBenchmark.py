import numpy as np

class ChaoticSymmetricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters for frequency modulation with increased complexity
        self.freq_mod = 1.5 + 0.8 * np.sin(np.arange(dim) * np.pi / (dim + 3))
        self.decay_params = 0.2 + 0.6 * np.random.rand(dim)
        self.symmetry_break = 0.5 + 0.8 * np.random.rand(dim)
        # Additional chaotic parameters for enhanced complexity
        self.multi_freq = 2.0 + 1.5 * np.random.rand(dim)
        self.phase_shift = np.pi * np.random.rand(dim)
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Enhanced exponential decay component with chaotic frequency modulation
        exp_decay = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            exp_decay += np.exp(-self.decay_params[i] * np.abs(xi)) * np.sin(self.freq_mod[i] * xi + self.phase_shift[i])
        
        # Enhanced trigonometric coupling with symmetry breaking and cross-dimensional interactions
        trig_coupling = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            for j in range(i+1, self.dim):
                xj = x_scaled[j]
                # Cross-dimensional trigonometric interaction with enhanced symmetry breaking
                angle = np.arctan2(xj, xi)
                coupling = np.sin(5 * angle) * np.cos(3 * angle) * (1 + self.symmetry_break[i] * xi**3 + self.symmetry_break[j] * xj**3)
                trig_coupling += coupling
        
        # Enhanced adaptive frequency modulation with chaotic behavior and multiple frequencies
        adaptive_freq = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            # Chaos-inducing component using sine and cosine with varying frequencies and phase shifts
            adaptive_freq += np.sin(self.multi_freq[i] * xi + self.freq_mod[i] * np.cos(xi + self.phase_shift[i])) * np.cos(self.multi_freq[i] * xi + self.freq_mod[i] * np.sin(xi + self.phase_shift[i]))
        
        # Enhanced radial symmetry breaking with exponential modulation and additional chaotic components
        r = np.sqrt(np.sum(x_scaled**2))
        radial_symmetry = np.exp(-r**3) * np.sin(r * 3 * np.pi) * np.cos(r * 1.5 * np.pi)
        
        # Additional high-frequency chaotic component with multiple harmonics
        chaos_component = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            chaos_component += np.sin(20 * xi + np.sin(9 * xi) + np.cos(4 * xi)) * np.cos(18 * xi + np.cos(8 * xi) + np.sin(3 * xi))
        
        # Additional multi-scale chaotic interaction component
        multi_scale = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            multi_scale += np.sin(7 * xi + np.sin(12 * xi)) * np.cos(5 * xi + np.cos(10 * xi)) * np.sin(3 * xi + np.sin(6 * xi))
        
        # Combine all components with different weights to form the final landscape
        return 0.25 * exp_decay + 0.3 * trig_coupling + 0.25 * adaptive_freq - 0.1 * radial_symmetry + 0.08 * chaos_component + 0.07 * multi_scale