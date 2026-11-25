import numpy as np

class HyperChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Hyper-chaotic fractal parameters with memory effects
        self.hurst = 0.1 + 0.3 * np.random.rand(dim)
        self.amplitude = 1.5 + 4.0 * np.random.rand(dim)
        self.frequency = 0.5 + 3.0 * np.random.rand(dim)
        # Memory-dependent Gaussian peaks
        self.peak_centers = np.random.uniform(-4, 4, (dim, 3))
        self.peak_heights = 2.0 + 5.0 * np.random.rand(dim, 3)
        self.peak_widths = 0.5 + 2.0 * np.random.rand(dim, 3)
        # Time-varying saddle structures
        self.saddle_centers = np.random.uniform(-3, 3, (dim, 2))
        self.saddle_strengths = 1.0 + 3.0 * np.random.rand(dim, 2)
        # Cross-dimensional cubic couplings
        self.cubic_couplings = np.random.uniform(-0.5, 0.5, (dim, dim))
        
    def f(self, x):
        # Clip input to bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Hyper-chaotic fractal Brownian motion with memory
        fbm = 0.0
        for i in range(self.dim):
            noise = 0.0
            for k in range(1, 8):
                freq = self.frequency[i] * (2 ** k)
                amp = self.amplitude[i] / (freq ** (2 * self.hurst[i]))
                # Add memory effect with previous dimension
                if i > 0:
                    amp *= (1.0 + 0.2 * np.sin(x[i-1]))
                noise += amp * np.sin(freq * x[i])
            fbm += noise
        
        # Memory-dependent Gaussian peaks with temporal components
        gaussian = 0.0
        for i in range(self.dim):
            for j in range(3):
                peak_val = self.peak_heights[i, j] * np.exp(-0.5 * ((x[i] - self.peak_centers[i, j]) / self.peak_widths[i, j])**2)
                # Add temporal component
                temporal_factor = 1.0 + 0.3 * np.sin(0.5 * x[i] + 0.1 * i)
                gaussian += peak_val * temporal_factor
        
        # Cross-dimensional cubic couplings with time-varying coefficients
        cubic_coupling = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_strength = self.cubic_couplings[i, j] * (1.0 + 0.2 * np.cos(0.3 * x[i]))
                    cubic_coupling += coupling_strength * (x[i]**3) * (x[j]**3)
        
        # Time-varying saddle point structures with adaptive stiffness
        saddle = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                center1, center2 = self.saddle_centers[i]
                strength1, strength2 = self.saddle_strengths[i]
                # Adaptive stiffness based on position
                stiffness = 1.0 + 0.5 * np.sin(0.4 * x[i]) + 0.3 * np.cos(0.6 * x[i+1])
                saddle += stiffness * (x[i] - center1) * (x[i+1] - center2) * np.exp(-0.1 * ((x[i] - center1)**2 + (x[i+1] - center2)**2))
        
        # Multi-scale harmonic potentials with dynamic modulation
        harmonic = 0.0
        for i in range(self.dim):
            mod_freq = 1.0 + 4.0 * np.sin(0.5 * x[i])
            mod_amp = 0.5 + 1.5 * np.cos(0.3 * x[i])
            # Add temporal modulation
            temporal_mod = 1.0 + 0.2 * np.sin(0.7 * x[i] + 0.1 * i)
            harmonic += mod_amp * np.sin(mod_freq * x[i]) * temporal_mod
        
        # Adaptive conditioning with exponential weighting and dynamic scaling
        cond_weight = 0.0
        for i in range(self.dim):
            # Dynamic weight based on position and dimension
            weight = 1.0 + 0.4 * np.sin(0.7 * x[i]) + 0.3 * np.cos(0.9 * x[i]) + 0.2 * np.sin(0.5 * i)
            cond_weight += weight * (x[i]**2) / (1.0 + np.exp(-x[i]))
        
        # Combine all components with dynamic dimension scaling
        dim_factor = 1.0 + 0.1 * np.log(self.dim) + 0.05 * np.sin(0.3 * self.dim)
        return (0.20 * fbm + 0.25 * gaussian + 0.20 * cubic_coupling + 
                0.15 * saddle + 0.15 * harmonic + 0.10 * cond_weight) * dim_factor