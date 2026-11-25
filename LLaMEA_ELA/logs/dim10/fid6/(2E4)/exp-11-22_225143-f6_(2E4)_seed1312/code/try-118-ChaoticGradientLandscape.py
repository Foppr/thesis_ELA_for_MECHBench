import numpy as np

class ChaoticGradientLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Time-varying harmonic potential parameters
        self.harmonic_freqs = np.random.uniform(2.0, 12.0, dim)
        self.harmonic_ampls = np.random.uniform(1.0, 4.0, dim)
        # Dynamic conditioning with exponentially varying exponents
        self.conditioning_exps = np.random.uniform(3.0, 8.0, dim)
        self.conditioning_scales = np.random.uniform(0.5, 2.0, dim)
        # Multi-scale fractal interference patterns
        self.fractal_freqs = np.logspace(0, 2, 10)
        self.fractal_ampls = np.random.uniform(0.1, 0.8, 10)
        # Chaotic time-varying parameters
        self.tau = np.random.uniform(0.1, 0.5, dim)
        self.coupling_strengths = np.random.uniform(0.3, 1.2, dim)
        
    def f(self, x):
        t = np.sum(x**2) / (self.dim * 100.0) + 1.0
        f_val = 0.0
        
        # Harmonic potential with time-varying frequencies
        for i in range(self.dim):
            freq = self.harmonic_freqs[i] * (1.0 + 0.3 * np.sin(t * self.tau[i]))
            ampl = self.harmonic_ampls[i] * (1.0 + 0.2 * np.cos(t * self.tau[i]))
            f_val += ampl * np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Dynamic conditioning with time-varying exponents
        for i in range(self.dim):
            exp = self.conditioning_exps[i] * (1.0 + 0.25 * np.sin(t * self.tau[i]))
            scale = self.conditioning_scales[i] * (1.0 + 0.1 * np.cos(t * self.tau[i]))
            f_val += scale * np.abs(x[i])**exp
        
        # Multi-scale fractal interference
        for i in range(10):
            freq = self.fractal_freqs[i]
            ampl = self.fractal_ampls[i]
            interference = 0.0
            for j in range(self.dim):
                interference += np.sin(freq * x[j]) * np.cos(freq * x[j])
            f_val += ampl * np.sin(interference) * np.cos(interference)
        
        # Cross-dimensional coupling with chaotic interaction
        for i in range(self.dim):
            coupling = 0.0
            for j in range(min(i+3, self.dim)):
                if i != j:
                    dist = np.abs(x[i] - x[j])
                    coupling += self.coupling_strengths[i] * np.exp(-dist**2 / (2 * 0.1**2)) * \
                               np.sin(5 * dist) * np.cos(3 * dist)
            f_val += coupling
        
        # Add time-varying chaotic noise
        noise = 0.0
        for i in range(self.dim):
            noise += np.sin(t * x[i] + i) * np.cos(t * x[i] + i)
        f_val += 0.2 * noise * np.sin(t)
        
        # Global scaling with fractal-like modulation
        global_scale = 1.0 + 0.5 * np.sin(3 * t) + 0.3 * np.cos(7 * t)
        f_val *= global_scale
        
        return f_val